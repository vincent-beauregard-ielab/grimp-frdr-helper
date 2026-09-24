# Quality Control Report — RogersPass_2025-2026

Step 4 of the GRIMP FRDR deposit workflow. This report is an **issue list only**; it does not
duplicate the file inventory or deposit-scope summary already in `artifacts/data_exploration.md`.
Documentation-coverage reconciliation between `research.md` and `data_exploration.md` was already
completed before this step (BHG glossary/citation patch) and is not repeated here.

Every issue below was independently verified against the raw files in `raw_data/` (not copied from
`data_exploration.md`'s own discrepancy list) using `openpyxl`/`pandas` inspection scripts run against
this dataset's `.venv`. Cross-references to `data_exploration.md`'s "Summary of discrepancies" (items
1–11) are noted where relevant so Data Preparation doesn't re-discover them, but this report's own
numbering is independent and organized by severity.

**Correction to the file inventory:** `data_exploration.md` states 15 stratigraphy workbooks. The
actual count is **14** (18 non-template `.xlsx` files in the day folders, minus the 4 spatial/linkage
workbooks `Spatial_Round_Hill.xlsx`, `JimBay_Spatial.xlsx`, `20260309_HermitMeadow_Spatial.xlsx`,
`20260310_RoundHill_Spatial.xlsx`). All findings below that reference "all stratigraphy workbooks"
were checked against these 14 real files, confirmed via `find raw_data -iname "*.xlsx"` (19 total: 14
stratigraphy + 4 spatial + 1 `templates/StratiTemplate.xlsx`). Data Preparation should use 14, not 15,
in any file-count statements.

---

## A. Critical — data integrity (silent corruption / broken linkage risk)

### A1. `GopherButte_2026-03-04.xlsx` Stability Tests sheet is a byte-for-byte copy of `RoundHill.xlsx`'s (Day1)

**What.** `Day2_Fidelity_RH_04-03-2026/GopherButte_2026-03-04.xlsx`, sheet `Stability Tests`, all 8
populated data rows (A2:E9) are cell-for-cell identical to `Day1_RoundHill_03-03-2026/RoundHill.xlsx`,
sheet `Stability Tests`, rows A2:E9 — same Test/Score/Facture-Char/Down sequence in the same order
(`ct/M13/rp/10`, `ct/h21/rp/13`, `CT/H24/sp/51`, `ct/H27/sc/118`, `Ect/N23/–/20`, `ECT/N29/–/31`,
`CT/M20/RP/31`, `CT/H27/RP/62`). These are two different sites (Round Hill vs. Gopher Butte) on two
different days (2026-03-03 vs. 2026-03-04); identical compression-test results in identical order
across both is not physically plausible and indicates the sheet was copy-pasted from the Day1
workbook and never updated with Gopher Butte's actual test results. (This file's `AVY profile` LOCATION
field, B4, does correctly read "Gopher Butte" — only the Stability Tests sheet appears carried over.)

**Impact.** If retained as-is, this dataset would silently misrepresent Gopher Butte's snow stability
as identical to Round Hill's — a serious scientific-integrity problem for any avalanche-hazard reuse
of this file, not merely a formatting nuisance.

**Recommended action.** Flag for researcher: confirm whether real Gopher Butte stability-test data
exists (paper fieldbook, per `Write in the Rain - table of content.docx`) and can be transcribed, or
whether the Stability Tests sheet must be marked "not recorded" / excluded for this file in Data
Preparation and `DATA_PREPARATION.md`.

### A2. `dku` radar linkage table unusable in two workbooks — referenced counters exist nowhere in the dataset

**What.** Both `Day1_RoundHill_03-03-2026/RoundHill.xlsx` (sheet `dku`) and
`Day2_Fidelity_RH_04-03-2026/RoundHill_bottom.xlsx` (sheet `dku`) list the identical angle→file-number
mapping, counters **780–789** (Angle 0–50° in 5° steps, with counter 789 duplicated for angles 0°, 45°,
and 50°). No file with counter 780–789 exists anywhere in `raw_data/` (verified by directory listing).
The real `dku` files for these two profiles are `Day1.../dku/0790_..._RHFP_...` through `0818_...`
(Day1, site code RHFP) and `Day2.../dku/0819_...` through `0832_...` (Day2) — two entirely different,
non-overlapping counter ranges, neither of which is 780–789. The fact that both files (different days,
different real file ranges) contain the exact same wrong 780–789 block strongly suggests unedited
template/placeholder content rather than a simple transcription slip in either file individually.

**Impact.** The pit-to-radar-angle linkage for these two profiles is completely non-functional as
recorded — anyone using the workbook to find "which `dku` file corresponds to which stratigraphy
depth/angle" for these two pits will look up nonexistent files. Downstream radar-stratigraphy
validation (the dataset's core scientific purpose per `research.md`) cannot use these two linkage
tables as-is.

**Recommended action.** Flag for researcher: the true angle→counter mapping for Day1's RoundHill full
profile is very likely 790–799 (10 higher than recorded) based on file-count and angle-order alignment,
and for Day2's RoundHill_bottom likely within 819–828 — but this is Data Preparation's/researcher's
inference to confirm against field notes, not an automatic fix. Document as a known linkage gap in
`DATA_PREPARATION.md` regardless of resolution.

### A3. `2026-03-09_Hermit_SurfacePit2_StratiTemplate.xlsx` contains no recorded data in any sheet

**What.** `DAY7_HermitMeadows_20260309/2026-03-09_Hermit_SurfacePit2_StratiTemplate.xlsx` — all 9
sheets (`AVY profile`, `Stability Tests`, `Density`, `IRIS`, `smp`, `Dual KU`, `Radar K`, `SS`, `BHG`)
contain only the template's column headers/labels and zero filled observation rows. The `AVY profile`
sheet's 29 non-empty cells match the blank `templates/StratiTemplate.xlsx` exactly, cell-for-cell. Its
sibling file in the same folder, `..._SurfacePit1_StratiTemplate.xlsx`, does contain real data (date,
elevation, aspect, stratigraphy rows with compression-test comments). Both files retain the literal
`StratiTemplate` suffix in their filename, unlike every other stratigraphy workbook in the deposit.

**Impact.** `data_exploration.md` §1's per-day table counts DAY7 as having "2 surface profiles"; only
one (Pit1) actually contains data. If "2 surface profiles" is repeated in `DATA_PREPARATION.md`'s file
inventory or the README without correction, it overstates DAY7's coverage.

**Recommended action.** Exclude `SurfacePit2` from the deposit's stratigraphy-workbook count (document
as an empty/never-completed pit in `DATA_PREPARATION.md`), unless the researcher confirms the data
exists elsewhere (e.g. only recorded in the paper fieldbook) and should be transcribed in before
deposit.

### A4. SMP file-linkage entries reference `.pnt` counters absent from disk

**What.**
- `Day2_Fidelity_RH_04-03-2026/FidelityStation_2023-03-04.xlsx`, sheet `smp`: references counter
  **756**. Day2's `smp/` folder on disk contains only 758–763 (6 files); 756 (and 757) do not exist.
- `DAY4_JimBay-RoundHill-GopherButte_20260306/JimBayFullProfile.xlsx`, sheet `smp`: references
  counters **773** and **774**. DAY4's `smp/` folder on disk contains only 776–792 (16 files); 773–775
  do not exist.

**Impact.** Two of the deposit's pit-to-SMP-file linkages point to files that were never captured (or
were captured but not delivered in `raw_data/`). A reuser following the linkage table will get a
file-not-found for these specific depth markers.

**Recommended action.** Document as a known gap per pit in `DATA_PREPARATION.md` (do not silently drop
the linkage row). Ask researcher whether 756 and 773/774 exist under a different counter or were lost.

### A5. Off-by-one gaps at the start of two other `dku`/`Dual KU` linkage series

**What.**
- `Day2_Fidelity_RH_04-03-2026/FidelityStation_2023-03-04.xlsx`, sheet `dku`: references 818–828; disk
  has 819–832 (818 missing).
- `DAY4_JimBay-RoundHill-GopherButte_20260306/JimBayFullProfile.xlsx`, sheet `Dual KU`: references
  832–843; disk has 833–862 (832 missing).

**Impact.** Minor compared to A2/A4, but the pattern (linkage table's first counter = one below the
first file actually on disk) recurs across two independent files, suggesting a systematic off-by-one
in how the "starting" counter is recorded at profile setup, not two unrelated typos.

**Recommended action.** Document as known gaps; low priority to chase down but worth asking the field
team about the recording convention (does the linkage table record the counter *before* the sweep
starts, off by one from the first actual angle file?).

---

## B. High — structural inconsistency (breaks naive multi-file parsing)

### B1. `GopherButte_2026-03-04.xlsx` `AVY profile` sheet has a different column layout than the other 13 stratigraphy workbooks

**What.** Row 5 (column headers) for `Day2_Fidelity_RH_04-03-2026/GopherButte_2026-03-04.xlsx`,
`AVY profile` sheet, columns C–G reads `BHG, FORM, Ѳ (LWC), IRIS Depth, Irish Value` instead of the
template's (and every other file's) `FORM, EXTENT, Ѳ (LWC), WEIGHT, DENSITY`. This is the **only** one
of the 14 stratigraphy workbooks with this layout (verified by dumping row 5 of all 14 — the other 13,
including the two `StratiTemplate`-suffixed DAY7 files, match the template exactly). Concretely: a BHG
hardness column is inserted at column C (this file has no separate `BHG` sheet, unlike its siblings —
the BHG data was recorded inline instead), the `EXTENT` column is dropped entirely, and `WEIGHT`/
`DENSITY` are replaced with IRIS depth/value readings recorded inline instead of in the `IRIS` sheet.
"Irish Value" (G5) is also a typo for "IRIS Value."

**Impact.** `data_exploration.md` describes this loosely as "a few header cells shift by one column
between files" (plural, unquantified). The precise picture is: only 1 of 14 files is affected, and it
is not a 1-column shift but a full 4-column reinterpretation (insert/drop/replace). Any script that
concatenates all 14 `AVY profile` sheets by column position (rather than by header name) will silently
write this file's BHG readings into the shared "FORM" column and its inline IRIS readings into the
shared "WEIGHT"/"DENSITY" columns.

**Recommended action.** Data Preparation must parse `AVY profile` sheets by header name, not fixed
column index, or must special-case this file. Fix the "Irish Value" typo to "IRIS Value" when
transcribing/documenting.

### B2. `GopherButte_upperSnowpack.xlsx` internal LOCATION field says "Fidelity", not "Gopher Butte"

**What.** `DAY4_JimBay-RoundHill-GopherButte_20260306/GopherButte_upperSnowpack.xlsx`, `AVY profile`
sheet, cell B4 (LOCATION) reads `"Fidelity"`. This is a different file from A1's
`GopherButte_2026-03-04.xlsx` (Day2), whose LOCATION field correctly reads "Gopher Butte" — so the two
Gopher-Butte-named files have opposite label problems (one has the wrong site name, the other has a
copy-pasted data sheet under the right site name).

**Impact.** A per-file "site" field derived from internal metadata (rather than filename/folder) would
misassign this file's profile to Fidelity.

**Recommended action.** Flag for researcher: confirm this file's true site (filename, day-folder name,
and every other cross-reference say Gopher Butte) and correct the LOCATION cell's provenance note in
`DATA_PREPARATION.md`; do not trust the internal LOCATION field over the filename for this one file.

### B3. IRIS "Field Notes" cells contain the blank template's boilerplate text, verbatim, in 12 of 14 workbooks

**What.** `templates/StratiTemplate.xlsx`'s `IRIS` sheet has three pre-filled French free-text cells
at P5, P8, P10: `"Calib 2 : « encore à 40 » pour 40"`, `"H=260 : 4 mesures"`, `"H=220 : 4 mesures"`
(exact characters, including the same non-breaking-space Unicode sequences). The identical text, at
the identical cell coordinates, appears in 12 of the 14 real stratigraphy workbooks' `IRIS` sheets
(all except `Day2/FidelityStation_2023-03-04.xlsx`, which has different text at P5 and nothing at
P8/P10, and DAY8's file, which keeps the same text but has genuinely different Calibration
Voltage/Scan numbers). The numeric IRIS columns (Calibration Voltage, Scan, Height) themselves *are*
genuinely distinct per file — this issue is confined to the free-text Field Notes cells.

**Impact.** These three cells read as if they were day-specific field observations, but they are
unedited template instructions/reminders (a note about the calibration-panel-2 procedure and a
reminder to take 4 measurements at H=260 cm and H=220 cm) that were never replaced. A reuser reading
"Field Notes" for a specific file would be misled into thinking this text describes something that
happened during that file's specific IRIS session.

**Recommended action.** Document as template boilerplate, not genuine field notes, in
`DATA_PREPARATION.md`; consider excluding or clearly re-labeling these 3 cells (not the rest of the
IRIS sheet) during Data Preparation.

### B4. `dku` radar files contain 50 repeated chirp blocks per file, not a single waveform

**What.** Sampled file `Day1_RoundHill_03-03-2026/dku/0790_13GHz_RHFP_00_V_00deg.txt` (51,437 lines):
1 `# === Measurement Header ===` block followed by exactly 50 repeated `# Chirp Number:` /
`# --- End of Chirp ---` sub-blocks, each containing its own `X, I, Q, Q2`-style IQ sample rows.
`data_exploration.md` §3 notes the file is large ("~51k lines observed") but does not characterize
this internal repeated-block structure.

**Impact.** A parser that reads the body as one continuous waveform table (as the "CSV block" framing
in `data_exploration.md` might suggest for `ka`/`Radar_K`) will concatenate 50 independent chirp
sweeps into one nonsensical series instead of 50 separate range profiles.

**Recommended action.** Document explicitly in `DATA_PREPARATION.md`/README's data-specific
information: each `dku` file = 1 measurement header + 50 chirp repetitions, each chirp block delimited
by its own `# Chirp Number:` / `# --- End of Chirp ---` markers.

---

## C. Medium — codebook / controlled-vocabulary inconsistency

Applies to the 14 stratigraphy workbooks' `Stability Tests` and `AVY profile` sheets. None of these
individually block parsing (case-insensitive/fuzzy matching handles most), but a codebook in
`DATA_PREPARATION.md` should document the canonical set and note these variants exist in the raw data.

### C1. Compression-test `Test` column — case inconsistency

`CT` (50 occurrences, 10 files) / `ECT` (17, 7 files) vs. lowercase `ct` (11, in 3 files:
`RoundHill.xlsx`, `GopherButte_2026-03-04.xlsx`, `20260309_HermitMedow.xlsx`) / `Ect` (2, in 2 files:
`RoundHill.xlsx`, `GopherButte_2026-03-04.xlsx`). **Recommended action:** normalize to uppercase in
Data Preparation; document both forms as equivalent.

### C2. Stability Tests `Score` column — mixed formats within the same column

Most rows use a clean fracture-quality-letter + tap-count code (e.g. `H21`, `M12`, `N23`, `E1`,
`ECTN15`). But several rows embed the *entire* compression-test result as one string instead of
splitting it across the sheet's own Test/Score/Facture-Char columns — e.g.
`2026-03-09_Hermit_SurfacePit1_StratiTemplate.xlsx` rows 2–7: Score cells read `'CTE8 (PC)'`,
`'CTM13 (RP)'` (×2), `'CTM14 (RP)'` (×3) — Test type, tap count, and fracture character all concatenated
into the Score cell, leaving the sheet's own Test/Facture Char columns blank for those rows. Also
present: lowercase variants (`e1`, `e9`, `h21`, `h26`, `m11`, all in `20260309_HermitMedow.xlsx`) and
bare tap-counts with no fracture-quality letter (`12.0`, `23.0` in
`Day1_RoundHill_03-03-2026/uppersnowpackstability.xlsx`, rows 5–6). **Recommended action:** flag for
researcher — the Pit1 rows in particular need the Score cell's embedded values split into the correct
columns before any cross-file Score comparison is meaningful.

### C3. `Facture Char.` column — numeric "Down (cm)" values leaking into the fracture-character column

Expected codes (`SC`, `RP`, `BRK`/`brk`, `SP`, `PC`, `N`) co-occur with plain numeric values (`31.0`,
`10.0`, `13.0`, `51.0`, `118.0`, `20.0`, `62.0` — all in `RoundHill.xlsx` and its copy
`GopherButte_2026-03-04.xlsx`, see A1) and `d`-prefixed values (`d24`, `d28`, `d48`, `d59`, all in
`20260309_HermitMedow.xlsx`) that look like depth/"Down (cm)" values shifted one column right from
their proper `Down` column. Also a lowercase/uppercase split: `brk` (2, `JimBayFullProfile.xlsx` and
`20260309_HermitMedow.xlsx`) vs. `BRK` (7, other files). **Recommended action:** flag for researcher —
verify whether `Down` and `Facture Char.` are transposed for the affected rows before using either
column downstream.

### C4. Hand-hardness (`RESISTANCE`) column — case and notation inconsistency

Standard codes `F`/`4F`/`1F`/`P`/`K` (with `+`/`-` modifiers) dominate, but: lowercase `p` (3×, all in
`Day1_RoundHill_03-03-2026/uppersnowpackstability.xlsx`) and `4f` (1×, same file); likely capital-I/
digit-1 typos `IF` and `IF+` (1× each, in `uppersnowpackstability.xlsx` row 13 and `RoundHill.xlsx` row
22 respectively — ICSSG has no "IF" hardness code, only `1F`); compound/range notations `F/1F`
(`GopherButte_upperSnowpack.xlsx` row 12), `4F to 1F` (`..._SurfacePit1...` row 14), `4F -> 1F`
(`GopherButte_2026-03-04.xlsx` row 14); and an unexplained `1K` (`JimBayFullProfile.xlsx` row 34, not a
standard code). **Recommended action:** document as observer shorthand for a hardness transition within
one layer (plausible field practice) vs. genuine typo — flag `IF`/`IF+` specifically for researcher
confirmation since ICSSG defines no such code.

### C5. Grain-form/type (`FORM`) column — spelling and case variants

`Fc` (1×, `RoundHill.xlsx` row 22) vs. standard `FC` (13×, 3 other files) — case variant of the same
code. `MF-CR` (1×, `FidelityStation_2023-03-04.xlsx` row 24) vs. standard `MFcr` (8× elsewhere) —
hyphenated variant spelling of melt-freeze crust. `RG-DF` (2×, `20260309_HermitMedow.xlsx`) vs.
`DF - RG` (1×, `JimBayFullProfile.xlsx` row 12) — same two-code combination in reverse order with
different spacing/hyphenation; could be a genuine stratigraphic transition (order matters) rather than
a typo — flag rather than auto-normalize. `Ice` (1×, `20260305_RogersPass.xlsx` row 34) — not a
standard ICSSG code (ICSSG's ice-layer code is `IF`). **Recommended action:** normalize case (`Fc`→`FC`,
`MF-CR`→`MFcr`); flag `Ice` and the `RG-DF`/`DF - RG` ordering for researcher confirmation rather than
auto-normalizing, since intent is ambiguous.

*(Note: the earlier `GopherButte_2026-03-04.xlsx` FORM-column anomalies — numeric-looking values like
`1.0`, `0.6`, `-` — are not a separate grain-form issue; they are a direct consequence of B1's column
shift, where column C in that file is actually the BHG hardness column, not FORM. No action beyond B1.)*

---

## D. Medium — naming and date-formatting consistency

### D1. Site-name spelling: "Hermit Meadows" has three different internal spellings

Folder name: `DAY7_HermitMeadows_20260309` (plural, no space). README/data_exploration.md prose:
"Hermit Meadows" (plural, spaced). Internal `AVY profile` LOCATION field:
`2026-03-09_Hermit_SurfacePit1_StratiTemplate.xlsx` → `"Hermit Meadow"` (singular);
`20260309_HermitMedow.xlsx` → `"Hermit Medow"` (singular **and** misspelled — missing the "a"). The
misspelled filename (`HermitMedow`) also propagates the typo into the file's own name, not just its
internal field. **Impact:** a site-name join/group-by across files using internal LOCATION text would
split Hermit Meadows data into two or three different "sites." **Recommended action:** normalize to
"Hermit Meadows" in any derived/processed dataset; document original spellings in
`DATA_PREPARATION.md`'s transformation record.

### D2. "Jim Bay" family has at least four spellings, likely not one typo but four different naming systems

`JIM_BAY_TRANSECT.kml` (all-caps, underscored — GPS export naming), `JimBayFullProfile.xlsx` /
`JimBay_Spatial.xlsx` / `JimBay_FullProfile` (Snowscope subfolder) (camelCase, no space), `JimBayCorner`
(IRIS/Snowscope subfolder names, adds "Corner"), and README/`research.md` prose "Jim Bay" (spaced, no
"Corner"). Distinct again from the `dku` radar filename site codes `JBFP`/`JBTR` (4-letter abbreviation
scheme). **Impact:** low risk of data corruption (these are different systems' native naming
conventions, not random typos within one system), but reuse documentation should state clearly that
"Jim Bay" == "JimBay" == "Jim Bay Corner" == `JBFP`/`JBTR` are the same site. **Recommended action:**
document the canonical name and all variant spellings/abbreviations in `DATA_PREPARATION.md`; no data
fix needed.

### D3. Date-format inconsistency across day-folder names, and within one day folder's own filenames

Day1–Day2–DAY3 folders use `DD-MM-YYYY` with dashes (e.g. `Day1_RoundHill_03-03-2026`); DAY4–DAY8
folders use compact `YYYYMMDD` (e.g. `DAY4_JimBay-RoundHill-GopherButte_20260306`). Within
`DAY7_HermitMeadows_20260309/` itself, sibling stratigraphy files mix both conventions on the same day:
`2026-03-09_Hermit_SurfacePit1_StratiTemplate.xlsx` (dashed `YYYY-MM-DD` prefix) alongside
`20260309_HermitMedow.xlsx` (compact `YYYYMMDD` prefix). **Impact:** any filename-based date parser
must handle both formats, including within a single folder. **Recommended action:** document both
formats in `DATA_PREPARATION.md`; no rename needed unless the researcher wants a normalized deposit
naming scheme (also affects `data_exploration.md` discrepancy #9's folder-naming recommendation).

### D4. `Radar_K` subfolder names are one calendar day ahead of their parent day-folder's date

`DAY7_HermitMeadows_20260309/Radar_K/` files sit inside a subfolder literally named `10_03_2026`
(10 March — one day *after* DAY7's actual 2026-03-09 collection date). `DAY8_Fidelity_20260310/Radar_K/`
files sit inside a subfolder named `11_03_2026` (11 March — one day after DAY8's actual 2026-03-10
date). This is distinct from the already-documented `ka`/`Radar_K` device-clock desync
(`data_exploration.md` discrepancy #4, which affects the file-internal Date field and reads
`2025-09-0x`) — this is the *subfolder name* itself, one day ahead in both cases it occurs (a
consistent +1 pattern, not random). **Impact:** compounds the existing device-clock problem — a reuser
who fixes the internal-timestamp issue by trusting folder names could still get the wrong date for
these two days' `Radar_K` files if they use the immediate subfolder name rather than the day-folder
name. **Recommended action:** document in the README/`DATA_PREPARATION.md` known-issues section
alongside the existing radar-clock note: rely on the top-level day-folder name only, not the `Radar_K`
subfolder name, for this instrument's collection date.

---

## E. Low — file-format / portability

### E1. IRIS log file extension casing (`.txt` vs `.TXT`) spans 9 subfolders across every data-bearing day

13 of the dataset's IRIS `.txt`/`.TXT` log files use uppercase `.TXT`, the remaining ~316 non-IRIS text
files (radar logs) use lowercase `.txt`. The uppercase files are not confined to one day/site — they
appear in IRIS subfolders under all 6 data-bearing days (`Day1`, `Day2`×3 subfolders, `DAY3`, `DAY4`×3
subfolders, `DAY7`, `DAY8`), confirmed by directory search (`data_exploration.md` §1 mentions this only
in passing for IRIS generally). **Impact.** FRDR deposit storage and most downstream tooling
(Python `glob`, shell scripts) are case-sensitive on Linux; a single hardcoded `*.txt` glob pattern in
a data-loading script would silently skip these 13 files, while the same script works fine on Windows
(case-insensitive filesystem) where this was authored. **Recommended action.** Either normalize all
IRIS log extensions to lowercase `.txt` during Data Preparation, or explicitly document the mixed
casing and require case-insensitive globbing (`*.[tT][xX][tT]` or `glob(..., case_sensitive=False)`) in
any provided loading code/notebook.

---

## Summary

| Severity | Count | Issues |
|---|---|---|
| Critical (A) | 5 | A1 copy-pasted Stability Tests, A2 unusable dku linkage (2 files), A3 empty Pit2 workbook, A4 broken SMP links, A5 off-by-one dku/Dual KU gaps |
| High (B) | 4 | B1 GopherButte column-shift, B2 wrong LOCATION field, B3 template boilerplate in IRIS notes, B4 undocumented 50-chirp repeat structure |
| Medium (C) | 5 | C1–C5 codebook/case inconsistencies (Test, Score, Facture Char., Resistance, Form) |
| Medium (D) | 4 | D1–D4 site-name and date-format inconsistencies |
| Low (E) | 1 | E1 IRIS `.TXT` extension casing |
| Documentation correction | 1 | Stratigraphy-workbook count is 14, not 15 (noted above, not counted as a data issue) |

**Total: 19 issues** (plus 1 documentation-accuracy correction to `data_exploration.md`'s file count,
noted at the top of this report but not itself a raw-data defect).

None of these issues require excluding entire instrument types from the deposit; all are addressable
in Data Preparation via documentation (`DATA_PREPARATION.md` known-issues/transformation record),
targeted researcher confirmation (as decision items in README once Step 6 drafts it), or light
normalization
(case/spelling) during file preparation. The two most consequential for scientific reuse are **A1**
(Gopher Butte's stability-test data may not be real) and **A2** (two pits' entire radar-angle linkage
tables point to nonexistent files) — both should be resolved with the researcher before Data
Preparation finalizes the deposit package.
