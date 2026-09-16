# FIG_SPECS — live figure tracker & specs

**Registry convention (HANDOFF.md §7.3):** one spec row/file per figure.
This INDEX is the single "what's left" tracker — update the Status column as
work moves. Task assignment ground truth: **`ANNOTATION_AUDIT.md`** (extracted
2026-09-16 from the canonical `(Figs)` docx). Full pipeline: `../HANDOFF.md`.

**Status legend**
| status | meaning |
|---|---|
| `done` | svg+png+generator committed to main; commit hash in Notes |
| `in-progress` | spec/artwork being worked |
| `blocked` | needs professor input (see Notes) |
| `open` | queued — redraw/correct task assigned by annotation |
| `scan` | insert original/photo/rescan — NOT a redraw |
| `owner` | **real-data figure — Abinael draws by hand. Do NOT generate.** |
| `draft` | image-model redraw in `Abi'sFigures/` (by Abinael) — raster only, awaiting professor review |
| `not-ours` | assigned to Hazarika / Nakazawa / Harada, or traced elsewhere |
| `—` | no annotation — not an assigned task |

> **Illustrative vs data.** Schematics (`open`) may be produced with image
> generation. Figures plotting measured or published data — N-value profiles,
> strength-vs-water-content curves, grain-size distributions — are marked
> `owner`: a generative model invents plausible-but-wrong curves, so these are
> drawn by hand from the source. Never mix the two routes.

---

## Ch.1 — Introduction
Only **1.14** carries an annotation in either the '23.1.27 or '26.7.30 edition.
The "Task" column below preserves what the pre-audit tracker recorded, but for
1.1–1.13 that had **no basis in the professor's markup** (`ANNOTATION_AUDIT.md`
§4) — status is therefore `—` (unconfirmed), not `open`.

| Fig | Title | Task (pre-audit note) | Status | Notes |
|---|---|---|---|---|
| 1.1 | Three phase diagram of soils (Ishibashi & Hazarika 2015) | redraw + color | — | no annotation; confirm before working |
| 1.2 | Compaction curve | redraw / approx OK | — | no annotation; confirm before working |
| 1.3 | Compaction curve and zero air void curve | redraw | — | no annotation; confirm before working |
| 1.4 | Difference between compaction and consolidation | standardize | — | no annotation; confirm before working |
| 1.5 | e-logσ curve | consult manu & pretty up | — | no annotation; confirm before working |
| 1.6 | Settlement computation model | redraw | — | no annotation; confirm before working |
| 1.7 | Shear strength of a soil mass | redraw | — | no annotation; confirm before working |
| 1.8 | Failure strength criteria for soils | — | — | caption highlight only |
| 1.9 | Terzaghi's bearing capacity model | consult manu & redraw | — | no annotation; confirm before working |
| 1.10 | Model diagram of soil strength increasing mechanism (Ingles & Metcalf 1972) | — | — | |
| 1.11 | Increasing soil strength by consolidation | — | — | |
| 1.12 | Change of soil strength by densification | standardize labeling | — | no annotation; confirm before working |
| 1.13 | Change of soil strength by solidification | standardize labeling | — | no annotation; confirm before working |
| 1.14 | Change of soil strength by reinforcement (Narain 1984) | reconstruct (b) | done | `3a730e2`; （ｂ）図を再構成する(学生アルバイト); regen 2026-08-17 (v3) |
| 1.15 | Leaning Tower of Pisa, Italy | photo | scan | "send photo in" |
| 1.16 | Kansai international airport | — | — | caption highlight only |
| 1.17 | Tilted buildings during Niigata earthquake | — | — | caption highlight only |
| 1.18 | Damaged residential house, 2011 Tohoku liquefaction | — | — | highlighted |

## Ch.2 — Compaction / vibro-flotation / tamping (non-cohesive)
| Fig | Title | Task | Status | Notes |
|---|---|---|---|---|
| 2.1 | Compaction curve and Engineering Properties (Lambe 1958, modified) | — | — | |
| 2.2 | Governing Factors in Soil Compaction | — | — | |
| 2.3 | Compaction Curve vs. Compaction Energy (I&H 2010) | insert original | scan | （オリジナルを入れる）— **was blank in pre-audit INDEX** |
| 2.4 | Range of field water content to achieve specified quality | — | — | typo in caption: "achive" |
| 2.5 | Field compaction equipments (I&H 2010) | insert original | scan | （オリジナルを入れる） |
| 2.6 | Effect of field compaction w/ depth & passes (D'Appolonia 1969) | insert original | scan | （オリジナルを入れる）; typo: "Effctof" |
| 2.7 | Work Flow of Compaction Method | — | — | |
| 2.8 | Loose sand and Vibration | redraw | done | `912f378`; 図を書き直す（学生アルバイト）; spec: `fig-2.8-loose-sand-vibration.md`; regen 2026-08-17 (v3) |
| 2.9 | Grain size distribution curve & Vibro-flotation range | source/citation | owner | data curve — confirm source first, do NOT fake data |
| 2.10 | Procedure of Vibro-flotation method | — | — | |
| 2.11 | Renewal work for pier by Vibro-flotation | — | — | |
| 2.12 | Soil structure change during Tamping (Wood 1968) | — | — | |
| 2.13 | Illustrated system and procedure of Heavy Tamping | fix W / w notation | blocked | （Wとwの修正）— notation decision |
| 2.14 | Ground behavior by Heavy Tamping passes (Yamada 1991) | — | — | |
| 2.15 | Planning and Designing | confirm Weight vs Mass | blocked | 本文も含めてWeightとMassの定義の確認 |
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
| 3.10 | Sand Drain Method | — | — | no annotation; in-text EN labels exist if ever needed |
| 3.11 | Vacuum Consolidation Method | — | — | no annotation; in-text EN labels exist if ever needed |
| 3.12 | Principle of vertical drain method | insert original | scan | （オリジナルを入れる） |
| 3.13 | Wick drain | insert original | scan | （オリジナルを入れる） |
| 3.14 | Procedures of Sand Drain Method with Casing Pipe | minor corrections | done | `bd7b9e9`; 若干修正（学生アルバイト）; regen 2026-08-17 (v3) |
| 3.15 | Prefabricated Typical Wick Drain (JGS 2006) | — | done | `124cc30` — **no annotation found**; built anyway, harmless |
| 3.16 | Mandrel-type Machine for Wick Driving | redraw | done + draft | `0d9582c` (v3 generator twin); **also** re-done as `Abi'sFigures/fig-3.16.png` — wheeled carrier per the sketch, leader lines on every label. On the 検討事項 要修正 list; professor to choose |
| 3.17 | Relationship of Th and U on Vertical Drain (Takagi 1955) | re-scan | scan | （図をもう一度スキャンする）学生アルバイト |
| 3.18 | Pattern of Sand Pile and Effective Distance | add reference | open | 参考文献を入れる：高木論文？ |
| 3.19 | Seawall Foundation & Soil Profiles, Kansai Int'l Airport | — | — | Furudoi & Kobayashi 2009, highlighted |

---

## Ch.4 — With admixture or inclusion (SCP / stone columns)
Source: `Chapter 4 with admixture or Inclusion(Figs)2023 Feb Shinsaibashi.docx`

| Fig | Title | Annotation | Task | Status |
|---|---|---|---|---|
| 4.4 | Relationship between quicklime amount and water content | 中澤先生からOriginalを送って貰う | — | not-ours |
| 4.9 | Principle of SCP (Fudo Construction, 1971) | （学生に書き直し） | redraw | draft → `Abi'sFigures/fig-4.9.png` |
| 4.12 | Designing chart of SCP method for sandy ground | 原田さんにお尋ね | — | not-ours |
| 4.14 | Mechanism of bearing capacity on composite ground | 中澤先生からOriginalを貰う | — | not-ours |
| 4.16 | Case history of SCP (JAFEC, 2016) | 原田さんにお尋ね／トレースしてください | trace | owner (case data) |
| 4.17 | Effect of stone column for settlement (Som & Das, 2004) | Originalからスキャンする | insert original | scan |
| 4.18 | Procedure of Stone Column Method (Civil Digital, 2017) | （書き直す：学生へ） | redraw | draft → `Abi'sFigures/fig-4.18.png` |
| 4.22 | Settlement reduction with stone columns (Greenwood & Thomson, 1984) | Originalを探す／トレースを依頼中のものと差し替える | — | not-ours — **trace already commissioned, see May 27 email** |
| 4.23 | Results of ground improvement by SPT N Values (Basarkar 2009) | (作り直す学生へお願い) | remake | owner (measured N-values) |

## Ch.5 — Grouting-type admixture / DMM
Source: `Chapter 5. with grouting type admixture ( Fig) 2023 Feb Shinsaibashi.docx`

| Fig | Title | Annotation | Task | Status |
|---|---|---|---|---|
| 5.1 | Grouting Type with Admixture | (Hatchingを入れる) | add hatching | draft → `Abi'sFigures/fig-5.1.png` |
| 5.5 | Compaction Grouting | （書き直す：学生へ） | redraw | draft → `Abi'sFigures/fig-5.5.png` |
| 5.6 | Procedure Types of Permeation Grouting | （直しました：もう少し改善が必要） | improve | **open** — original is EMF, no raster to trace |
| 5.9 | Relation of Soil Type, Injection Pattern and Grout (JGS 2009) | （スキャンをし直し：学生へ） | re-scan | scan |
| 5.13 | Triple Pipe system (JAFEC, 2014) | Fig.5.14を挿入すること？ | — | blocked (question to professor) |
| 5.16 | Unconfined compressive strength vs. Total water content | （書き直す；学生へ） | redraw | owner (data plot) |
| 5.17 | Example of Mixing shaft | 検討事項 要修正 | — | blocked (scope unclear) |
| 5.18 | Construction Procedure of DMM | (イメージを書く直す：学生へ) | redraw | draft → `Abi'sFigures/fig-5.18.png` |
| 5.20 | Typical applications of DMM | （書く直す：学生へ） | redraw | **open** — original is EMF, no raster to trace |

## Ch.6 — Earth reinforcement
Source: `Chapter 6 Earth Reinforcement (Fig).docx`. The professor supplied
**JA→EN glossaries inline** for 6.1, 6.2, 6.13 — the wordlist is already in the
docx, so these are redraw-with-English-labels jobs.

| Fig | Title | Annotation | Task | Status |
|---|---|---|---|---|
| 6.1 | Geotechnical categories for ground improvement (JGS, 2009) | JA→EN glossary supplied | redraw EN labels | draft → `Abi'sFigures/fig-6.1.png` |
| 6.2 | Earth reinforcement vs. soil improvement (JGS, 2009) | JA→EN glossary supplied | redraw EN labels | draft → `Abi'sFigures/fig-6.2.png` |
| 6.4 / 6.5 | Pseudo cohesion / Ziegler (2018) | タイトルをつける | add title | open (text only) |
| 6.13 | EPS | JA→EN glossary supplied | redraw EN labels | draft → `Abi'sFigures/fig-6.13.png` |
| 6.14 | Tire derived Geo-materials | 図の変更（ハザリカ） | — | not-ours |

## Ch.7 — Others (electro-osmosis / ground freezing)
Source: `Chapter 7. Others (Figs).docx`. Meeting notes '22.2.11 §1: *付図は原本
からのコピーをそのまま掲載している…特に Fig.7.6〜7.9 は図中の説明が日本語のままに
なっているので修正する。ハザリカ担当でハザリカ研の学生に作成させる* — **7.6–7.9
still carry Japanese in-figure text and are assigned to the lab student.**

| Fig | Title | Annotation | Task | Status |
|---|---|---|---|---|
| 7.6 | Growth Process of Frozen Wall (JGS, 2013) | JA→EN glossary supplied | redraw EN labels | draft → `Abi'sFigures/fig-7.6.png` |
| 7.7 | Unconfined compression strength vs. freezing temperature | JA→EN glossary supplied | redraw EN labels | owner (data: Toyoura sand / Fujinomori clay curves) |
| 7.8 | Brine System (Oguro, 2017) | JA→EN glossary supplied | redraw EN labels | draft → `Abi'sFigures/fig-7.8.png` |
| 7.9 | Liquefied Gas System | 別の図に入れ替えること！ | replace figure entirely | blocked (needs a new source figure) |

---

## Summary of open work
- **Drafted, awaiting professor (11):** 3.16, 4.9, 4.18, 5.1, 5.5, 5.18, 6.1,
  6.2, 6.13, 7.6, 7.8 — raster redraws in `../Abi'sFigures/` (by Abinael),
  provenance in its MANIFEST. 3.16 also still has its v3 generator twin.
- **Schematic, still open (2):** 5.6, 5.20 — originals are EMF; no raster to trace
- **Owner-only, real data (5):** 2.9, 4.16, 4.23, 5.16, 7.7
- **Scan / insert original (9):** 2.3, 2.5, 2.6, 3.8, 3.12, 3.13, 3.17, 4.17, 5.9
- **Text-only edits (3):** 3.18 (add citation), 6.4, 6.5 (add title)
- **Blocked on professor (5):** 2.13, 2.15, 5.13, 5.17, 7.9
- **Done (5):** 1.14, 2.8, 3.14, 3.15, 3.16

## Conventions reminder
- New spec files: copy `_TEMPLATE.md` → `fig-<n>-<slug>.md`.
- Committing a figure = commit generator + svg + png + spec together.
- After commit: set Status `done`, add commit hash, run
  `python3 scripts/qa_figure.py <fig>`.
