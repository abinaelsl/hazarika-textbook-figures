# Hazarika Textbook Figures (GI Book A)

Redraw project for Prof. Hazarika's ground-improvement textbook figures (Ch.1-3
active; Ch.4-7 docx exist, untouched). The professor annotates figures in
Japanese in the source Word docs; we redraw them as clean SVG+PNG twins with
English labels.

## Read order (new model — do this, in this order)

1. `README.md` (this file) — 30 seconds
2. `HANDOFF.md` — purpose, professor's annotation tables, pipeline, quality bar, pitfalls
3. `FIG_SPECS/INDEX.md` — live tracker (what's done/open/blocked)
4. For any figure: its generator under `source/_generators/` + `figkit.py`
   — the script IS the figure.

**Never read the docx as text**; extract media with `scripts/docx_extract.py` /
annotations with `scripts/docx_annot.py` (stdlib, no lxml).

## Layout

```
README.md  HANDOFF.md  FIG_SPECS/ (tracker+specs)
source/               SVG vectors (v3, current)     export/    PNG (2x, v3, current)
source/_generators/   figkit.py + render_fig-*.py (v3, current)
v1/  v2/              frozen reference archives of earlier redraw generations — do not edit
scripts/     render_figure.py · qa_figure.py · docx helpers
GI BookA Manuscript 2022.2.2/   ← CANONICAL source docx (current editions = '26.7.30 / 2023 Shinsaibashi)
GI Book 2024 May/               ← Ch4-7 docx (untouched)
Fig_Workspace/                  ← legacy sketches + old READMEs (ignore, superseded by source/ + FIG_SPECS)
```

## Render / QA one figure

Generator output paths and font lookup are repo-relative / cross-platform
(figkit.py tries Windows, macOS, then Linux font paths in turn) — run from
anywhere, on any OS, no path edits needed:

```bash
python3 source/_generators/render_fig-1.14.py      # emits SVG + PNG twins
python3 source/_generators/figkit.py               # self-test swatch
python3 scripts/qa_figure.py 1.14                   # QA gate
```

```bash
# Windows; Pillow in the Hermes venv is BROKEN — use system python + temp pylib:
PY="C:/Users/Owner/AppData/Local/Programs/Python/Python312/python.exe"
PYLIB="C:/Users/Owner/AppData/Local/Temp/pylib"
export VIRTUAL_ENV= PYTHONPATH="$PYLIB"
"$PY" source/_generators/render_fig-1.14.py        # emits SVG + PNG twins
"$PY" source/_generators/figkit.py                 # self-test swatch
"$PY" scripts/qa_figure.py 1.14                    # QA gate
```

## Conventions (non-negotiable)

- One generator per figure; SVG+PNG are regenerable twins from the SAME script. Never hand-edit binaries.
- Soil must look like SOIL: graded seeded grains, per-material hatching, wavy water — never uniform dot grids. (Owner's #1 quality ask.)
- English labels, Arial/Helvetica; title case captions, first-letter caps in-figure labels.
- `viewBox` in 1x coords, PNG at 2x scale. Seed every RNG (deterministic re-renders).
- Commit generator+svg+png together, one figure per commit, straight to `main` (professor sees drafts live).

## License

Open for educational use.