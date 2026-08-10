# HANDOFF — Hazarika Textbook Figures (GI Book A)

> **Handoff document.** Written 2026-08-10 by the previous assisting model (Hermes) for whoever regenerates the figure artwork next — human or AI.
> This file is the single source of truth for *how this repo works, what is done, what the professor asked for, and how to make the figures better.*

---

## 1. Purpose of this repo

This repository contains the **figure redraw / reconstruction project for Prof. Hazarika's ground-improvement textbook (GI Book A)** — Chapters 1–3 (Ch.1 Introduction, Ch.2 compaction/vibro-flotation/tamping in non-cohesive soils, Ch.3 sand-drain/preloading/vertical-drain methods in cohesive soils; Ch.4–7 admixture-related chapters exist as source docx but are not yet worked on).

**Why it exists:** the manuscript figures are low-quality scans / old diagrams (some half-Japanese, some missing panels, some are photos or copies from other publications). The professor annotates each figure **in Japanese in the source Word documents** (see §4), and the figures are redrawn as **clean vector SVG + high-resolution PNG**, with English labels, ready for the final book.

**The work is done by a "student worker" (the repo owner, Abinael) with heavy assistance from the Hermes agent (this assistant)**, which extracts the figures, decodes the annotations, generates the drawings programmatically, and commits drafts directly to `main`.

**Repo:** `github.com/abinaelsl/hazarika-textbook-figures` — branch `main`, local clone at `~/trading-agent/hazarika-textbook-figures` (Windows). Also on Desktop: `C:/Users/Owner/Desktop/Hazarika Repo/` is an older copy.

---

## 2. Repository layout

```
hazarika-textbook-figures/
├── README.md                          ← informal placeholder (written by repo owner, keep)
├── HANDOFF.md                         ← YOU ARE HERE
├── source/
│   ├── fig-<n>-<slug>.svg              ← editable vector per figure (generated)
│   └── _generators/
│       ├── render_fig-<n>.py          ← ONE generator script per figure
│       └── figkit.py                  ← shared drawing library (IMPLEMENTED)
├── scripts/
│   ├── render_figure.py               ← render + QA one-shot (IMPLEMENTED)
│   └── qa_figure.py                   ← QA gate (IMPLEMENTED)
├── .qa/                               ← per-figure QA reports (gitignored)
├── export/
│   └── fig-<n>-<slug>.png             ← high-res raster (2× scale, generated)
├── FIG_SPECS/                         ← per-figure specs (IMPLEMENTED)
│   ├── INDEX.md                       ← the live "what's left" tracker
│   ├── _TEMPLATE.md                   ← spec template
│   └── fig-<n>-<slug>.md              ← one spec per figure
├── Fig_Workspace/
│   ├── CH1/ CH2/ CH3/                 ← ORIGINAL manuscript docx + legacy SVGs + per-chapter README to-do lists
│   └── ...
├── GI BookA Manuscript 2022.2.2/      ← master copy of ALL manuscript docx (figs + manu per chapter)
│   ├── Chapter 1 Introduction (Figs) '26.7.30 (Ito Campus).docx     ← CURRENT Ch1 figures doc
│   ├── Chapter 2 ... (Figs)'26.7.30 Ito Campus.docx                 ← CURRENT Ch2 figures doc
│   ├── Chapter 3 ... (Fig) July 30 2026 Ito Campus.docx             ← CURRENT Ch3 figures doc
│   ├── GI BookA  Figures List.docx
│   ├── Gi Book Aの打ち合わせ結果 '22.2.11.docx                        ← old (2022) meeting-notes doc
│   ├── GI 検討事項 ('22.11.4）.docx                                   ← old (2022) review-notes doc
│   └── GI Book A 2024 May/  (+ Harada san/ subfolders)
└── .gitignore
```

**Legend of document suffixes:** `(Figs)` = figures-only doc; `(Manu)` = manuscript text; dates/places = version (`'26.7.30 (Ito Campus)` is the newest, "26.7.30" = 2026-07-30).

---

## 3. Status tracker (as of 2026-08-10)

### ✅ Completed redraws (all on `main`, pushed)
| Fig | Title | Annotation | Commit |
|---|---|---|---|
| Ch1 Fig 1.14 | Change of soil strength by reinforcement | (b) 図を再構成する (reconstruct panel b) | `3a730e2` |
| Ch2 Fig 2.8 | Loose sand and Vibration | 図を書き直す (redraw) | `912f378` |
| Ch3 Fig 3.16 | Mandrel-type Machine for Wick Driving | 図を書き直す (redraw) | `0d9582c` |
| Ch3 Fig 3.15 | Prefabricated Typical Wick Drain (JGS 2006) | 若干修正 (minor corrections) | `124cc30` |
| Ch3 Fig 3.14 | Procedures of Sand Drain Method with Casing Pipe | 若干修正 (minor corrections) | `bd7b9e9` |

Git history: `b8a6520` (original scans) → … → `0d9582c` → `912f378` → `3a730e2` → `124cc30` → `bd7b9e9` (head). **Local == remote == `bd7b9e9`.**

**2026-08-10 scaffold commit** (after `bd7b9e9`, see git log): added `figkit.py`, `scripts/qa_figure.py`, `scripts/render_figure.py`, `FIG_SPECS/` (INDEX + template + example), `.gitignore` `.qa/`, and marked §7 components IMPLEMENTED in this file.

### ⛔ Blocked (needs the professor)
| Fig | Annotation (exact) | What's needed |
|---|---|---|
| Ch2 Fig 2.9 | Grain size distribution curve and suitable range for Vibro-flotation — `Sourceを確認し、引用文献を入れる」または図を書きなす` | Confirm the SOURCE + add citation, **or** redraw it. Do not fake a data curve — ask Prof. Hazarika for the reference first. |
| Ch2 Fig 2.15 | Planning and Designing — `本文も含めてWeightとMassの定義の確認` | Confirm definitions of **Weight vs Mass** (incl. main text) before labeling. |
| Ch2 Fig 2.14 | Ground behavior by Heavy Tamping passes (Yamada 1991) — `（WとHwの修正）` | Fix **W** and **Hw** notation (need the manu to know which is which). |

### 📋 Open / not yet done
- **Insert-original scans** (`（オリジナルを入れる）` = "insert the original ASCII/scan"): **Ch2 Fig 2.5, 2.6; Ch3 Fig 3.8, 3.12, 3.13.** These are figures reproduced from other publications (Ishibashi & Hazarika 2010, D'Appolonia 1969, etc.) — the professor wants the *original* figure inserted (scan), **not** a redraw. Confirm copyright/attribution is fine; scan at high res.
- **Ch3 Fig 3.17** (Relationship of Th and U on Vertical Drain, Takagi 1955) — `（図をもう一度スキャンする）学生アルバイト` = **re-scan the figure** (student worker).
- **Ch3 Fig 3.18** (Pattern of Sand Pile and Effective Distance) — `参考文献を入れる：高木論文？` = add reference (Takagi's paper?). Research the Takagi 1955 citation.
- **Ch1 Fig 1.15** (Leaning Tower of Pisa) — per `Fig_Workspace/CH1/README.md`: "Send Photo In" (photo, not a redraw).
- **Ch1 Fig 1.1–1.7, 1.9, 1.12/1.13** — per `Fig_Workspace/CH1/README.md` to-do list: redraw/color/standardize/consult-manu as noted there.
- **Ch4–7** — source docx exist (`GI BookA Manuscript 2022.2.2/` and `GI Book 2024 May/`), no work started.

### 🔄 Revision pass (after professor feedback)
The professor + Abinael still need to review the 5 published drafts. **Known open quality note from the owner (IMPORTANT):**
> "The figures still need work on representing the soil particles better… it's still kinda low-effort-y for both figures that were pushed. We'll revise based on comments from professors."

So: **soil / particle rendering quality is the #1 known weakness** and the primary target of the system design in §7.

---

## 4. Professor's annotations — the complete "meeting notes"

The professor marks the figures **in Japanese directly in the Word docs** (highlights/red text). Decoding convention per chapter (from the `'26.7.30 (Ito Campus)` editions):

### Ch.1 (`Chapter 1 Introduction (Figs) '26.7.30 ...docx`)
| Fig | Caption | Annotation | Meaning |
|---|---|---|---|
| 1.1 | Three phase diagram of soils (Ishibashi & Hazarika 2015) | — | redraw + color |
| 1.2 | Compaction curve | — | redraw / approx OK |
| 1.3 | Compaction curve and zero air void curve | — | redraw |
| 1.4 | Difference between compaction and consolidation | — | pretty up / standardize |
| 1.5 | e-logσ curve | — | consult manu & pretty up |
| 1.6 | Settlement computation model | — | redraw |
| 1.7 | Shear strength of a soil mass | — | redraw |
| 1.8 | Failure strength criteria for soils | — | (highlighted) |
| 1.9 | Terzaghi's bearing capacity model | — | consult manu & redraw |
| 1.10 | Model diagram of soil strength increasing mechanism (Ingles & Metcalf 1972) | — | — |
| 1.11 | Increasing soil strength by consolidation | — | — |
| 1.12 | Change of soil strength by densification | highlighted | standardize labeling |
| 1.13 | Change of soil strength by solidification | highlighted | standardize labeling |
| 1.14 | **Change of soil strength by reinforcement** | **(b) 図を再構成する(学生アルバイト)** | **reconstruct panel (b)** ✅ done |
| 1.15 | Leaning Tower of Pisa, Italy | — | send photo in |
| 1.16 | Kansai international airport, Osaka | highlighted | — |
| 1.17 | Tilted buildings during Niigata earthquake | highlighted | — |
| 1.18 | Damaged residential house due to liquefaction lateral flow, 2011 Tohoku (courtesy Prof. Motoki Kazama) | highlighted | — |

### Ch.2 (`Chapter 2 ... (Figs)'26.7.30 ...docx`)
| Fig | Caption | Annotation | Meaning |
|---|---|---|---|
| 2.5 | Field compaction equipments (Ishibasi & Hazarika 2010) | （オリジナルを入れる） | insert original |
| 2.6 | Effect of field compaction with depth and number of passes (D'Appolonia et al. 1969) | （オリジナルを入れる） | insert original |
| 2.8 | **Loose sand and Vibration** | **図を書き直す（学生アルバイト）** | **redraw** ✅ done |
| 2.9 | Grain size distribution curve and suitable range for Vibro-flotation | Sourceを確認し、引用文献を入れる。または図を書きなす | confirm source & citation, or redraw ⛔ |
| 2.14 | Ground behavior by Heavy Tamping passes (Yamada 1991) | WとHwの修正 | fix W / Hw notations ⛔ |
| 2.15 | Planning and Designing | 本文も含めてWeightとMassの定義の確認 | confirm Weight vs Mass definitions ⛔ |

### Ch.3 (`Chapter 3 ... (Fig) July 30 2026 ...docx`)
| Fig | Caption | Annotation | Meaning |
|---|---|---|---|
| 3.8 | Consolidation curve of Preloading method (Ishibasi & Hazarika 2010) | （オリジナルを入れる） | insert original |
| 3.12 | Principle of vertical drain method (Ishibasi & Hazarika 2010) | （オリジナルを入れる） | insert original |
| 3.13 | Wick drain (Ishibashi & Hazarika 2010) | （オリジナルを入れる） | insert original |
| 3.14 | **Procedures of Sand Drain Method with Casing Pipe** | **若干修正（学生アルバイト）** | **minor corrections** ✅ |
| 3.15 | **Prefabricated Typical Wick Drain (JGS 2006)** | **若干修正（学生アルバイト）** | **minor corrections** ✅ |
| 3.16 | **Mandrel-type Machine for Wick Driving** | **図を書き直す（学生アルバイト）** | **redraw** ✅ |
| 3.17 | Relationship of Th and U on Vertical Drain (Takagi 1955) | 図をもう一度スキャンする （学生アルバイト） | re-scan the figure |
| 3.18 | Pattern of Sand Pile and Effective Distance | 参考文献を入れる：高木論文？ | add reference (Takagi?) |
| 3.19 | Seawall Foundation and Soil Profiles of Kansai Int'l Airport (Furudoi & Kobayashi 2009) | highlighted | — |

**Anthropological note:** the annotation syntax is consistently `図を〜する（学生アルバイト）` = "do 〜 to this figure (student worker)" — i.e. these are the tasks assigned to the repo owner. "オリジナルを入れる" NEVER means redraw; it means *insert the original published figure* (scan).

---

## 5. The exact pipeline (how the 5 published figures were made)

This is the working procedure that produced all current figures. Follow it for new redraw tasks.

### Step 0 — Tooling (Windows, MSYS bash)
- Python: `C:/Users/Owner/AppData/Local/hermes/hermes-agent/venv/Scripts/python` (has Pillow; **NO lxml** — use stdlib `zipfile`+`ElementTree` for docx reads, see helpers).
- Fonts: `C:/Windows/Fonts/arialbd.ttf`, `arial.ttf` (Arial/Helvetica look; book formatting calls for Helvetica-style).
- Helpers available in `C:/Users/Owner/AppData/Local/Temp/` (regenerate if lost — they are small):
  - `docx_extract.py <docx>` → extracts all embedded images to `media/`
  - `docx_annot.py <docx>` → prints document text in order with `[H]` markers for highlighted runs and `[IMG]` markers for images — this is how you find captions + annotations.

### Step 1 — Extract the source image
From the current chapter `(Figs)` docx, extract embedded media with `docx_extract.py` → `media/` (EMF files aren't renderable by Pillow — only use `.png`/`.jpeg`; convert others with autocontrast enhancement to `media/png/`).

### Step 2 — Identify the figure
- Build a **contact sheet** of the extracted images; `vision_analyze` each candidate to match it to the numbered caption.
- Read the caption + surrounding text via `docx_annot.py` to confirm which figure it is and what the annotation says. **Never skip this — the annotation dictates the task type** (redraw vs reconstruct vs minor corrections vs insert-original).

### Step 3 — Write ONE generator script
One Python script `source/_generators/render_fig-<n>.py` that emits **both** `source/fig-<n>-<slug>.svg` (as a list of SVG strings joined at the end) **and** `export/fig-<n>-<slug>.png` (Pillow, drawn at **2× scale** — multiply all coords by `rx=ry=2.0`; `viewBox` stays 1×). The script IS the source of truth; the SVG and PNG are regenerable twins.

### Step 4 — Vision-QA before committing
`vision_analyze` the PNG against a checklist: all panels present, labels correct, arrows point the right way, no overlapping text, geometry plausible. **Fix, re-render, re-check.** (Real bugs caught this way: SVG written as a single string instead of list; panel 2 drawn at panel-1 coordinates; dash lines missing in PNG; down-arrows instead of up-arrows in a withdrawal sequence.)

### Step 5 — Commit straight to main
```
git add source/fig-<n>-<slug>.svg export/fig-<n>-<slug>.png source/_generators/render_fig-<n>.py
git commit -m "Add Fig <n> <title> (Ch<c>, draft 1|minor-corrections pass)"
git push origin main
```
One figure per commit; drafts are public to the professor immediately. **Note:** git warns "LF will be replaced by CRLF" for generators — cosmetic, ignore.

### Pitfalls / environment quirks (learned the hard way)
- MSYS bash: `/tmp` → `C:/tmp`. Windows curl needs a real temp path, not `/dev/null`.
- `git -C <dir>` loops misbehave under MSYS — `cd` into the repo then run git directly.
- PIL `text(..., anchor="mm")` — supported. Keep the `text()` helper signature **`text(cx, cy, s, bold=False, size=20, color="#111")`** and use keyword args; positional misuse crashed a generator.
- Dashed lines: PIL has no native dash — implement a segment-walking loop (both SVG and PNG paths) so the dash survives in both twins.
- Keep the SVG `viewBox` in the *same coordinate space* as the script's numbers (1×), scale only at the PNG step.

---

## 6. What the 5 published figures actually contain (rediscovery notes)

So the next model doesn't have to re-derive them from the scans:

- **Fig 1.14 (Ch1)** — three panels: (a) uniaxial σ₁; (b) triaxial unreinforced — solid square + dashed "Deformed shape" bulge, σ₁>σ₃ [reconstructed]; (c) triaxial reinforced — 2 gray reinforcement layers with tensile arrows + "Imaginary end plate" inset; bottom Mohr diagram. **Mohr geometry decision:** physically consistent circles — radius `r = σc·sin(φ)` with `φ=30°`, zero cohesion envelope through origin; unreinforced σ3=1.0/σ1=3.0, reinforced σ3R=2.0/σ1R=6.0, `Δσ₃` line showing apparent confinement gain. Both circles tangent to the same envelope.
- **Fig 2.8 (Ch2)** — three panels of loose saturated sand under vibration: ① loose + saturated ("Pore water"/"Sand particle"), ② during vibration grains lose contact (slurry, blue wavy water lines), ③ re-settled densified (dashed original-surface line, downward settlement arrows, upward dashed sand-boil arrows with dots).
- **Fig 3.14 (Ch3)** — 7 panels: **Movement → Penetration (↓) → full penetration → Sand supply (sand dots inside pipe) → Sand-pile formation (↑ as casing withdraws, dotted sand drain grows in the soil) → complete drain left**. Vibro-hammer + Sand callouts.
- **Fig 3.15 (Ch3)** — table: **Structure vs Cross-section of Wick Type Drains**; Composite structure (ladder-type / corrugated / cell-type cores) vs Single structure (non-woven fabric); each core drawn between two horizontal geotextile-filter lines.
- **Fig 3.16 (Ch3)** — mandrel wick-driving machine, labeled redraw.

Useful in-source labels (Ch3 docx, for future figures): Fig 3.10 sand-drain cross-section → "Permeable sand layer / Soft clayey soil / Sand drains / Water flow / Sand mat / Embankment as surcharge"; Fig 3.11 vacuum consolidation → "Vacuum pump / Air & Water / Sand mat with drain pipes / Airtight membrane / Vertical drainage materials".

---

## 7. SYSTEM DESIGN — how to make the figures better and the workflow smoother

This is the plan for the next generation of figure work. It directly addresses the owner's complaint (soil particles look low-effort) and the pain points found in the first 5 figures.

### 7.1 Shared drawing library: `source/_generators/figkit.py`
**IMPLEMENTED 2026-08-10** (scaffold commit, see §3) — this section documents the design;
all components below exist in the repo and are wired. `figkit.py` ships with a self-test
swatch (`python source/_generators/figkit.py`) covering every soil preset.

Today every generator re-implements line/arrow/hatch/dots/text. Extract them once:

```python
# figkit.py — shared primitives (SVG strings + PIL twins, 2× scale)
class Canvas:            # holds SVG list + PIL image; viewBox + scale
    def line(x1,y1,x2,y2, w=1.6, color="#111", dash=None)
    def rect(x1,y1,x2,y2, w=1.6, color="#111", fill=None)
    def circle(cx,cy,r, fill=None, stroke="#111")
    def arrow(x1,y1,x2,y2, head=9, w=1.8)      # auto head direction
    def text(cx,cy,s, bold=False, size=20, color="#111", anchor="mm")
    def hatch(x1,y1,x2,y2, spacing=11, angle=45, color="#c9c9c9")
    def grain(x,y,r_min=1.5,r_max=3.5, seed=n)  # ONE particle
    def save(svg_path, png_path)                # writes both twins
```
Palette (consistent across figures): ink `#111`, secondary `#444`, soft `#888`, hatch `#c9c9c9`, sand fill `#8f8f8f`, accent blue `#1f4fa3`, accent red `#c22`, grid `#ccc`. Font: Arial; size hierarchy roughly 20–24 (title), 18–19 (labels), 14 (callouts) at 1× viewBox.

### 7.2 Soil & particle rendering standard (QUALITY BAR — the owner's #1 ask)
**Rule: never render soil as a uniform grid of identical dots.** Use:
- **Graded particles**: `grain()` picks radius from a seeded distribution (coarser at bottom of a layer, finer at top) and jitters position — reads as sand/gravel, not noise.
- **Layered hatching** for soil bodies: fine hatching (15–20 px spacing) for clay; coarser (~11 px) for sand; add a **second cross-hatch layer** for fill/embankment zones.
- **Texture presets** in figkit: `soil_texture(region, kind="sand"|"clay"|"gravel"|"reclaimed")` — one call per material region, so every figure is instantly consistent.
- **Water**: wavy blue lines (polyline of short segments), not flat rectangles.
- **Particles in motion** (vibration/liquefaction): show displacement vectors, not just colored dots.

### 7.3 Spec-first workflow: `FIG_SPECS/<fig>.md`
**IMPLEMENTED 2026-08-10** — registry at `FIG_SPECS/INDEX.md` (seeded with all of
§3/§4), template at `FIG_SPECS/_TEMPLATE.md`, filled example `fig-2.8-loose-sand-vibration.md`.

Before drawing, write a short spec (this is what makes a new model fast and keeps the professor's intent):

```markdown
# FIG 3.x <Title>
- Source: <docx> · caption verbatim · annotation verbatim + gloss
- Task type: redraw | reconstruct | minor-corrections | insert-original
- Panels: P1 … Pn  (count, layout direction)
- Labels (EN): …    Labels (JA): …   (book is EN → English default; JA on request)
- Geometry notes: <Mohr rule, angles, arrows, dims>
- Quality bar: <soil texture type per region, grain grading, water style>
- Status: pending | in-progress | done | blocked(<why>)
```
Keep a registry `FIG_SPECS/INDEX.md` — the live "what's left" tracker (supersedes the scattered `Fig_Workspace/*/README.md` to-do lists). A figure is "spec'd" before any SVG is touched.

### 7.4 Automated QA gate: `scripts/qa_figure.py <fig>`
**IMPLEMENTED 2026-08-10.** Usage: `python scripts/qa_figure.py fig-3.15` (number-only OK).
Run before every commit. Checks:
1. SVG well-formed XML, `viewBox` = expected canvas, parses.
2. PNG exists, non-blank (>0.5% non-white pixels in a probe region), same dimensions as expected (2×).
3. Generator script **re-runs byte-identically** (deterministic — reseed RNGs per figure!) → `svg/png` unchanged after re-render.
4. Every label from the spec appears in the SVG text layer.
5. Emit a one-page `QA_REPORT.md` per figure (or one line into `FIG_SPECS/INDEX.md`).
Failures are advisory warnings, not blockers (drafts ship early), but the report tells you exactly what to look at.

### 7.5 Command wrappers
**IMPLEMENTED 2026-08-10.**

```bash
python scripts/render_figure.py fig-3.10        # render + QA + report, one shot
python scripts/qa_figure.py fig-3.10
```
`render_figure.py` finds `source/_generators/render_fig-3.10.py`, runs it, then QA, then prints `OK` / the check list.

### 7.6 Conventions (keep from the first 5 figures + book formatting)
- English labels by default; Japanese offered as an option per figure. Title case for figure-level labels; first-letter caps for in-figure labels. (README's "Formatting" section: Helvetica font, clear labeling.)
- `viewBox` in 1× coordinate space; PNG at 2×. Canvas sizes: ~900×440 (landscape panels), ~900×620 (tables), scaled per content.
- One commit per figure; message: `Add Fig <n> <title> (Ch<c>, draft 1|minor-corrections pass)`; commit generator + svg + png together. Push to `main` immediately (professor sees drafts live).

### 7.7 Faster, easier round-trips
- Extract the annotation + caption **programmatically** (`docx_annot.py`) instead of reading pages — already proven.
- When a figure must be *redrawn*, first re-derive geometry from the **labels in the docx text layer** (e.g. Ch3 labels for 3.10/3.11 above) — faster and more accurate than squinting at scans.
- Batch by task type: do all `insert-original` in one sitting (they're scans, not drawings), all `minor-corrections` next, etc.
- Keep figure numbers in filenames everywhere: `fig-<number>-<slug>.{svg,png,py,md}`.

### 7.8 Flow for the next batch (recommended starting point)
1. Land this handoff; install `figkit.py` + `qa_figure.py` + `render_figure.py` scaffolds.
2. Write `FIG_SPECS/` + `INDEX.md` seeded from §3/§4 tables.
3. Next coding targets (easiest → hardest): **Fig 2.9** (once prof confirms source; or redraw with a real citation), **Ch1 1.1/1.2/1.3/1.6/1.7** (redraws), **Ch3 3.10/3.11** (labels already in-text), then scan batches (2.5, 2.6, 3.8, 3.12, 3.13, 3.17).
4. Revision pass on the 5 published figures — apply the §7.2 soil-quality bar and any professor comments.

---

## 8. Definition of done (checklist for every figure)

- [ ] Spec exists in `FIG_SPECS/` (or INDEX row) with caption+annotation verbatim
- [ ] Task type honored: redraw vs reconstruct vs minor corrections vs insert-original (no mixing!)
- [ ] Generator script emits SVG + PNG twins; no hand-edited binaries
- [ ] Soil/material rendering meets §7.2 quality bar (no uniform-dot grids)
- [ ] Labels in the documented language; no spelling errors ("Effctof", "achive" type typos fixed)
- [ ] QA gate passed (or warnings reviewed & logged)
- [ ] SVG + PNG + generator committed to `main` and pushed
- [ ] INDEX.md status updated to `done`

---

## 9. Environment cheat-sheet

| Item | Value |
|---|---|
| Repo local path | `~/trading-agent/hazarika-textbook-figures` (= `C:\Users\Owner\trading-agent\...`) |
| Remote | `github.com/abinaelsl/hazarika-textbook-figures` |
| Python | `C:/Users/Owner/AppData/Local/hermes/hermes-agent/venv/Scripts/python` (Pillow ✓, lxml ✗) |
| Fonts | `C:/Windows/Fonts/arialbd.ttf`, `arial.ttf` |
| Temp helpers | `C:/Users/Owner/AppData/Local/Temp/docx_{extract,annot}.py` |
| Old figure work dirs | `C:/Users/Owner/AppData/Local/hermes/work/hazarika/{ch1,ch2,ch3}/` (media extracts, contact sheets) |
| Owner | Abinael (repo owner, "student worker"); Prof. Hazarika reviews |
| Language | English in figures; Japanese annotations from professor; owner speaks Bahasa Indonesia — chat casually, short, emoji ok |

*Leave it better than you found it: every figure you add should be reproducible from `source/_generators/` alone.*