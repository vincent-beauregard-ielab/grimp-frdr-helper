# Rogers Pass Snow Profiles QC Report

## Scope

This report implements step 6 of `plans/step_5_6_else_data_preparation.md`.

The raw package in `datasets/rogers_pass_snow_profiles/raw_data/Rogers Pass March 2024-2025` contains scientific files mixed with logistics and administrative material. The goal here is to define a proposed FRDR deposit scope and record the main reuse risks found during exploration.

Raw-tree counts used for this review:

- 322 `.csv`
- 79 `.pnt`
- 172 text exports with mixed `.txt` / `.TXT`
- 13 `.xlsx`
- 3 shapefile ZIP packages
- 11 `.docx`
- 17 `.pdf`
- 25 HEIC images

## Proposed deposit scope

### Include as core scientific data

| Class | Decision | Notes |
| --- | --- | --- |
| Filled stratigraphy workbooks in the six day folders | Include | Primary reference snowpit records. |
| SnowScope CSV profile folders | Include | Primary spatial hardness-depth observations. |
| Radar text export folders (`radar_k`, `radar_ka`, `Radar K`) | Include | Primary radar observations. |
| IRIS plain-text exports | Include | Primary instrument outputs. |
| SMP `.pnt` folders | Include | Primary penetrometer observations, including weak files that should be flagged rather than silently removed. |

### Include as ancillary or scientific support

| Class | Decision | Notes |
| --- | --- | --- |
| Mapping workbooks | Include as support | Needed to match radar, SMP, SnowScope, and profile IDs. |
| GNSS CSV exports | Include as support | Needed because `.pnt` coordinates are not usable. |
| Shapefile ZIP packages | Include as support | Spatial companions to the GNSS outputs. |
| Day-level field-note `.docx` files and instrument note files | Include as support | Explain point counts, workflows, and file relationships. |
| `StratiTemplate.xlsx` | Include as support | Blank template documenting workbook structure. |
| `README.txt` | Include as support | Required package documentation. |

### Exclude from deposit by default

| Class | Decision | Notes |
| --- | --- | --- |
| `AWP/` permit PDFs | Exclude | Administrative records. |
| `Bouffe et infos/` workbook | Exclude | Logistics only. |
| `Campagne Roger_s Pass 2025 planification.docx` | Exclude | Planning document, not measurement documentation. |
| `YUL parking reservation.pdf` | Exclude | Travel logistics only. |
| Morning hazard assessment PDFs | Exclude | Operational context, not the target scientific data product. |
| HEIC field photos and field-book images | Exclude by default | Useful provenance material but not needed for the current deposit scope. |
| `www.expedia...pdf` in `Jour 1 - Fidelity/Spatial_Jimbaycorner/` | Exclude | Travel or logistics artifact mixed into the raw tree. |

## Packaging recommendation

Recommended FRDR package:

- keep the six day folders
- retain scientific files in their original formats
- keep ancillary mapping files and field notes beside the relevant day folders
- remove excluded admin and logistics files before submission
- remove HEIC images unless the owner explicitly wants them archived with the data

## Confirmed issues

| Issue | Impact | Recommended handling |
| --- | --- | --- |
| `Round Hill` vs `RoundHill` spelling inconsistency | Ambiguous site naming in search and metadata. | Normalize to `Round Hill` in README and metadata; keep raw filenames as-is unless a derivative package is created. |
| `Christiana` vs `Christiania` spelling inconsistency | Ambiguous site identity for day 6 materials. | Normalize to `Christiania Ridge` in README and metadata; document the raw variation. |
| Mixed `.txt` / `.TXT` extension casing | Minor scripting friction. | Document only for raw-format deposit. |
| Mixed `.HEIC` / `.heic` extension casing | Minor inconsistency in excluded files. | No action needed if HEIC files remain excluded. |
| Likely date typo `202500306` in `Fidelity_Strati_20250306.xlsx` | Wrong date inside an included workbook. | Owner should confirm and correct in a prepared derivative, or document the typo if the raw workbook is deposited unchanged. |
| Placeholder zeros in template-derived workbook rows | Risk of reading placeholders as measurements. | Document in README and QC; only replace in a cleaned derivative after confirmation. |
| Truncated SMP file `Jour 5 - Round Hill/Spatial Survey/SMP/S35M0196.pnt` | Likely unusable as a scientific profile. | Keep for completeness but flag as likely truncated. |
| Missing or invalid coordinates in `.pnt` metadata | SMP files cannot be geolocated on their own. | Include GNSS CSVs and mapping workbooks as required support files. |
| Repeated radar data blocks within each export | Naive parsers may misread file shape. | Document explicitly in the README; no raw-file correction recommended. |

## Correct vs document

Correct in prepared deliverables if the owner wants a cleaned package:

- normalized site names in README and FRDR metadata
- the likely internal workbook date typo after owner confirmation
- confirmed template placeholder zeros in derivative tables only

Document rather than silently change in the raw package:

- extension-case differences
- repeated radar blocks
- missing `.pnt` coordinates
- truncated SMP file
- raw folder and filename spelling differences

## README verification

The draft `datasets/rogers_pass_snow_profiles/README.txt` is consistent with the current raw-tree review on the following points:

- collection dates span 2025-03-01 to 2025-03-06
- the package is organized by field day, not by instrument
- the main scientific file classes are stratigraphy workbooks, SnowScope CSVs, radar text exports, IRIS text exports, and SMP `.pnt` files
- mapping workbooks, GNSS CSVs, and shapefile ZIPs are needed to interpret spatial relationships
- `.pnt` files do not provide usable coordinates by themselves
- radar files contain repeated data blocks that must be documented

Still pending owner confirmation:

- final title
- author list and order
- public contact
- license
- funding statement
- whether excluded files should be reinstated as ancillary material
- whether the submission should remain raw-format or include a cleaned derivative

## Normalization requirement before FRDR submission

No raw-file renaming is strictly required if the dataset is submitted as a raw-format package with the README and QC report included.

Recommended before submission:

- remove excluded administrative and logistics files
- keep support files with the scientific day folders
- complete the owner-confirmed metadata fields in the README
- decide whether to correct the internal workbook date typo in a derivative package
