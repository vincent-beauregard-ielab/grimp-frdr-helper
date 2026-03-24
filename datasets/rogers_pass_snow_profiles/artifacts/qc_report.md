
# Quality Control Report: Rogers Pass Snow Profiles

**Date:** 2026-03-24
**Status:** Prepared for Level 2 researcher review

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
| Morning hazard assessment PDFs | Open | Researcher decision still required |
| HEIC field notebook photos | Exclude for now | Researcher decision still required |
| Logistics, planning, and travel documents | Exclude | Administrative material |

## Issues and status

| Issue | Status | Action |
|---|---|---|
| Raw folders use spaces, mixed case, and inconsistent site tokens | Resolved | Prepared package uses standardized FRDR folder names |
| Day 1 IRIS file naming differs from Days 2-6 | Resolved | Renamed to `20250301_fidelity_iris_raw.txt` |
| Day 6 SnowScope folder typo uses `20240306` and `christridge` | Resolved | Prepared folder is `20250306_christiana_ridge_snowscope` |
| DOCX field notes are not deposit-friendly | Resolved | Converted eight DOCX files to UTF-8 TXT |
| Scientific and administrative material are mixed in raw package | Resolved | Only in-scope scientific/support files were copied to `frdr_data/` |
| Day 6 Fidelity stratigraphy workbook may be misfiled or a revisit | Open | Included with explicit `revisit` naming; researcher confirmation required |
| Radar band terminology (`radar_k` vs `radar_ka`) is inconsistent | Open | Prepared folder standardized, wording still needs confirmation |
| Hazard assessment PDFs are still undecided | Open | Excluded from prepared package pending researcher decision |
| Some raw SMP headers contain invalid GPS sentinels | Documented | Left unchanged because source data were not edited |
| Some template-derived workbook cells contain placeholder zeros | Documented | Left unchanged because source data were not edited |

## README consistency check

- The README draft describes the prepared folders in `frdr_data/`, not the raw directory.
- The README draft documents the naming convention for standardized folders and representative raw instrument file names.
- The README draft explains how linkage workbooks, GPS files, shapefile ZIPs, radar exports, SnowScope files, SMP files, and stratigraphy workbooks relate to each other.
- The README draft explicitly lists excluded or pending materials so the deposit boundary is reviewable.
