# Annotation audit — what the professor actually marked

Extracted 2026-09-16 from the **canonical** `(Figs)` docx via
`scripts/docx_annot.py` (highlight + red-text runs). This is the ground truth
for task assignment; `INDEX.md` predates it and disagrees in places (see §4).

Editions read: Ch1/Ch2 `'26.7.30 Ito Campus`, Ch3 `July 30 2026 Ito Campus`,
Ch4/Ch5 `2023 Feb Shinsaibashi`, Ch6 `(Fig)`, Ch7 `(Figs)`.

> Note: **cyan** highlight is applied to nearly every caption — it is caption
> styling, NOT a task marker. Task markers are the **red text** and
> **yellow-highlighted Japanese** parentheticals.

## 1. Assigned to the student worker (学生アルバイト / 学生へ)

| Fig | Annotation (verbatim) | Gloss | Task | Status |
|---|---|---|---|---|
| 1.14 | （ｂ）図を再構成する(学生アルバイト) | reconstruct panel (b) | reconstruct | done `3a730e2` |
| 2.8 | 図を書き直す（学生アルバイト） | redraw | redraw | done `912f378` |
| 3.14 | 若干修正（学生アルバイト） | minor corrections | minor corr. | done `bd7b9e9` |
| 3.16 | (図を書き直す；学生アルバイト) | redraw | redraw | done `0d9582c` |
| 3.17 | （図をもう一度スキャンする）学生アルバイト | re-scan | **scan** | open |
| 4.9  | （学生に書き直し） | student redraw | redraw | **open** |
| 4.16 | (原田さんにお尋ね) / トレースしてください。 | ask Harada-san; please trace | **trace** | open |
| 4.18 | （書き直す：学生へ） | redraw, to student | redraw | **open** |
| 4.23 | (作り直す学生へお願い) | remake, request to student | redraw | **open** |
| 5.1  | (Hatchingを入れる) | add hatching | edit | **open** |
| 5.5  | （書き直す：学生へ） | redraw, to student | redraw | **open** |
| 5.6  | （直しました：もう少し改善が必要） | fixed, needs more improvement | improve | **open** |
| 5.9  | （スキャンをし直し：学生へ） | re-scan, to student | **scan** | open |
| 5.16 | （書き直す；学生へ） | redraw, to student | redraw | **open** |
| 5.18 | (イメージを書く直す：学生へ) | redraw the image, to student | redraw | **open** |
| 5.20 | （書く直す：学生へ） | redraw, to student | redraw | **open** |

### Ch.6 / Ch.7 — Japanese labels to be replaced with English
Meeting notes (`Gi Book Aの打ち合わせ結果 '22.2.11`, §1): *"付図は原本からのコピーを
そのまま掲載しているので、修正する。特に、Fig.7.6～7.9は図中の説明が日本語のままに
なっているので、修正する。ハザリカ担当でハザリカ研の学生に作成させる"* — figures are
raw copies of originals; **Fig. 7.6–7.9 still carry Japanese in-figure text**;
Hazarika's lab student to remake them.

The professor supplied JA→EN glossaries inline for: **6.1, 6.2, 6.13, 7.6, 7.7,
7.8** — these are redraw-with-English-labels jobs, wordlist already given.
Also: 6.4/6.5 タイトルをつける (add title); 7.9 別の図に入れ替えること！ (replace with a
different figure entirely).

## 1a. Illustrative vs data — routing rule

Assigned figures divide into two routes that must never be mixed:

**Illustrative / schematic — may be produced with image generation:**
4.9, 4.18, 5.1, 5.5, 5.6, 5.18, 5.20, 6.1, 6.2, 6.13, 7.6, 7.8.
These are principle diagrams, procedure sequences, system layouts and
cross-sections. No measured quantity is being asserted, so a redrawn version
is judged on clarity alone.

**Real data — drawn by hand by the owner, NOT generated:**
2.9 (grain-size distribution curve), 4.16 (SCP case history), 4.23 (SPT
N-value results, Basarkar et al. 2009), 5.16 (unconfined compressive strength
vs. total water content), 7.7 (frozen-soil strength vs. freezing temperature,
Toyoura sand / Fujinomori clay).

> A generative model will produce a curve that looks right and is not the
> published data. For anything plotting measured values the figure must be
> traced or replotted from the source. These rows carry status `owner` in
> `INDEX.md`.


## 2. Insert original / re-scan — NEVER redraw
2.3, 2.5, 2.6 （オリジナルを入れる） · 3.8, 3.12, 3.13 （オリジナルを入れる） ·
3.17 re-scan · 4.17 (Engelhardt らの Original からスキャンする) · 5.9 re-scan.

## 3. Blocked / not the student's job
- 2.13 （Wとwの修正） and 2.15 (Weight vs Mass 定義の確認) — notation decisions.
- 4.4, 4.14 — 中澤先生から Original を送って貰う (Prof. Nakazawa supplies).
- 4.12 — （Originalについては、原田さんにお尋ね）(ask Harada-san).
- 4.22 — （Originalを探す）+ トレースを依頼中のものと差し替える (a trace is already
  commissioned elsewhere; see the May 27 email) → **do not duplicate this work.**
- 6.14 図の変更（ハザリカ）— Hazarika's own.
- `GI A検討事項 ('22.11.4)` adds a 要修正 ("needs fixing") list: 3.16, 4.17,
  4.22, 4.23, 5.16, 5.17, 5.18.

## 4. Where INDEX.md disagrees with the markup
- INDEX lists Ch.1 **1.1–1.9, 1.12, 1.13** as `open` redraws ("redraw + color",
  "standardize labeling"). **No such annotation exists** in either the '23.1.27
  or '26.7.30 Ch.1 edition — 1.14 is the only marked figure in Ch.1.
- INDEX lists **3.15** as "minor corrections". **No annotation on 3.15** in the
  2026 Ch.3 edition (3.14 carries the 若干修正 note, not 3.15).
- INDEX marks **2.3** as unannotated; it is in fact （オリジナルを入れる）.
- INDEX's Ch.4–7 row says "not yet analyzed" — §1 above now covers them.

Confirm 1.1–1.9 / 1.12 / 1.13 / 3.15 with the professor before spending effort
on them; they may be verbal asks not recorded in the docx, or may be stale.
