# Preflight Validation: Rogers Pass Snow Profiles

**Date:** 2026-04-29
**Status:** PASS

---

## Automated checks

| Check | Result | Notes |
|---|---|---|
| README title present | PASS | "Snow profile observation datasets, Rogers Pass, Glacier National Park, British Columbia, Canada" |
| README author / PI contact | PASS | Jean-Benoit Madore with confirmed email |
| README contact email | PASS | jean-benoit.madore@usherbrooke.ca |
| README collection dates | PASS | 2025-03-01 to 2025-03-06 |
| README geographic location + coordinates | PASS | Rogers Pass named; WGS84 bbox present |
| README license | PASS | CC BY-NC 4.0 |
| README funding | PASS | FRQNT and Fonds des nouvelles initiatives de recherche et de sauvetage |
| README no template markers (🔔) | PASS | 0 occurrences |
| README self-standing (no workflow refs) | PASS | No references to internal artifacts, PR numbers, or review rounds |
| README all deposit folders named | PASS | snow_stratigraphy/, iris/, snowmicropenetrometer/, snowscope/, radar_FMCW_K/, spatial_reference/, documentation/ |
| README variable definitions | PASS | DATA-SPECIFIC sections cover all 7 folder types with variable lists, units, and null-value codes |
| `frdr_data/` total files | PASS | 595 files (matches preparation report) |
| `frdr_data/` folder structure | PASS | 7 expected top-level folders, all present; no stale `radar/` folder |
| Folder file counts vs. preparation report | PASS | documentation 8, iris 6, radar_FMCW_K 166, snow_stratigraphy 7, snowmicropenetrometer 79, snowscope 319, spatial_reference 10 |
| `metadata.yaml` title | PASS | |
| `metadata.yaml` authors (10) | PASS | Madore, Langlois, Imbach, F. Gauthier, F. Meloche, V. Paquette, K. Hale, H.-P. Marshall, J. Meyer, J. Meloche |
| `metadata.yaml` contact | PASS | jean-benoit.madore@usherbrooke.ca |
| `metadata.yaml` license | PASS | CC BY-NC 4.0 |
| `metadata.yaml` time period | PASS | 2025-03-01 to 2025-03-06 |
| `metadata.yaml` bounding box | PASS | WGS84: west -117.7304, south 51.2274, east -117.4670, north 51.3284 |
| `metadata.yaml` funding | PASS | Two funders; award numbers blank (acceptable — not required by FRDR) |
| Required artifacts present | PASS | scope.md, research.md, data_exploration.md, qc_report.md, data_preparation_report.md |
| QC report: all issues resolved | PASS | Status "Researcher review applied (PR #2). All Open items resolved." |
| Researcher review applied | PASS | PR #2 comments from jbmadore incorporated 2026-04-28 |
| Third-party attributions | PASS | All instruments cited (Pomerleau et al. 2020, Montpetit et al. 2012, Schneebeli & Johnson 1998, Hagenmuller et al. 2024); standards cited (ICSSG, OGRS) |
| No protected or restricted information flagged | PASS | GPS coordinates are public field sites; no personal data beyond research team names |

---

## Flags requiring action before deposit

None. The previous placeholder-zero passthrough was resolved by rerunning `data_preparation.ipynb`: prepared stratigraphy workbooks now clear blank density-template formulas and materialize observed density formulas as numeric values.

---

## Known blanks (acceptable)

| Field | Status | Notes |
|---|---|---|
| DOI | Blank | Assigned by FRDR at deposit time |
| Award numbers | Blank | FRQNT and Fonds des nouvelles initiatives confirmed; numbers not yet provided — acceptable for initial submission |
| CRDC field-of-research code | Candidate only (RDF10508) | Researcher confirmation preferred; not blocking |
| F. Gauthier ORCID | Blank | Candidate 0000-0003-4961-7952 not confirmed as matching person; left blank |
| J. Meloche ORCID | Blank | Candidate 0000-0001-9617-1979 not confirmed; left blank |
| V. Paquette ORCID | Blank | No ORCID per researcher |
| DOI-per-year policy | Unconfirmed | Confirm with JB or FRDR liaison whether each campaign year gets its own DOI before submitting |

---

## Next step

Proceed to Step 8 Deposit after final researcher review of the prepared package.
