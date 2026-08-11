# Figures v2 — Regeneration Pass (2026-08-11)

This directory contains **v2 redraws** of the 5 published figures, keeping the
original v1 figures in `source/` and `export/` at the repo root untouched.

## v1 → v2 progression

| Fig | v1 → v2 improvements |
|---|---|
| figkit | New: `arc()`, `tag()`, `polygon()`, `grains(angular=True)`, improved soil presets |
| 1.14 | Full Mohr **circles** (not arcs), `soil("sand")` textures, tag labels, taller canvas |
| 2.8 | **Graded grains** (varied radii), **wavy water** (cosine), **displacement vectors**, dense vs loose packing |
| 3.14 | `soil("clay")` ground, **graded sand grains** in piles, double-wall casing, tag callouts |
| 3.15 | **Textured geotextile filters**, double-layer corrugation, **fiber strands** in nonwoven |
| 3.16 | `soil("clay")` ground, detailed **crawler tracks**, mast **cross+diagonal bracing**, graded wick drain grains |

## Layout
```
v2/
├── source/          ← v2 SVG vectors
├── export/          ← v2 high-res PNG (2× scale)
└── generators/      ← v2 generator scripts + figkit_v2.py
    ├── figkit_v2.py
    ├── render_fig-1.14.py
    ├── render_fig-2.8.py
    ├── render_fig-3.14.py
    ├── render_fig-3.15.py
    └── render_fig-3.16.py
```

## Rendering v2 figures
```bash
# Pillow must be on PYTHONPATH (Hermes venv's Pillow is broken)
PY="C:/Users/Owner/AppData/Local/Programs/Python/Python312/python.exe"
PYLIB="C:/Users/Owner/AppData/Local/Temp/pylib"
VIRTUAL_ENV= PYTHONPATH="$PYLIB" "$PY" v2/generators/render_fig-1.14.py
```
