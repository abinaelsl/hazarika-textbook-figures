# Abi'sFigures — image-model redraws by Abinael (2026-09-16)

**Author: Abinael (abinaelsl).** Kept separate from `Miguel'sPitOfDespair/`
so the two workers' output stays distinguishable.

Ten of the professor's schematic redraw tasks, produced with the Higgsfield MCP
(`nano_banana_pro` requested; the service ran them on `nano_banana_2`), each
**traced from the original figure** supplied as an `image_references` input —
the crops in `refs/` are exactly what each generation saw.

> **These are raster-only.** They do NOT follow the repo's generator+SVG+PNG
> twin convention (README "Conventions"); there is no `render_fig-*.py` behind
> them and they cannot be re-rendered deterministically. Re-running the same
> prompt gives a *different* image. Treat them as **drafts for the professor**,
> not as finished twins. If one is accepted and later needs an edit, it must be
> either re-generated from scratch or rebuilt as a real generator.

## Provenance

| Fig | Task (annotation) | Reference | Post-edits applied |
|---|---|---|---|
| 3.16 | 図を書き直す；学生アルバイト — redraw (also on the 検討事項 要修正 list) | `ch3/image17.jpeg` (autocontrast) | "Ground line" / "Road wheels" were transposed — the two leaders were correct, so the words were swapped and re-stamped |
| 4.9 | 学生に書き直し — redraw | `ch4/image14.jpeg` | none |
| 4.18 | 書き直す：学生へ — redraw | `ch4/image21.jpeg` | none |
| 5.1 | Hatchingを入れる — add hatching | `ch5/image5.png` | none |
| 5.5 | 書き直す：学生へ — redraw | `ch5/image6.png` | none |
| 5.18 | イメージを書く直す：学生へ — redraw | `ch5/image26.jpeg` | none |
| 6.1 | JA→EN labels (glossary in docx) | `ch6/image1.jpeg` | erased a duplicated "COMPACTION" in panel (b) |
| 6.2 | JA→EN labels (glossary in docx) | `ch6/image2.jpeg` | "Reinforcement of soils" re-stamped — model rendered it as overlapping garbled glyphs |
| 6.13 | JA→EN labels (glossary in docx) | `ch6/image13.png` | erased a duplicated "SAND MAT" label + its leader line |
| 7.6 | JA→EN labels (glossary in docx) | `ch7/image6.jpeg` | erased a ghost of the original Japanese text and a baked-in "Figure 1 …" caption |
| 7.8 | JA→EN labels (glossary in docx) | `ch7/image8.png` → **cropped** to the schematic | regenerated; see note below |

Post-edits are reproducible via `repair.py` (Pillow; white-box + Arial re-stamp).

## Notes / known deviations
- **3.16 already had a v3 generator version** (`export/fig-3.16-mandrel-machine.png`,
  commit `0d9582c`). That one is *not* deleted — it remains the reproducible
  twin. This raster draft is an alternative: it follows the original sketch more
  closely (the sketch shows a **wheeled** carrier; the v3 generator drew crawler
  tracks) and every label now has a leader line, which the v3 labels lacked.
  The professor picks which to keep.
- **7.8 needed two attempts.** The reference is a screenshot of a Japanese PDF
  *viewer*; the first generation faithfully reproduced the browser chrome,
  taskbar and body text. Cropping the reference down to the bare schematic
  fixed it. Reading the real original also corrected the glossary: 冷凍圧縮機
  (③ compressor) and 凝縮器 (④ condenser) are **separate** components, not the
  single "refrigeration compressor and condenser" the docx wordlist implied,
  and there is no "brine supply" label.
- **Capitalisation:** 6.1 and 6.13 came back ALL-CAPS, 4.18 and 5.18 Title Case.
  README asks for first-letter caps only. Left as generated — restamping every
  label risks more damage than it fixes. Flag if the professor cares.
- **7.8** retains two faint grey smudges over "Condenser" and "Cooling tower".
- Figures plotting real data were **not** generated — see
  `../FIG_SPECS/ANNOTATION_AUDIT.md` §1a.

## Still missing a reference
**5.6** (Procedure Types of Permeation Grouting) and **5.20** (Typical
applications of DMM) are stored in the docx as **EMF vector objects**, which
are not renderable by the stdlib extractor — there is no raster original to
trace. Options: open the docx in Word and export those two figures as PNG, or
draw them from the main text. Not generated.
