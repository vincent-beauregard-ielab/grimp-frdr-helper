
# Data Preparation Report: Rogers Pass Snow Profiles

**Date:** 2026-03-24 (researcher review applied 2026-04-28, PR #2)
**Prepared package:** `datasets/rogers_pass_snow_profiles/frdr_data/`
**Notebook:** `datasets/rogers_pass_snow_profiles/notebooks/data_preparation.ipynb`

## Proposed deposit scope

| Material class | Decision | Notes |
|---|---|---|
| Snow stratigraphy XLSX workbooks | Include | Seven workbooks kept in raw Excel format with standardized names |
| IRIS TXT exports | Include | Six daily raw text exports kept unchanged except naming normalization |
| SMP `.pnt` profiles | Include | Four day-site folders preserved as binary raw outputs |
| SnowScope CSV profiles | Include | Five day-site folders preserved with standardized folder names |
| Radar TXT exports | Include | Five day-site folders preserved with standardized folder names |
| Spatial linkage XLSX / GPS CSV / SHP ZIP | Include | First-class scientific support files linking measurements to coordinates |
| Site and instrument DOCX notes | Include as ancillary support | Converted to plain text in `documentation/` |
| Morning hazard assessment PDFs | Exclude | Out of scope per researcher review (PR #2) |
| HEIC field notebook photos | Exclude | Out of scope per researcher review (PR #2) |
| Logistics, planning, and travel documents | Exclude | Administrative material |

## Change summary

- Raw files reviewed: 633
- Files included in `frdr_data/`: 595
- Files excluded from `frdr_data/`: 38
- Copy and rename operations: 23
- Copy and restructure operations: 564
- DOCX to TXT conversions: 8
- Scientific data values modified: 0

## File inventory

| Category | Prepared files | Size (MB) | Notes |
|---|---:|---:|---|
| snow_stratigraphy | 7 | 1.51 | Seven snow-pit workbooks, including one unconfirmed Day 6 Fidelity revisit workbook |
| iris | 6 | 0.01 | Six daily IRIS raw text exports with normalized names |
| snowmicropenetrometer | 79 | 62.35 | Four day-site folders of `.pnt` profiles |
| snowscope | 319 | 10.01 | Five standardized SnowScope folder names |
| radar_FMCW_K | 166 | 17.82 | Five day-site radar folders, K-band 24.5 GHz center, sweep 23.5–26 GHz |
| spatial_reference | 10 | 0.12 | Linkage workbooks, RTK CSVs, and zipped shapefiles |
| documentation | 8 | 0.01 | French field and instrument notes converted from DOCX to UTF-8 TXT |

## Structural changes

- Folder structure was reorganized from day-first raw folders into deposit folders grouped by data type: `snow_stratigraphy/`, `iris/`, `snowmicropenetrometer/`, `snowscope/`, `radar_FMCW_K/`, `spatial_reference/`, and `documentation/`.
- File names were normalized to lowercase or to explicit `<YYYYMMDD>_<site>_<content>` names for top-level prepared files.
- No scientific file contents were edited. The only format conversion was DOCX to plain text for documentation files.
- The Day 6 SnowScope raw folder name typo (`SS4_christridge_20240306`) was corrected in the prepared folder name `20250306_christiana_ridge_snowscope`.

## Transformation log

- `Jour 1 - Fidelity/IRIS data/IRIS_20250301.TXT` -> `frdr_data/iris/20250301_fidelity_iris_raw.txt`
- `Jour 5 - Round Hill/Spatial Survey/radar_ka/` -> `frdr_data/radar_FMCW_K/20250305_round_hill/`
- `Jour 6 - RoundHill and Christiana Ridge/Spatial Survey Christiana Ridge/SS4_christridge_20240306/` -> `frdr_data/snowscope/20250306_christiana_ridge_snowscope/`
- `Jour 4 - Fidelity/20250304_Fidelity.docx` -> `frdr_data/documentation/20250304_fidelity_field_notes_fr.txt`
- `Jour 6 - RoundHill and Christiana Ridge/Fidelity_Strati_20250306.xlsx` -> `frdr_data/snow_stratigraphy/20250306_fidelity_revisit_stratigraphy.xlsx`

## Structural checks on representative file types

- Snow stratigraphy workbooks: 7 files, 4 sheets per workbook, preserved as Excel without row or column edits.
- IRIS text files: 6 files, 52-92 rows per file, still two-column raw text.
- SMP `.pnt` files: 79 files, 3-411400 samples per file, binary content unchanged.
- SnowScope CSV files: 319 files, 81-2266 profile rows per file, metadata header + profile table preserved.
- Radar TXT files: 166 files, 2565 rows per file, metadata header + numeric table preserved.
- GPS CSV files: 3 files, coordinate/elevation values unchanged.

## Excluded data

- 25 HEIC field notebook photos were excluded as out of scope per researcher review (PR #2).
- 6 morning hazard assessment PDFs were excluded as out of scope per researcher review (PR #2).
- The planning DOCX, the parking/travel PDFs, the logistics spreadsheet, and the field-book index were excluded as administrative material.
- `StratiTemplate.xlsx` was excluded as a blank template rather than observed data.
- `IRIS_20250301.TXT.docx` was excluded as a companion duplicate of the IRIS raw text export.

## Unresolved issues

- The prepared package includes `20250306_fidelity_revisit_stratigraphy.xlsx`. Confirmed revisit by researcher (PR #2): same Fidelity site five days after Day 1; kept with `_revisit` filename.
- Raw Day 5 radar files were stored in a folder named `radar_ka`. Band confirmed K-band by researcher (PR #2). Folder standardized to `radar_FMCW_K`.
- Some raw SMP files contain invalid GPS sentinels; these were documented and left unchanged.
- Template-derived placeholder zeros remain flagged for the final researcher passthrough before deposit.

## README consistency check

- The README draft describes the prepared folders in `frdr_data/`, not the raw directory.
- The README draft documents the naming convention for standardized folders and representative raw instrument file names.
- The README draft explains how linkage workbooks, GPS files, shapefile ZIPs, radar exports, SnowScope files, SMP files, and stratigraphy workbooks relate to each other.
- The README draft explicitly lists excluded or pending materials so the deposit boundary is reviewable.
