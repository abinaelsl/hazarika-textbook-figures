#!/usr/bin/env python3
"""render_figure.py <fig> — render + QA in one shot (HANDOFF.md §7.5).

Usage:
    python scripts/render_figure.py fig-3.10
    python scripts/render_figure.py 3.10

Finds source/_generators/render_fig-<n>.py, runs it (regenerates BOTH
svg+png twins), then runs the QA gate. Exit 0 = clean render.
"""
import subprocess
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent


def normalize(fig: str) -> str:
    fig = fig.strip().lower()
    if fig.startswith("fig-"):
        fig = fig[4:]
    return fig


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        return 2
    fig = normalize(sys.argv[1])
    stem = f"fig-{fig}"
    gen = REPO / "source" / "_generators" / f"render_{stem}.py"
    if not gen.exists():
        print(f"ERROR: generator not found: {gen.relative_to(REPO)}")
        return 1

    print(f"== rendering {stem} ==")
    r = subprocess.run([sys.executable, str(gen)], capture_output=True,
                       text=True, cwd=REPO, timeout=300)
    if r.returncode != 0:
        print("generator FAILED:\n" + r.stderr[-1500:])
        return 1
    for line in (r.stdout or "").splitlines()[-5:]:
        print("  gen:", line)

    sys.path.insert(0, str(REPO / "scripts"))
    import qa_figure  # local import: scripts/ may not be on path otherwise
    qa_code = qa_figure.run(fig)
    print(f"\n== {stem}: {'PASS' if qa_code == 0 else 'FAIL'} ==")
    return qa_code


if __name__ == "__main__":
    sys.exit(main())