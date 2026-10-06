# Quality Control Report — rogers_pass_snow_profiles, period 2025-2026

Step 4 for version 2 (see `steps/extension.md`). Issue list only; inventory and formats are in `artifacts/2025-2026/data_exploration.md`. Every issue was verified on the raw files with `scripts/qc_checks_2025-2026.py` (read-only; run it to reproduce the evidence). Issues from the earlier exercise (commit 44e55ec) were re-checked, not copied; differences are noted.

This report is frozen after this step. Resolution tracking goes to `DATA_PREPARATION.md`.

---

## 0. Documentation-coverage reconciliation

| Check | Result |
|---|---|
| File types in exploration → method + reference in research | All covered: dual-Ku (IMST sensors, TSMM context), BHG (Borstad & McClung 2011), Emlid Reach RS2, K-band, IRIS, SMP, SnowScope, spatial workbooks, field readmes. |
| Instruments in research → files | Federal Sampler and drone: described in readmes, **no files** in `raw_data/2025-2026/`. Documented as ancillary data not included (not phantom instruments). |
| Variables → definition/unit | Patched in `research.md`: BHG unit (N, 0–50 N). Open: dual-Ku header fields (`Ramp *`, `Radar Cube`, `Processing`, `Range Window Function`, `Trigger Threshold`, range bins) — no public documentation, **ask researcher**. `RADAR HEIGHT` unit (dual-Ku sheet) — ask. `HS` assumed cm (values 282–344). |

---

## A. Critical — data integrity

### A1. `GopherButte_2026-03-04.xlsx` reuses Round Hill (Day 1) data in three sheets

**What.** The `Stability Tests` (8 rows), `Density` (63 rows) and `IRIS` (15 rows) sheets of `Day2_Fidelity_RH_04-03-2026/GopherButte_2026-03-04.xlsx` are cell-for-cell identical to those of `Day1_RoundHill_03-03-2026/RoundHill.xlsx`. Only `AVY profile` differs (LOCATION "Gopher Butte", 1930 m, observers MC, KH, JM). The earlier exercise found the Stability Tests copy only; Density and IRIS are new findings.
**Impact.** Two sites on two days would carry the same stability, density and SSA data. Any reuse for Gopher Butte would be wrong.
**Recommended action.** Researcher: confirm which Gopher Butte measurements were really taken on 2026-03-04 (readme: upper-snowpack observations by MC, KH, JM; field book pp. 3.3–3.4). In prepared copies, keep only the sheets with real Gopher Butte data; mark the copied sheets as "not recorded" and record the decision in `DATA_PREPARATION.md`.

### A2. BHG sheet identical in Hermit Meadows (03-09) and Round Hill upper snowpack (03-10)

**What.** The `BHG` sheet (27 rows: heights 0, 8, 16, 34 … with readings 0.5, 1.5, 2.15, 1.75 …) is identical in `DAY7_HermitMeadows_20260309/20260309_HermitMedow.xlsx` and `DAY8_Fidelity_20260310/20260310_Round Hill upper snowpackl.xlsx`. Other sheets differ. New finding.
**Impact.** Same as A1, for blade hardness.
**Recommended action.** Researcher: which workbook the BHG readings belong to (field book: Hermit Meadow pp. 1.21–1.24 vs Round Hill p. 1.26 onwards). Blank the BHG sheet in the other prepared copy.

### A3. Dual-Ku linkage tables point to counters that do not exist or are offset

**What.** Angle→counter tables vs files on disk:

| Workbook / sheet | Counters in table | Files on disk | Pattern |
|---|---|---|---|
| `RoundHill.xlsx` / `dku` (Day 1) | 780–789 | 790–800 (RHFP) | none exist; 11 angles mapped to 10 counters |
| `RoundHill_bottom.xlsx` / `dku` (Day 2) | 780–789 (same block) | 819–829 (FIFP) | copied block, none exist |
| `FidelityStation_2023-03-04.xlsx` / `dku` (Day 2) | 818–828 | 819–829 (FIFP) | off by one |
| `JimBayFullProfile.xlsx` / `Dual KU` (Day 4) | 832–843 | 833–844 (JBFP) | off by one |
| `JimBay_Spatial.xlsx` / Dual KU (Day 4) | 846–861 incl. 846, 860 | 847–862 (JBTR) | 846 and 860 absent |
| `20260310_RoundHill_Spatial.xlsx` / Dual KU (Day 8) | includes 862 | 863–880 (RHUT) | 862 is a Day 4 file |

Two full-profile tables are offset by exactly one: the table probably records the counter *before* the first sweep. Dual-Ku file names carry site, point and angle, so linkage can be rebuilt from file names without the tables.
**Impact.** The workbook tables cannot be used to find the radar file for an angle or transect point.
**Recommended action.** Do not edit the tables silently. Document that file names are authoritative for dual-Ku linkage. Researcher: confirm the off-by-one convention and whether `RoundHill.xlsx`/`RoundHill_bottom.xlsx` tables are placeholders. Optionally add a corrected linkage table to the prepared package, marked as derived.

### A4. 12 SMP files referenced in workbooks are missing from the raw data

**What.** SMP files on disk: 732–757 (Day 1), 758–763 (Day 2), 776–792 (Day 4, 784 missing). Counters **764–775 do not exist**, yet `20260305_RogersPass.xlsx` references 764–766 and `JimBayFullProfile.xlsx` references 773–774. Day 3 (Rogers Pass) has no SMP folder at all. Also: `RoundHill.xlsx` references 170 (probably 736, typo), `FidelityStation_2023-03-04.xlsx` references 756 (a Day 1 file), `JimBay_Spatial.xlsx` references 784 (absent).
**Impact.** The Rogers Pass and Jim Bay full-profile SMP measurements are missing from the deposit candidate, while the workbooks claim they exist.
**Recommended action.** Researcher: locate SMP files `S35M0764`–`S35M0775` and `S35M0784` (SMP memory card, another computer). If found, add them to `raw_data/2025-2026/` before Data Preparation. If not, document as missing.

### A5. Empty files

**What.** Seven 0-byte files: K-band `Day1/ka/03_03_2026/000020250903_1636.txt`, `000120250903_1637.txt`; dual-Ku `Day2/dku/0831_13GHz_FITO_01…`, `0831_17GHz_FITO_01…`, `0832_13GHz_FITO_02…`, `DAY4/dku/0862_13GHz_JBTR_15…`, `0862_17GHz_JBTR_15…`. Counter 832 has no 17 GHz file at all.
**Impact.** Users would find measurement files without data.
**Recommended action.** Exclude from the deposit and list them in `DATA_PREPARATION.md` (failed acquisitions). Fidelity tower dual-Ku (FITO) then has only counter 830 and the 13 GHz half of 832 left — check with researcher whether better copies exist.

---

## B. High — structural and metadata errors

### B1. Wrong date in `RoundHill_bottom.xlsx`

`AVY profile` DATE = 2026-04-03 in a Day 2 (2026-03-04) folder: day and month swapped. **Action:** document; correct in the prepared copy only if the researcher agrees (header value, not observation).

### B2. File name year `FidelityStation_2023-03-04.xlsx`

DATE inside is 2026-03-04. **Action:** rename in the prepared package following the v1 convention (`20260304_fidelity_stratigraphy.xlsx`).

### B3. `GopherButte_upperSnowpack.xlsx` LOCATION reads "Fidelity"

File name, day folder and readme say Gopher Butte (2026-03-06). **Action:** trust the file name; document the internal value; researcher to confirm.

### B4. `2026-03-09_Hermit_SurfacePit2_StratiTemplate.xlsx` is the SWE-only pit, with an empty header

All sheets equal the blank template except `Density`, which has an added `SWE (mm)` column with values every 10 cm (0–70 cm) and densities of 0. Matches the readme ("second surface pit to measure only SWE"). The earlier exercise reported this file as empty: corrected here. **Action:** keep; document as SWE-only; fill nothing in the header; researcher to confirm site and time.

### B5. `GopherButte_2026-03-04.xlsx` uses a different layer-table layout

`AVY profile` columns are `HEIGHT, RESISTANCE, BHG, FORM, Ѳ (LWC), IRIS Depth, Irish Value, …` instead of the standard `HEIGHT, RESISTANCE, FORM, EXTENT, Ѳ (LWC), WEIGHT, DENSITY, …` used in the 13 other workbooks and in v1. **Action:** document the layout in the README codebook; do not restructure.

### B6. Header fields shifted or missing

`RoundHill.xlsx` and `RoundHill_bottom.xlsx`: ELEVATION cell holds "SKY" (value missing, cells shifted). `20260310_Round Hill upper snowpackl.xlsx`: ELEVATION missing. `20260305_RogersPass.xlsx`: elevation and LOCATION missing. Dates are datetime cells in 8 workbooks and `YYYYMMDD` numbers in 5 (SurfacePit2 has none). **Action:** document; elevations available from GNSS or SnowScope for most sites.

### B7. Placeholder zeros in Density sheets

The density formula returns 0 where no weight was entered: 158 zeros across 8 workbooks (`RoundHill_bottom.xlsx` 39, `uppersnowpackstability.xlsx` 29, both Hermit surface pits 29 each, …). Real densities: 84–504 kg/m³ (n = 223). **Action:** document that 0 means "not measured"; consider blanking them in prepared copies (content transform, needs approval).

### B8. K-band radar clock and folder dates

All 141 K-band files have 2025-09-03/04 in file names and headers (clock not set). Day 7 and Day 8 subfolders are named `10_03_2026` and `11_03_2026`, one day after their day folders (2026-03-09, 2026-03-10). **Action:** document; derive dates from day folders; keep raw file names (they contain the instrument counter) unless the researcher prefers renaming with real dates.

### B9. SnowScope locations and empty reflectance column

7 profiles (Day 2: 3, Day 4: 4) have a stale phone location (51.4155, -117.0087, 806 m), 45 km from the sites. The third data column is unnamed and empty in all 89 files. **Action:** document both; do not alter values; list affected files.

### B10. Missing GNSS

Day 1 KMZ: 17 of 19 points without height. Rogers Pass profile (Day 3): no GNSS. Two SMP files without GPS fix (`S35M0736`, `S35M0782`). Only Day 7 has the full Emlid CSV; other days are KML/KMZ only. **Action:** document; ask whether Emlid CSV exports exist for other days (same format as v1).

---

## C. Medium — codebook and vocabulary

### C1. Stability test codes — case and format

`Test`: `CT` 50, `ct` 11, `ECT` 17, `Ect` 2 (v1: `CT`, `ECT` only). `Score`: standard codes (`M13`, `H27`, `E1`, `N23`…) mixed with lowercase (`h21`, `e1`, `m11`), bare numbers (`12.0`, `23.0`) and combined forms (`CTM13 (RP)`, `ECTN15`). **Action:** document; optionally normalize case in prepared copies (approval needed).

### C2. `Down` and `Facture Char.` columns swapped in some rows

In the A1 block (`RoundHill.xlsx`, `GopherButte_2026-03-04.xlsx`) fracture characters (`rp`, `sp`, `sc`) sit in the `Down` column and depths (10–118) in `Facture Char.`. `20260309_HermitMedow.xlsx` has `d24`, `d28`, `d48`, `d59` in the fracture column and `d13` in `Down`. **Action:** researcher to confirm; document.

### C3. Hand hardness (`RESISTANCE`)

Non-standard values: `p` (3), `4f`, `IF`/`IF+` (letter I for digit 1), `1K`, `K-`, `-` (4), ranges `4F -> 1F`, `4F to 1F`, `F/1F`. v1 also had ranges (`P to K`, `1F+ to P`). **Action:** document; optional case fix `p`→`P`, `4f`→`4F`, `IF`→`1F` with approval.

### C4. Grain form (`FORM`)

Non-ICSSG or inconsistent codes: `R` (8, probably RG), `CR` (3), `Fc`, `Ice`, `K` (hardness code in form column), hyphenated mixes `RG-DF`, `DF - RG`, `MF-CR`, `MFcr-FC`, `SH (4-6)`. v1 used parentheses for secondary forms (`FC (RG)`). **Action:** document; harmonize notation only with researcher approval.

### C5. BHG value formats

Single numbers, triplets (`75-60-48`, `2.03-1.83-2.42`), ranges (`3 to 4`, `3.7 - 5`), decimal commas (`0,06`, `6,08` in `20260305_RogersPass.xlsx`), `-`. `RoundHill.xlsx` triplet `75-60-48` is far outside the 0–50 N range. **Action:** document format and unit (N); researcher to confirm `75-60-48`; decimal commas may be converted in prepared copies (approval).

### C6. Linkage sheet names

Same content under different names: `dku`/`Dual KU`, `Radar K`/`RadarK`/`Radar K GPS`, `SS`/`SnowScope`/`Snowscope`. Several are unfilled templates (Hermit workbooks, Round Hill 03-10). **Action:** document; optionally harmonize sheet names in prepared copies.

---

## D. Naming

### D1. Site names

Variants: Hermit Meadows / Hermit Meadow / HermitMedow / HERMIT; Jim Bay / JimBay / JimBayCorner / Jim Bay Corner; Gopher Butte / GopherButte / Gopher_Butte / Gopher; Round Hill / RoundHill / RH; Rogers Pass / RogersPass / RP. **Action:** apply v1 snake_case site names in the prepared package (`hermit_meadows`, `jim_bay_corner`, `gopher_butte`, `round_hill`, `rogers_pass`, `fidelity`).

### D2. Free-form file names

`20260310_Round Hill upper snowpackl.xlsx` (typo, space), `IRIS2 _HermitMedow.TXT` (space), `IRIS#1-Gopher Butte TP/20260304.TXT` (`#`, space), `HERMIT MEADOWS TR.csv`, `uppersnowpackstability.xlsx` (no date or site). **Action:** rename to the v1 convention `<YYYYMMDD>_<site>_<content>.<ext>`.

### D3. Observer initials not in the team list

`MS` and `NaA` in `20260310_Round Hill upper snowpackl.xlsx`; `jb`, `JM-AL`, `NM-AL` formats vary. **Action:** researcher to identify MS and NaA (field participants list for the PR reviewer).

---

## E. Low — format and portability

- **E1.** Extension casing: 13 `.TXT` (IRIS) vs 316 `.txt`. Normalize to lowercase in prepared names (v1 did).
- **E2.** Duplicate photo `FullProfile_picture.jpg` = `GPS_pts/97885b1e-….jpg` (excluded class anyway).
- **E3.** IRIS-2 files have 4 columns, IRIS-1/IRIS-3 have 2 (see exploration §4). Document both.
- **E4.** Short file: `IRIS2_20260303_upperSnowpackStability.TXT`, 18 lines — consistent with a short upper-snowpack profile, no action.

---

## F. Cross-period consistency (v1 → 2025-2026)

Differences that would confuse a user combining both periods:

| Topic | Difference | Recommendation |
|---|---|---|
| K-band folder | v1 `radar_FMCW_K/`; 2026 `ka/` + `Radar_K/` | harmonize to `radar_FMCW_K/` |
| K-band timestamps | v1 correct; 2026 clock wrong | document in README per period |
| New instrument | dual-Ku only in 2026 | new top-level folder, documented as 2026 only |
| Stratigraphy template | v1: 4 sheets; 2026: up to 9, with BHG and linkage sheets | document sheets per period in README codebook |
| Heights | v1 elevations from workbooks/GPS; 2026 mixes ellipsoidal (GNSS), app (SnowScope), workbook | state height reference per source |
| SnowScope | v1 reflectance column partly filled; 2026 always empty; 2 new header keys | document |
| GNSS | v1 CSV + zipped shapefile; 2026 KML/KMZ (+1 CSV) | keep raw exports; optionally derive CSV for consistency (derived file, documented) |
| Sites | "Hermit" (v1, weather-station area ~51.323 N) vs "Hermit Meadows" (2026, ~51.330 N) | keep separate names |
| Vocabulary | 2026 adds lowercase test codes, hyphenated forms, BHG | same handling in both periods (v1 left values as recorded) |

## G. Erratum candidates in the published v1

No data error found in v1 files. Documentation-level only:

1. **FRDR description and keywords omit SnowScope** (319 files in v1). Fix in v2 metadata.
2. **v1 README says IRIS sheets "preserve field calibration voltages"**, but the IRIS sheet of `20250303_hermit_stratigraphy.xlsx`, `20250306_christiana_ridge_stratigraphy.xlsx` and `20250306_fidelity_revisit_stratigraphy.xlsx` is the unfilled template. Clarify in the v2 README (no file change).

---

## Questions for the researcher (summary)

1. A1: which Gopher Butte (03-04) sheets hold real data?
2. A2: which workbook do the BHG readings belong to (Hermit Meadows or Round Hill 03-10)?
3. A3: dual-Ku linkage convention (off by one?) and the 780–789 tables.
4. A4: where are SMP files 764–775 and 784?
5. A5: better copies of the empty dual-Ku/K-band files?
6. B1, B3, B4: confirm date, location and the SWE-only pit.
7. C2, C5: swapped Down/Fracture columns; BHG `75-60-48`.
8. D3: who are MS and NaA?
9. Dual-Ku header field definitions and `RADAR HEIGHT` unit; any GRIMP reader script to cite.
10. Emlid CSV exports for days other than 03-09?
