# HANDOFF — Hazarika Textbook Figures (GI Book A)

> Single source of truth for the figure redraw project. Written 2026-08-10,
> compressed 2026-08-11 for token efficiency. Repo: `abinaelsl/hazarika-textbook-figures`
> (main, local `~/trading-agent/hazarika-textbook-figures`). Live status: `FIG_SPECS/INDEX.md`.

## 1. Purpose
Redraw low-quality scans in Prof. Hazarika's ground-improvement textbook
manuscript (Ch.1-3 active: Ch.1 intro, Ch.2 compaction/vibro/tamping
non-cohesive, Ch.3 sand-drain/preloading/vertical-drain cohesive; Ch.4-7 docx
exist, NOT worked). The professor marks figures **in Japanese inside the Word
docs** (highlights/red text); figures are redrawn as clean vector SVG + hi-res
PNG, English labels. Owner = "student worker" (Abinael); assistant (Hermes)
extracts, decodes annotations, generates, commits directly to `main`.

## 2. Layout (production files)
```
source/fig-<n>-<slug>.svg + export/fig-<n>-<slug>.png   ← CURRENT (v3) twins, generated
source/_generators/figkit.py + render_fig-<n>.py        ← CURRENT (v3) library + generators
v1/source/ v1/export/ v1/source/_generators/            ← v1 archive, reference only, do NOT edit
v2/source/ v2/export/ v2/generators/ (figkit_v2.py)      ← v2 archive, reference only, do NOT edit
scripts/{render_figure,qa_figure,docx_extract,docx_annot}.py
FIG_SPECS/INDEX.md (live tracker) · _TEMPLATE.md · fig-<n>-<slug>.md
GI BookA Manuscript 2022.2.2/   ← CANONICAL source docx ('26.7.30 = current editions)
GI Book 2024 May/               ← Ch4-7 docx, untouched
Fig_Workspace/                  ← legacy sketches + stale to-do READMEs (IGNORE)
```
Root `source/`/`export/` is always the current canonical generation — work
against it, never against `v1/` or `v2/`. Those two are frozen snapshots kept
only so the redraw progression (v1 → v2 → v3) stays visible; if you improve a
figure again, bump root in place (or archive today's root as `v3/` first if
you want it kept too — there's no fixed cap on how many generations to keep,
just don't silently overwrite a snapshot once it's archived).

## 3. Status (2026-08-17, v3)
- **Done** (commit → source/): Ch1 1.14; Ch2 2.8; Ch3 3.16, 3.15, 3.14. This
  is generation **v3** — built on v2's figkit (graded grains, soil() presets,
  wavy water, tag() labels, full Mohr circles, detailed machine parts) with
  the bugs below fixed. v1 (first redraws) and v2 (texture/geometry pass)
  are kept as archives under `v1/` and `v2/` respectively — see §2.
- **v3 fixes over v2** (see figkit.py `subtext()`/`badge_title()`): replaced
  every Unicode subscript (σ₁ σ₃ etc.) and circled-digit (①②③) glyph — Arial
  lacks those codepoints on both Windows and macOS, they rendered as tofu
  boxes (□) even in the "done" PNGs (both v1 and v2 had this). Also: font
  paths now resolve across Windows/macOS/Linux instead of hardcoding
  `C:/Windows/Fonts`, and every generator's output path is repo-relative
  (`dirname x3` from `__file__`) instead of a hardcoded `C:/Users/Owner/...`
  path — run `python3 source/_generators/render_fig-<n>.py` from anywhere and
  it finds the repo root itself. Fixed a stray-divider bug in fig 3.15 (a
  composite-row separator line leaked into the Single-structure band) and a
  label/diagram text collision in the same figure. Fig 1.14 had a caption
  overlapping its own arrow label, and its τ-axis label overlapping the
  "Failure envelopes" title — both repositioned. Fig 2.8's panel titles were
  also wider than their panels (independent of the tofu bug) — wrapped to two
  lines, and the "densified" panel was barely denser than the "loose" panel
  (grain count bumped so the contrast actually reads). Also caught by the
  repo's own `qa_figure.py`: `_esc()` (XML-escaping for SVG text) was a
  complete no-op — `.replace("&", "&")` instead of `"&amp;"` — so any label
  with a literal `&` produced invalid SVG; fixed.
- **Blocked (needs professor):** Ch2 2.9 (grain-size curve — confirm source
  citation before drawing, do NOT fake data), 2.14 (W/Hw notation), 2.15
  (Weight vs Mass definition).
- **Open:** Ch1 1.1-1.9/1.12/1.13 redraws; Ch2 2.10/2.13; Ch3 3.10/3.11
  (labels already in docx text); 3.18 (add Takagi 1955 reference).
- **Scan tasks (insert ORIGINAL scan, never redraw):** Ch2 2.5/2.6; Ch3 3.8/3.12/3.13; Ch3 3.17 re-scan; Ch1 1.15 photo.

## 4. Professor's annotations (decode convention)
`図を〜する（学生アルバイト）` = "do ~ to this figure (student worker)".
`オリジナルを入れる` = insert the ORIGINAL published figure (scan) — NEVER a redraw.
Full per-figure table: `FIG_SPECS/INDEX.md` (Task + Status + Notes columns).

### Annotation glossary (Japanese → task)
| Kanji | Task |
|---|---|
| 図を書き直す | redraw |
| 図を再構成する | reconstruct (panel) |
| 若干修正 | minor corrections |
| オリジナルを入れる | insert original scan |
| 図をもう一度スキャンする | re-scan |
| 本文含めて〜の定義の確認 | confirm definition w/ main text |
| Sourceを確認し、引用文献を入れる | confirm source + add citation |

## 5. Pipeline (proven — how all figures were made)
1. **Extract:** `scripts/docx_extract.py <docx>` → media/ (stdlib zipfile;
   EMF NOT renderable — use .png/.jpeg, autocontrast enhance).
2. **Identify:** contact sheet → vision match each image to numbered caption;
   `scripts/docx_annot.py` gives caption + `[H]`-marked annotation runs. NEVER
   skip — annotation dictates task type.
3. **Write ONE generator** `source/_generators/render_fig-<n>.py` emitting BOTH
   `source/fig-<n>-<slug>.svg` (list of strings, viewBox 1x) and
   `export/fig-<n>-<slug>.png` (PIL at 2x scale, multiply coords by 2). Script
   IS source of truth; twins regenerable. Seed EVERY random (byte-identical
   re-renders).
4. **Vision-QA** the PNG: all panels, labels correct, arrows point right,
   no overlap, geometry plausible. Fix → re-render → re-check. (Real catches:
   withdrawal arrows pointing down; panel drawn at wrong offsets; dash lines
   missing.)
5. **Commit** generator+svg+png together, one figure per commit, straight to
   `main`, push immediately (professor sees drafts live).

## 6. Quality bar (owner's #1 ask — "low-effort" was the complaint)
- NEVER uniform grid of identical dots. `figkit.soil()`/`grains()` presets:
  seeded graded grains (coarser at bottom), per-material hatching (clay ~7px
  fine, sand ~12px, gravel ~16px angular, fill = cross-hatch), wavy water.
- Physics consistent (e.g. Mohr circles tangent to ONE failure envelope,
  r = σc·sinφ; settlement arrows DOWN, withdrawal arrows UP).
- Labels: EN by default (JA on request); tag() white-bg labels over hatching.
- Fonts Arial; hierarchy ~20-24 title / 18-19 labels / 14 callouts.
- Draft-commit-iterate; never skip quality bar. Vague notes (若干修正) = rebuild
  cleanly + state interpretation in commit message.

## 7. Environment (Windows, MSYS bash)
| Item | Value |
|---|---|
| Python | `C:/Users/Owner/AppData/Local/Programs/Python/Python312/python.exe` |
| **Pillow BROKEN in Hermes venv** → use temp pylib | `py -m pip install --target C:/Users/Owner/AppData/Local/Temp/pylib Pillow`, then `VIRTUAL_ENV= PYTHONPATH=C:/Users/Owner/AppData/Local/Temp/pylib python ...` |
| Fonts | `C:/Windows/Fonts/arialbd.ttf`, `arial.ttf` |
| Helpers | `scripts/docx_extract.py`, `scripts/docx_annot.py` (regenerate if lost — small) |
| QA | `scripts/qa_figure.py <fig>` (well-formed, determinism, labels) · `scripts/render_figure.py <fig>` (render+QA one-shot) |
| Owner | Abinael (repo owner); Prof. Hazarika reviews; chat language casual (Bahasa Indo ok), English in figures |

### Pitfalls (learned the hard way)
- XML-escape `& < >` in every label (QA catches raw `&`).
- SVG = list of strings (`'str' object has no attribute append'`).
- PIL has no native dash → segment-walking loop in BOTH twins.
- MSYS: `/tmp` → `C:/tmp`; `git -C` loops misbehave — cd in first; CRLF warnings cosmetic.
- Vision model may misread complete circles as arcs — verify with `getpixel()` before "fixing".
- Canvas must fit largest circle: `oy + r ≤ height` (Fig 1.14 needed 920px tall).
- QA determinism check regenerates files — re-run QA after any refresh.

## 8. Definition of done
Spec in FIG_SPECS → task type honored (no mixing redraw/scan) → ONE generator
emits SVG+PNG twins → §6 quality bar met → labels EN, no typos → QA passed or
warnings logged → committed (gen+svg+png) to main + pushed → INDEX.md status=done.

*Leave it better than you found it: every figure reproducible from `source/_generators/` alone.*