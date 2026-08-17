# FIG_SPECS — live figure tracker & specs

**Registry convention (HANDOFF.md §7.3):** one spec row/file per figure.
This INDEX is the single "what's left" tracker — update the Status column as
work moves. Full annotation details: `../HANDOFF.md` §3/§4.

**Status legend**
| status | meaning |
|---|---|
| `done` | svg+png+generator committed to main; commit hash in Notes |
| `in-progress` | spec/artwork being worked |
| `blocked` | needs professor input (see Notes) |
| `open` | queued — redraw/correct task assigned by annotation |
| `scan` | insert original/photo/rescan — NOT a redraw |
| `—` | no annotation yet (queued behind annotated items) |

---

## Ch.1 — Introduction
| Fig | Title | Task | Status | Notes |
|---|---|---|---|---|
| 1.1 | Three phase diagram of soils (Ishibashi & Hazarika 2015) | redraw + color | open | |
| 1.2 | Compaction curve | redraw / approx OK | open | |
| 1.3 | Compaction curve and zero air void curve | redraw | open | |
| 1.4 | Difference between compaction and consolidation | standardize | open | |
| 1.5 | e-logσ curve | consult manu & pretty up | open | |
| 1.6 | Settlement computation model | redraw | open | |
| 1.7 | Shear strength of a soil mass | redraw | open | |
| 1.8 | Failure strength criteria for soils | — | — | highlighted in docx |
| 1.9 | Terzaghi's bearing capacity model | consult manu & redraw | open | |
| 1.10 | Model diagram of soil strength increasing mechanism (Ingles & Metcalf 1972) | — | — | |
| 1.11 | Increasing soil strength by consolidation | — | — | |
| 1.12 | Change of soil strength by densification | standardize labeling | open | |
| 1.13 | Change of soil strength by solidification | standardize labeling | open | |
| 1.14 | Change of soil strength by reinforcement | reconstruct (b) | done | `3a730e2`; spec: see HANDOFF §6; regen 2026-08-17 (v3, subscript-glyph + layout fixes) |
| 1.15 | Leaning Tower of Pisa, Italy | photo | scan | "send photo in" |
| 1.16 | Kansai international airport | — | — | highlighted |
| 1.17 | Tilted buildings during Niigata earthquake | — | — | highlighted |
| 1.18 | Damaged residential house, 2011 Tohoku liquefaction | — | — | highlighted |

## Ch.2 — Compaction / vibro-flotation / tamping (non-cohesive)
| Fig | Title | Task | Status | Notes |
|---|---|---|---|---|
| 2.1 | Compaction curve and Engineering Properties | — | — | |
| 2.2 | Governing Factors in Soil Compaction | — | — | |
| 2.3 | Compaction Curve vs. Compaction Energy | — | — | |
| 2.4 | Range of field water content | — | — | |
| 2.5 | Field compaction equipments (I 2010) | insert original | scan | （オリジナルを入れる） |
| 2.6 | Effect of field compaction w/ depth & passes (D'Appolonia 1969) | insert original | scan | （オリジナルを入れる） |
| 2.7 | Work Flow of Compaction Method | — | — | |
| 2.8 | Loose sand and Vibration | redraw | done | `912f378`; spec: `fig-2.8-loose-sand-vibration.md`; regen 2026-08-17 (v3, badge titles + density fix) |
| 2.9 | Grain size distribution curve & Vibro-flotation range | source/citation or redraw | blocked | confirm source with professor first; also fix typos (Effctof, achive) |
| 2.10 | Procedure of Vibro-flotation method | — | open | |
| 2.11 | Renewal work for pier by Vibro-flotation | — | — | |
| 2.12 | Soil structure change during Tamping (Wood 1968) | — | — | |
| 2.13 | System and procedure of Heavy Tamping | — | open | |
| 2.14 | Ground behavior by Heavy Tamping passes (Yamada 1991) | fix W / Hw notation | blocked | 本文含めW/Hwの定義確認 |
| 2.15 | Planning and Designing | confirm Weight vs Mass | blocked | 本文含めて定義の確認 |
| 2.16 | Procedure flow of Heavy Tamping | — | — | |

## Ch.3 — Preloading / drains (cohesive soils)
| Fig | Title | Task | Status | Notes |
|---|---|---|---|---|
| 3.1 | Road embankment by Replacement method | — | — | Nishida & Nakazawa 1991 |
| 3.2 | Breakwater foundation by Replacement method | — | — | |
| 3.3 | Replacement by Light-weight materials | — | — | |
| 3.4 | Replacement by surcharging and squeezing | — | — | |
| 3.5 | Under-fill Style | — | — | |
| 3.6 | Flow of Design for Replacement method | — | — | |
| 3.7 | Foundation of Gentle sloping revetment bank | — | — | Horiuchi et al. 2008 |
| 3.8 | Consolidation curve of Preloading method | insert original | scan | （オリジナルを入れる） |
| 3.9 | Preloading by embankment | — | — | |
| 3.10 | Sand Drain Method | — | open | in-text labels: Permeable sand layer / Soft clayey soil / Sand drains / Water flow / Sand mat / Embankment as surcharge |
| 3.11 | Vacuum Consolidation Method | — | open | in-text labels: Vacuum pump / Air & Water / Sand mat with drain pipes / Airtight membrane / Vertical drainage materials |
| 3.12 | Principle of vertical drain method | insert original | scan | （オリジナルを入れる） |
| 3.13 | Wick drain | insert original | scan | （オリジナルを入れる） |
| 3.14 | Procedures of Sand Drain Method with Casing Pipe | minor corrections | done | `bd7b9e9`; 7-panel procedure; regen 2026-08-17 (v3) |
| 3.15 | Prefabricated Typical Wick Drain (JGS 2006) | minor corrections | done | `124cc30`; cross-section table; regen 2026-08-17 (v3, fixed stray divider + label overlap) |
| 3.16 | Mandrel-type Machine for Wick Driving | redraw | done | `0d9582c`; regen 2026-08-17 (v3, ground-hatch clip fix) |
| 3.17 | Relationship of Th and U on Vertical Drain (Takagi 1955) | re-scan | scan | 図をもう一度スキャンする |
| 3.18 | Pattern of Sand Pile and Effective Distance | add reference | open | 参考文献：高木論文？ |
| 3.19 | Seawall Foundation and Soil Profiles of Kansai Int'l Airport | — | — | Furudoi & Kobayashi 2009, highlighted |

---

## Ch.4–7 (admixture / grouting / earth reinforcement)
Not yet analyzed. Source docx exist: `../GI BookA Manuscript 2022.2.2/` and
`../GI Book 2024 May/` (incl. `Harada san/` subfolder with SCP figures).

## Conventions reminder
- New spec files: copy `_TEMPLATE.md` → `fig-<n>-<slug>.md`.
- Committing a figure = commit generator + svg + png + spec together.
- After commit: set Status `done`, add commit hash, run
  `python scripts/qa_figure.py <fig>`.