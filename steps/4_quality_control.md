# Quality Control

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

- `datasets/{id}/artifacts/qc_report.md`
