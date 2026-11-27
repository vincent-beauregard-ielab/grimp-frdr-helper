⚠️ REVIEW INSTRUCTIONS
This document is part of the FRDR deposit preparation package for **Rogers Pass Snow Profiles** (new version v2).
🚩 marks items requiring your decision — please comment directly on these lines.
⚠️ marks critical context for your understanding — no action required.
Your companion review document is README.txt.
Notebooks and artifacts/ are reference material — you do not need to review them.
----------------------------------------------------------------

# Data Preparation Report

**Dataset:** Rogers Pass Snow Profiles
**Dataset ID:** rogers_pass_snow_profiles
**Version in preparation:** v2 (adds period 2025-2026 to the published v1, DOI 10.20383/103.01634)
**Last updated:** 2026-11-27

> **How to read this document.** It is a living document: it is updated at every workflow step, and each period section below carries a status.
> - **Projected** — the plan for Step 5 (Data Preparation). No files have been prepared yet. Your answers to the 🚩 items shape what will be prepared.
> - **Prepared** — Step 5 is done: the section records what was actually done.
> - **Final** — reviewed, all 🚩 resolved, ready for deposit.
> - **Published** — already on FRDR; carried over unchanged.
>
> The document has one section per campaign period (field season), newest first. You only need to read the section for the period under review.
>
> **Current review: period 2025-2026 (Projected).** Period 2024-2025 is published and is not under review.

---

## Period 2025-2026 — Projected

<!-- AGENT: remove this comment and the banner below at the end of Step 5, and set the period status to Prepared. -->
> ⚠️ **PROJECTED PLAN.** This section describes what Step 5 *will* do, based on the Quality Control findings. No files have been prepared yet. Tables marked "projected" contain expected values and will be replaced by actual results.

Sources: `artifacts/2025-2026/data_exploration.md`, `artifacts/2025-2026/research.md`, `artifacts/2025-2026/qc_report.md`. Issue references (A1, B7, …) point to the QC report.

### Scope

| Dimension | Value |
|-----------|-------|
| Spatial coverage | Rogers Pass area, Glacier National Park, BC: Round Hill, Fidelity, Gopher Butte, Rogers Pass, Jim Bay Corner, Hermit Meadows. Bounding box 2025-2026: W -117.7078, E -117.5160, S 51.2342, N 51.3311 (WGS84) |
| Temporal extent | 2026-03-03 to 2026-03-10 (data on 03-03, 03-04, 03-05, 03-06, 03-09, 03-10; none on 03-07 and 03-08) |
| Measurement domain | Snow stratigraphy and stability, density, IRIS, SMP (to 1.7 m), SnowScope (to 2.46 m), K-band radar (23.5–26 GHz), **dual Ku-band radar (12.5–18.5 GHz, new instrument)**, GNSS (Emlid RTK). Elevation 1303–2125 m |

### Proposed Deposit Scope

Each row describes one file class. Counts are projected from the data exploration (567 raw files).
🚩 marks any item where a decision is required before deposit can proceed.

| Category | Files | Decision | Rationale |
|----------|------:|----------|-----------|
| Snow stratigraphy workbooks | 14 | Include | Same template family as v1, expanded with linkage and BHG sheets. Several content issues, see Unresolved Issues (A1, A2, B1–B7) |
| IRIS TXT exports | 13 | Include | Two formats by unit (2 or 4 columns); documented |
| SMP `.pnt` profiles | 48 | Include | 🚩 12 SMP files referenced in the workbooks do not exist in the raw data (A4) |
| SnowScope CSV profiles | 89 | Include | Reflectance column empty in all files; 7 files with stale phone location (documented, not altered) |
| K-band radar TXT | 139 | Include | Same instrument as v1 (folders `ka/` and `Radar_K/` become `radar_FMCW_K/`). Instrument clock was wrong: file-name dates are not real dates. 2 empty files excluded |
| Dual Ku-band radar TXT | 170 | Include | New instrument in this period. 5 empty files excluded. 🚩 Folder name to decide |
| Spatial linkage workbooks | 4 | Include | Link measurements to transect points; renamed to v1 convention |
| GNSS exports (KML, KMZ, CSV) | 6 | Include | Raw exports kept. 🚩 Derive a CSV for consistency with v1? |
| Field readmes (DOCX to TXT) | 7 | Include | French field notes, converted to UTF-8 text as in v1 |
| 🚩 Field-book index (DOCX) | 1 | **Pending your decision** — Include or Exclude? | v1 excluded the field-book index as administrative material. Excluded in this projection |
| Photos (HEIC/JPG) | 57 | Exclude | v1 precedent |
| Hazard / risk assessment PDFs | 9 | Exclude | v1 precedent |
| Blank templates | 3 | Exclude | Not observed data |
| Empty files (0 bytes) | 7 | Exclude | Failed acquisitions: 2 K-band, 5 dual-Ku (A5). 🚩 Better copies may exist |
| **Total** | **567** | **490 included, 77 excluded** | |

### Restructure of the published files

The published v1 is flat (`frdr_data/iris/…`). To hold several periods, v1 files move under `frdr_data/2024-2025/`. File contents do not change: Step 5 verifies every published file by checksum after the move. Public file paths change, so the README version history and the public summary of changes will announce it.

| Published path (v1) | Path in v2 |
|---|---|
| `documentation/` | `2024-2025/documentation/` |
| `iris/` | `2024-2025/iris/` |
| `radar_FMCW_K/` | `2024-2025/radar_FMCW_K/` |
| `snow_stratigraphy/` | `2024-2025/snow_stratigraphy/` |
| `snowmicropenetrometer/` | `2024-2025/snowmicropenetrometer/` |
| `snowscope/` | `2024-2025/snowscope/` |
| `spatial_reference/` | `2024-2025/spatial_reference/` |
| `README.txt`, `LICENSE.txt`, `CITATION.txt` | unchanged (top level); `README.txt` is replaced by the v2 README |

### frdr_data/ File Tree (projected)

```
frdr_data/
├── README.txt                       (v2, covers both periods)
├── LICENSE.txt
├── CITATION.txt
├── 2024-2025/                       (published v1, 595 files, unchanged, moved only)
│   ├── documentation/  iris/  radar_FMCW_K/  snow_stratigraphy/
│   └── snowmicropenetrometer/  snowscope/  spatial_reference/
└── 2025-2026/                       (new, 490 files)
    ├── documentation/               7
    ├── iris/                        13
    ├── radar_FMCW_K/                139
    ├── radar_FMCW_dual_Ku/          170   (🚩 folder name to decide)
    ├── snow_stratigraphy/           14
    ├── snowmicropenetrometer/       48
    ├── snowscope/                   89
    └── spatial_reference/           10    (4 linkage workbooks + 6 GNSS exports)
```

Naming follows v1: `<datatype>/<YYYYMMDD>_<site>[_<content>]`, lowercase, snake_case site names (`round_hill`, `fidelity`, `gopher_butte`, `rogers_pass`, `jim_bay_corner`, `hermit_meadows`). The complete tree is generated at Step 5.

**Total (projected):** 490 new files, plus the 595 carried-over v1 files and 3 top-level files.

### Change Summary (projected)

| Operation | Count |
|-----------|-------|
| Raw files reviewed | 567 |
| Files included in `frdr_data/2025-2026/` | 490 |
| Files excluded | 77 |
| Copy and rename / restructure (no content change) | 483 |
| DOCX to TXT conversions | 7 |
| Files with content modifications | 0 by default; up to 4 workbook types if you approve the options in the Transformation Log |
| v1 files moved to `2024-2025/` (content unchanged) | 595 |

### Transformation Log (planned)

No content change is planned unless you approve it. Packaging-only operations (copy, rename, restructure, K-band folder harmonization, extension lowercasing) are not listed here. Each row below is conditional on a decision in the Unresolved Issues table.

| File(s) | Transform | Before | After | QC issue | Depends on |
|---------|-----------|--------|-------|----------|------------|
| `GopherButte_2026-03-04.xlsx` | blank copied sheets | `Stability Tests`, `Density`, `IRIS` identical to Round Hill 03-03 | marked "not recorded" | A1 | Question 1 |
| BHG sheet of one workbook (Hermit Meadows or Round Hill 03-10) | blank duplicated sheet | identical in both workbooks | blanked in the workbook it does not belong to | A2 | Question 2 |
| `RoundHill_bottom.xlsx` | correct header date | 2026-04-03 | 2026-03-04 | B1 | Question 6 |
| 8 workbooks, Density sheets | blank placeholder zeros | 158 cells with `0` meaning "not measured" | empty cell | B7 | Question 13 |
| Stratigraphy workbooks | normalize vocabulary | e.g. `ct`, `Ect`, `p`, `IF`, decimal commas | standard codes | C1, C3, C4, C5 | Question 13 |

### Excluded Files (projected)

| File(s) | Reason |
|---------|--------|
| 57 photos (HEIC, JPG) | Not part of the deposit (v1 precedent) |
| 9 hazard / risk assessment PDFs | Operational forms (v1 precedent) |
| 3 templates (`StratiTemplate`, hazard form, photo checklist) | Blank templates |
| 7 empty files (2 K-band, 5 dual-Ku) | Failed acquisitions, listed individually at Step 5 (A5) |
| Field-book index (DOCX) | 🚩 Administrative material (v1 precedent); your decision |

### Unresolved Issues

Questions 1–10 come from the QC report. Questions 11–15 are deposit-scope decisions. For each question, say what you want done; we apply it at Step 5.

| # | Issue | Status | Notes |
|---|-------|--------|-------|
| 1 | 🚩 Gopher Butte 03-04 workbook: which sheets hold real data? (A1) | Pending researcher decision | `Stability Tests`, `Density`, `IRIS` are identical to Round Hill 03-03. If you confirm which were really measured, we keep those and mark the others "not recorded" |
| 2 | 🚩 BHG readings: Hermit Meadows or Round Hill 03-10? (A2) | Pending researcher decision | Same sheet in both workbooks. We blank it in the other one |
| 3 | 🚩 Dual-Ku linkage tables: is the counter recorded before the first sweep (off by one)? Are the 780–789 tables in `RoundHill*.xlsx` placeholders? (A3) | Pending researcher decision | Tables are not edited. File names are documented as authoritative; a corrected linkage table can be added, marked as derived |
| 4 | 🚩 Where are SMP files 764–775 and 784? (A4) | Pending researcher decision | If found, add to raw data before Step 5. If not, documented as missing (Rogers Pass and Jim Bay full profiles) |
| 5 | 🚩 Better copies of the 7 empty files? (A5) | Pending researcher decision | Fidelity tower dual-Ku would otherwise keep only counter 830 and half of 832 |
| 6 | 🚩 Confirm: date of `RoundHill_bottom.xlsx` (B1), location of `GopherButte_upperSnowpack.xlsx` (B3), SWE-only Hermit surface pit 2 (B4) | Pending researcher decision | Raw values documented; corrections only in prepared copies, if you agree |
| 7 | 🚩 Swapped `Down` / fracture-character columns (C2); BHG value `75-60-48` outside 0–50 N (C5) | Pending researcher decision | Documented as found unless you correct |
| 8 | 🚩 Who are observers "MS" and "NaA"? (D3) | Pending researcher decision | Appear in one workbook and are not in the team list. The participants list itself is completed at Step 6 |
| 9 | 🚩 Dual-Ku header fields and `RADAR HEIGHT` unit: documentation or reader script to cite? | Pending researcher decision | No public documentation found |
| 10 | 🚩 Emlid CSV exports for days other than 2026-03-09? (B10) | Pending researcher decision | Only KML/KMZ exist for the other days |
| 11 | 🚩 Dual-Ku folder name | Pending researcher decision | Proposed `radar_FMCW_dual_Ku` |
| 12 | 🚩 K-band file names: keep raw names (clock dates wrong) or rename with real dates? (B8) | Pending researcher decision | Proposed: keep raw names (they carry the instrument counter), document real dates by day |
| 13 | 🚩 Vocabulary and placeholder zeros (B7, C1, C3, C4, C5): leave as recorded (v1 precedent) or normalize in prepared copies? | Pending researcher decision | Proposed: leave as recorded and document in the README codebook |
| 14 | 🚩 GNSS: deposit KML/KMZ only, or also a derived CSV for consistency with v1? | Pending researcher decision | A derived file would be marked as derived |
| 15 | 🚩 Field-book index: include? | Pending researcher decision | Excluded in this projection (v1 precedent) |
| – | ⚠️ K-band clock was not set | Acknowledged — not blocking deposit | File names and headers show 2025-09; real dates come from the day folders (B8) |
| – | ⚠️ SnowScope: reflectance column empty; 7 files with stale phone location (45 km off) | Acknowledged — not blocking deposit | Documented, values not altered (B9) |
| – | ⚠️ Missing GNSS: Rogers Pass profile; Day 1 heights; 2 SMP files without fix | Acknowledged — not blocking deposit | Documented (B10) |
| – | ⚠️ Heights mix ellipsoidal (GNSS), app (SnowScope) and workbook values | Acknowledged — not blocking deposit | The README states the height reference per source |

---

## Period 2024-2025 — Published (v1, DOI 10.20383/103.01634)

> ⚠️ **Published and carried over unchanged.** This section is the Data Preparation Report of v1 as written on 2026-03-24, kept for the record. Its paths are the flat v1 paths; in v2 these files move under `frdr_data/2024-2025/` (see the path table in the 2025-2026 section). Only the heading level and this note were changed.

**Date:** 2026-03-24
**Prepared package:** `datasets/rogers_pass_snow_profiles/frdr_data/`
**Notebook:** `notebooks/data_preparation.ipynb`

### Proposed deposit scope

| Material class | Decision | Notes |
|---|---|---|
| Snow stratigraphy XLSX workbooks | Include | Seven workbooks kept in raw Excel format with standardized names |
| IRIS TXT exports | Include | Six daily raw text exports kept unchanged except naming normalization |
| SMP `.pnt` profiles | Include | Four day-site folders preserved as binary raw outputs |
| SnowScope CSV profiles | Include | Five day-site folders preserved with standardized folder names |
| Radar TXT exports | Include | Five day-site folders preserved with standardized folder names |
| Spatial linkage XLSX / GPS CSV / SHP ZIP | Include | First-class scientific support files linking measurements to coordinates |
| Site and instrument DOCX notes | Include as ancillary support | Converted to plain text in `documentation/` |
| Morning hazard assessment PDFs | Open | Researcher decision still required |
| HEIC field notebook photos | Exclude for now | Researcher decision still required |
| Logistics, planning, and travel documents | Exclude | Administrative material |

### Change summary

- Raw files reviewed: 633
- Files included in `frdr_data/`: 595
- Files excluded from `frdr_data/`: 38
- Copy and rename operations: 23
- Copy and restructure operations: 564
- DOCX to TXT conversions: 8
- Scientific data values modified: 0

### File inventory

| Category | Prepared files | Size (MB) | Notes |
|---|---:|---:|---|
| snow_stratigraphy | 7 | 1.51 | Seven snow-pit workbooks, including one unconfirmed Day 6 Fidelity revisit workbook |
| iris | 6 | 0.01 | Six daily IRIS raw text exports with normalized names |
| snowmicropenetrometer | 79 | 62.35 | Four day-site folders of `.pnt` profiles |
| snowscope | 319 | 10.01 | Five standardized SnowScope folder names |
| radar | 166 | 17.82 | Five day-site radar folders; Day 5 raw `radar_ka` folder standardized here |
| spatial_reference | 10 | 0.12 | Linkage workbooks, RTK CSVs, and zipped shapefiles |
| documentation | 8 | 0.01 | French field and instrument notes converted from DOCX to UTF-8 TXT |

### Structural changes

- Folder structure was reorganized from day-first raw folders into deposit folders grouped by data type: `snow_stratigraphy/`, `iris/`, `snowmicropenetrometer/`, `snowscope/`, `radar/`, `spatial_reference/`, and `documentation/`.
- File names were normalized to lowercase or to explicit `<YYYYMMDD>_<site>_<content>` names for top-level prepared files.
- No scientific file contents were edited. The only format conversion was DOCX to plain text for documentation files.
- The Day 6 SnowScope raw folder name typo (`SS4_christridge_20240306`) was corrected in the prepared folder name `20250306_christiana_ridge_snowscope`.

### Transformation log

- `Jour 1 - Fidelity/IRIS data/IRIS_20250301.TXT` -> `frdr_data/iris/20250301_fidelity_iris_raw.txt`
- `Jour 5 - Round Hill/Spatial Survey/radar_ka/` -> `frdr_data/radar/20250305_round_hill/`
- `Jour 6 - RoundHill and Christiana Ridge/Spatial Survey Christiana Ridge/SS4_christridge_20240306/` -> `frdr_data/snowscope/20250306_christiana_ridge_snowscope/`
- `Jour 4 - Fidelity/20250304_Fidelity.docx` -> `frdr_data/documentation/20250304_fidelity_field_notes_fr.txt`
- `Jour 6 - RoundHill and Christiana Ridge/Fidelity_Strati_20250306.xlsx` -> `frdr_data/snow_stratigraphy/20250306_fidelity_revisit_stratigraphy.xlsx`

### Structural checks on representative file types

- Snow stratigraphy workbooks: 7 files, 4 sheets per workbook, preserved as Excel without row or column edits.
- IRIS text files: 6 files, 52-92 rows per file, still two-column raw text.
- SMP `.pnt` files: 79 files, 3-411400 samples per file, binary content unchanged.
- SnowScope CSV files: 319 files, 81-2266 profile rows per file, metadata header + profile table preserved.
- Radar TXT files: 166 files, 2565 rows per file, metadata header + numeric table preserved.
- GPS CSV files: 3 files, coordinate/elevation values unchanged.

### Excluded data

- 25 HEIC field notebook photos were excluded pending a researcher decision on whether image scans belong in the public deposit.
- 6 morning hazard assessment PDFs were excluded pending a researcher decision on whether operational hazard forms belong in the deposit.
- The planning DOCX, the parking/travel PDFs, the logistics spreadsheet, and the field-book index were excluded as administrative material.
- `StratiTemplate.xlsx` was excluded as a blank template rather than observed data.
- `IRIS_20250301.TXT.docx` was excluded as a companion duplicate of the IRIS raw text export.

### Unresolved issues

- The prepared package includes `20250306_fidelity_revisit_stratigraphy.xlsx`, but the Day 6 Fidelity revisit remains unconfirmed and should be reviewed by the researcher before deposit.
- Raw Day 5 radar files were stored in a folder named `radar_ka` while the research notes describe a 24 GHz K-band radar. The prepared package standardizes the folder name to `radar/`, but the band terminology should be confirmed in the final README review.
- Hazard assessment PDFs remain excluded until the researcher decides whether they are in scope.
- Some raw SMP files contain invalid GPS sentinels and some template-derived workbook cells use placeholder zeros; these raw-source conditions were documented rather than altered.

### README consistency check

- The README draft describes the prepared folders in `frdr_data/`, not the raw directory.
- The README draft documents the naming convention for standardized folders and representative raw instrument file names.
- The README draft explains how linkage workbooks, GPS files, shapefile ZIPs, radar exports, SnowScope files, SMP files, and stratigraphy workbooks relate to each other.
- The README draft explicitly lists excluded or pending materials so the deposit boundary is reviewable.
