# Quality Control

## Documentation-coverage reconciliation (first action)

Before any data-quality checks, reconcile `research.md` against `data_exploration.md`:

1. **File-type coverage:** Every instrument or file type found in `data_exploration.md` must have a methodology entry and citable reference in `research.md`.
2. **Reverse check:** Every instrument in `research.md` must have corresponding files in `data_exploration.md` (catches phantom instruments described in literature but absent from the deposit).
3. **Variable coverage:** Every variable found in file headers or data columns must have a definition or unit in one of the two artifacts.

If gaps are found, send a targeted research request back to the Research step (step 2) covering only the missing items. This is a lightweight patch — typically a web search and one glossary entry per missing instrument — not a full re-run. Proceed with data-quality checks only after all instruments and variables are documented.

Explore data files and validate integrity. QC **flags issues and recommends actions** but does not modify data — all fixes happen in Data Preparation.

**Autonomy:** Level 2 — Findings need human judgment before action.

**Requires:** Research and Explore Data both complete.

## Checks

- Consistent column names and data types across files
- Unexpected missing values or encoding issues
- Value range outliers
- Filename/folder naming consistency
- Typos in column/sheet names
- Inconsistent site spelling, date formatting, or extension casing
- Placeholder/template values that look like real observations
- Truncated or suspiciously short sensor files
- Missing spatial metadata or broken links between instrument files and GPS/linkage files
- Repeated data blocks or other format quirks that must be documented for reuse

## Issue format

For each issue found, the QC report should specify:

- **What** — The issue and where it occurs (file, column, row)
- **Impact** — How it affects deposit quality or reusability
- **Recommended action** — What Data Preparation should do (fix, document, exclude, or flag for researcher)

## Outputs

- `datasets/{id}/artifacts/qc_report.md` — Issue list only. Does not include deposit scope summaries, file inventories, or README checks (those belong in the Data Preparation report or Preflight Validation).
