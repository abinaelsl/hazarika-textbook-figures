# FIG 2.8 Loose sand and Vibration

- **Source doc:** `Chapter 2 without Admixture in Non-cohesive Soils (Figs)'26.7.30 Ito Campus.docx`
  · caption verbatim: `"Fig.2.8. Loose sand and Vibration"`
- **Annotation (verbatim):** `図を書き直す（学生アルバイト）`
- **Annotation gloss:** "redraw (student worker)"
- **Task type:** `redraw`
- **Reference citation in caption:** none (original schematic)

## Panels
- P1 — Loose saturated sand at rest: grains + pore water between grains
  ("Pore water" / "Sand particle" callouts)
- P2 — During vibration: grains lose contact (fluidized/slurry), wavy blue
  water lines between grains, small displacement vectors
- P3 — After vibration: re-settled densified pack; dashed line = original
  ground surface; downward settlement arrows; upward dashed sand-boil
  arrows with dots at top

## Labels (EN):
- Pore water, Sand particle, Before vibration,
- During vibration, After vibration, Settlement, Sand boil

## Labels (JA) [if requested]:
- ゆるい砂と振動 / 間隙水 / 砂粒子 / 液状化 / 沈下 / 砂杭(噴砂)

## Geometry notes
- 3 panels, horizontal (1×3); ground surface line across panels ~y=260
- P3: dashed original-surface line ABOVE final surface; ↓ settlement;
  ↑ dashed sand-boil arrows (with dots) rising from surface
- Mohr/vector rule: displacement arrows short, direction-consistent

## Quality bar (must pass, HANDOFF §7.2)
- soil regions: `sand` preset (hatch 12px @45° + graded grains 1.4–3.0),
  seeded per panel (seed = panel index)
- grains: graded, position-jittered — NOT uniform dots
- water: `wavy()` blue lines; motion shown with vectors in P2
- English labels, first-letter caps for in-figure labels

## Status: `done` (commit `912f378`) — revision pass pending professor feedback