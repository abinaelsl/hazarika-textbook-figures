#!/usr/bin/env python3
"""qa_figure.py <fig> — QA gate for one generated textbook figure.

Checks (per HANDOFF.md §7.4):
  1. SVG exists, is well-formed XML, viewBox parses
  2. PNG exists, dimensions match 2x viewBox, non-blank (has ink)
  3. Generator re-runs DETERMINISTICALLY (byte-identical svg+png after re-run)
  4. Every "Labels (EN):" entry in FIG_SPECS/<fig>.md appears in the SVG text

Exit code: 0 = no hard failures (warnings allowed) | 1 = hard failure.
Report written to .qa/<fig>.md (gitignored).

Usage:
    python scripts/qa_figure.py fig-3.15
    python scripts/qa_figure.py 3.15            (number-only also works)
"""
import hashlib
import re
import subprocess
import sys
import xml.etree.ElementTree as ET
from pathlib import Path

from PIL import Image

REPO = Path(__file__).resolve().parent.parent
QA_DIR = REPO / ".qa"


def sha256(p: Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest()[:12]


def normalize(fig: str) -> str:
    fig = fig.strip().lower()
    if fig.startswith("fig-"):
        fig = fig[4:]
    if "." not in fig.split("-")[0]:
        fig = fig  # already like "3.15"
    return fig


def find_paths(fig: str):
    stem = f"fig-{fig}"  # may be number-only ("3.15") or with slug ("3.15-wick-...")
    # artifact names carry slugs: glob by number prefix
    def first(glob_pat: str):
        cands = sorted(glob_pat)
        return cands[0] if cands else None
    gen = first((REPO / "source" / "_generators").glob(f"render_{stem}*.py"))
    svg = first((REPO / "source").glob(f"{stem}*.svg"))
    png = first((REPO / "export").glob(f"{stem}*.png"))
    # spec: exact match or by number prefix (e.g. fig-2.8-loose-sand-vibration)
    spec = first((REPO / "FIG_SPECS").glob(f"{stem}*.md"))
    if spec is None:
        head = fig.split("-")[0]  # e.g. "2.8" from "2.8-loose-sand-vibration"
        spec = first((REPO / "FIG_SPECS").glob(f"{head}*.md"))
    return gen, svg, png, spec


def check_svg(svg: Path, checks: list):
    if not svg.exists():
        checks.append(("FAIL", "svg", f"missing: {svg.name}"))
        return None
    try:
        tree = ET.parse(svg)
        root = tree.getroot()
    except ET.ParseError as e:
        checks.append(("FAIL", "svg", f"not well-formed XML: {e}"))
        return None
    vb = root.get("viewBox")
    if not vb:
        checks.append(("WARN", "svg", "no viewBox attribute"))
        return None
    parts = vb.split()
    if len(parts) == 4:
        try:
            w, h = float(parts[2]), float(parts[3])
            checks.append(("PASS", "svg", f"viewBox {w:.0f}x{h:.0f} OK"))
            return w, h
        except ValueError:
            pass
    checks.append(("WARN", "svg", f"unparsable viewBox: {vb!r}"))
    return None


def check_png(png: Path, checks: list, view):
    if not png.exists():
        checks.append(("FAIL", "png", f"missing: {png.name}"))
        return
    im = Image.open(png).convert("L")
    w, h = im.size
    if view:
        ew, eh = int(view[0] * 2), int(view[1] * 2)
        scale = w / view[0] if view[0] else 0
        if abs(w - ew) > max(2, 0.12 * ew) or abs(h - eh) > max(2, 0.12 * eh):
            checks.append(("WARN", "png", f"size {w}x{h} != 2x viewBox {ew}x{eh} (scale {scale:.2f}x)"))
        else:
            checks.append(("PASS", "png", f"size {w}x{h} ~ 2x viewBox (scale {scale:.2f}x)"))
    hist = im.histogram()
    total = w * h
    white = sum(hist[240:])
    dark = sum(hist[0:120])
    frac_ink = (total - white) / total
    frac_dark = dark / total
    if frac_ink < 0.001:
        checks.append(("WARN", "png", f"nearly blank: ink={frac_ink:.4%}"))
    elif frac_dark < 0.0002:
        checks.append(("WARN", "png", "very few dark pixels (check content)"))
    else:
        checks.append(("PASS", "png", f"ink={frac_ink:.2%}, dark={frac_dark:.2%}"))


def check_determinism(gen: Path, svg: Path, png: Path, checks: list):
    if not gen.exists():
        checks.append(("WARN", "determinism", f"no generator {gen.name} — skipped"))
        return
    if not svg.exists() or not png.exists():
        checks.append(("WARN", "determinism", "artifacts missing — skipped"))
        return
    before = (sha256(svg), sha256(png))
    r = subprocess.run([sys.executable, str(gen)], capture_output=True,
                       text=True, cwd=REPO, timeout=300)
    if r.returncode != 0:
        checks.append(("FAIL", "determinism", f"generator crashed:\n{r.stderr[-500:]}"))
        return
    after = (sha256(svg), sha256(png))
    if after == before:
        checks.append(("PASS", "determinism", "re-run byte-identical (deterministic)"))
    else:
        checks.append(("FAIL", "determinism",
                       "re-run CHANGED artifacts — generator not deterministic; "
                       "files refreshed to latest output, review git diff"))


def spec_labels(spec):
    if spec is None or not spec.exists():
        return []
    txt = spec.read_text(encoding="utf-8", errors="replace")
    labels = []
    m = re.search(r"^#{1,4}\s*Labels?\s*(?:\(EN\)|EN)?\s*:(.*?)(?=^#{1,4} |\Z)", txt, re.M | re.S)
    if m:
        for raw in m.group(1).splitlines():
            s = raw.strip().strip("`").rstrip(",")
            if not s:
                continue
            if s.startswith("-"):
                s = s[1:].strip().strip("`").rstrip(",")
            for part in s.split(","):
                part = part.strip()
                if part:
                    labels.append(part)
    return list(dict.fromkeys(labels))


def check_labels(spec: Path, svg: Path, checks: list):
    labels = spec_labels(spec)
    if not labels:
        checks.append(("WARN", "labels", "no spec / no Labels (EN) line — skipped"))
        return
    svg_txt = svg.read_text(encoding="utf-8") if svg.exists() else ""
    missing = [lab for lab in labels if lab and lab.lower() not in svg_txt.lower()]
    if not missing:
        checks.append(("PASS", "labels", f"all {len(labels)} spec labels present"))
    else:
        checks.append(("WARN", "labels", f"missing from SVG: {missing}"))


def run(fig: str, quiet: bool = False) -> int:
    fig = normalize(fig)
    gen, svg, png, spec = find_paths(fig)
    checks = []
    view = check_svg(svg, checks)
    check_png(png, checks, view)
    check_determinism(gen, svg, png, checks)
    check_labels(spec, svg, checks)

    n_fail = sum(1 for st, _, _ in checks if st == "FAIL")
    n_warn = sum(1 for st, _, _ in checks if st == "WARN")
    QA_DIR.mkdir(exist_ok=True)
    report = QA_DIR / f"{'fig-' + fig}.md"
    lines = [f"# QA report: fig-{fig}", f"generated: {__import__('datetime').date.today()}",
             "", "| status | check | detail |", "|---|---|---|"]
    for st, name, detail in checks:
        lines.append(f"| {st} | {name} | {detail.replace(chr(10), ' ; ')} |")
    lines.append("")
    lines.append(f"**Result: {'FAIL' if n_fail else 'pass'}** ({n_fail} fail, {n_warn} warn)")
    report.write_text("\n".join(lines), encoding="utf-8")

    if not quiet:
        for st, name, detail in checks:
            print(f"[{st:4s}] {name:12s} {detail}")
        print(f"\nfig-{fig}: {'FAIL' if n_fail else 'PASS'} — {n_fail} fail, {n_warn} warn -> {report.name}")
    return 1 if n_fail else 0


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(2)
    sys.exit(run(sys.argv[1]))