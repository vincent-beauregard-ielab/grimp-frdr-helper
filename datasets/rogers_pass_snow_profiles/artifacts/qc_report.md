
# Quality Control Report: Rogers Pass Snow Profiles

**Date:** 2026-03-24 (researcher review applied 2026-04-28)
**Status:** Researcher review applied (PR #2). All Open items resolved or documented.

## Issues

| Issue | Status | Action |
|---|---|---|
| Raw folders use spaces, mixed case, and inconsistent site tokens | Resolved | Prepared package uses standardized FRDR folder names |
| Day 1 IRIS file naming differs from Days 2-6 | Resolved | Renamed to `20250301_fidelity_iris_raw.txt` |
| Day 6 SnowScope folder typo uses `20240306` and `christridge` | Resolved | Prepared folder is `20250306_christiana_ridge_snowscope` |
| DOCX field notes are not deposit-friendly | Resolved | Converted eight DOCX files to UTF-8 TXT |
| Scientific and administrative material are mixed in raw package | Resolved | Only in-scope scientific/support files were copied to `frdr_data/` |
| Day 6 Fidelity stratigraphy workbook may be misfiled or a revisit | Resolved | Confirmed revisit at same Fidelity site five days after Day 1; kept with `_revisit` filename (PR #2). |
| Radar band terminology (`radar_k` vs `radar_ka`) is inconsistent | Resolved | Folder standardized to `radar_FMCW_K`; band confirmed K-band, center 24.5 GHz (PR #2). |
| Hazard assessment PDFs are still undecided | Resolved | Excluded as out of scope per researcher review (PR #2). |
| Some raw SMP headers contain invalid GPS sentinels | Documented | Left unchanged because source data were not edited |
| Some template-derived workbook cells contain placeholder zeros | Documented | Left unchanged because source data were not edited |
