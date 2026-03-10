# Data Preparation

Prepare data files for FRDR deposit by acting on issues identified in Quality Control. This step transforms raw data into deposit-ready files while preserving originals.

**Autonomy:** Level 2 — Modifies files, researcher must approve transforms.

**Requires:** Quality Control complete and reviewed.

## Non-destructive rule

**IMPORTANT: This step is non-destructive to original data.** All operations read from `datasets/{id}/raw_data/` and write to `datasets/{id}/frdr_data/`. Never modify files in `raw_data/`.

**All data preparation must be captured in a Jupyter notebook** saved to `notebooks/` with dataset name in filename (e.g., `notebooks/{id}_data_preparation.ipynb`) for reproducibility.

## Actions (driven by QC report)

- **File operations** — Copy and rename files from `raw_data/` to `frdr_data/`, apply consistent naming conventions, fix extension casing
- **Column/field fixes** — Correct typos in column names, standardize header casing, fix inconsistent site spelling
- **Data transforms** — Fix encoding issues, standardize date formatting, apply unit conversions when identified by QC
- **Subset and filter** — Drop out-of-scope records, merge split files, restructure folder layout for deposit
- **Documentation** — Record every transformation applied, mapping old names/values to new ones

## FRDR file naming conventions

File names should be logical, descriptive, and brief. Include project, content, date or version number. Use alphanumeric characters only — avoid spaces or special characters. Document naming conventions in the README.

## Verification report

A mandatory deliverable that the researcher reviews before approving Data Preparation. This is the Level 2 review gate. The report must include:

- **Change summary** — Total files copied, renamed, modified, excluded
- **File inventory** — Side-by-side comparison of `raw_data/` vs `frdr_data/` (file count, names, sizes)
- **Structural changes** — For each modified file: rows before/after, columns before/after, sheets/tables before/after
- **Transformation log** — Every change applied, with before → after examples (e.g., column rename, date reformat, value remap)
- **Excluded data** — What was dropped and why (out-of-scope records, duplicate blocks, ancillary files)
- **Unresolved issues** — QC issues that were not addressed and why (needs researcher decision, out of scope, etc.)

## Outputs

- `datasets/{id}/frdr_data/` — Deposit-ready files
- `notebooks/{id}_data_preparation.ipynb` — Reproducible transformation notebook
- `datasets/{id}/artifacts/verification_report.md` — Human-readable verification report
- Update `datasets/{id}/artifacts/qc_report.md` with a "Resolved" status for each addressed issue
