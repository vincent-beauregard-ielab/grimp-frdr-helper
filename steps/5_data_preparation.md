# Data Preparation

Prepare data files for FRDR deposit by acting on issues identified in Quality Control. This step transforms raw data into deposit-ready files while preserving originals.

**Autonomy:** Level 2 — Modifies files, researcher must approve transforms.

**Requires:** Quality Control complete and reviewed.

## Non-destructive rule

**IMPORTANT: This step is non-destructive to original data.** All operations read from `datasets/{id}/raw_data/` and write to `datasets/{id}/frdr_data/`. Never modify files in `raw_data/`.

**All data preparation must be captured in a Jupyter notebook** saved to `datasets/{id}/notebooks/` with dataset name in filename (e.g., `notebooks/{id}_data_preparation.ipynb`) for reproducibility.

## Expected notebook structure

The notebook must be organized as an auditable sequence of markdown-introduced operations. Each material operation gets its own markdown cell explaining the intent, source/target scope, and whether file contents are changed, followed by the code cell that performs only that operation.

Use this structure unless the dataset requires a clearly documented variation:

1. **Overview** — Dataset inputs, prepared outputs, naming conventions, and the non-destructive guarantee.
2. **Setup** — Imports, project paths, helper setup, and `TransformLog` initialization. This cell should not modify data.
3. **Reset target tree** — Optional idempotent reset of `frdr_data/`, guarded by an explicit flag.
4. **Packaging-only file operations** — Copy/rename/restructure cells that move files from `raw_data/` to `frdr_data/` without editing contents. Keep single-file mappings, directory copies, and format conversions in separate sections when they represent different operation types.
5. **Content-level transformations** — Any operation that changes values, formulas, encodings, columns, rows, or other file contents must be isolated in its own markdown + code cell pair. The markdown must explain the QC issue, the exact cleanup rule, which prepared files are affected, and why raw files remain unchanged. Do not hide content transformations inside generic copy cells.
6. **Excluded files** — Explicitly list raw files not deposited, with reasons.
7. **Structural statistics** — Read-only summaries of prepared files used by the report and README.
8. **Report table rendering** — Render transformation logs, summary tables, and the full `frdr_data/` file tree for `DATA_PREPARATION.md`.
9. **Sanity report and assertions** — End-to-end checks for expected file counts, transform counts, content-transformation counts, preservation checks, and unresolved QC assumptions.
10. **Synthesis for Report** — Markdown cells explaining key decisions and unresolved issues; code cells printing structured summaries (file counts per category, transform counts, any items flagged for researcher decision). The agent reads this section before writing `DATA_PREPARATION.md`. No intermediate file — the notebook is the source, the report is the formatted output.

For spreadsheet or workbook changes, keep the workbook transformation in a distinct code cell from the initial copy. For example, first copy the workbook into `frdr_data/`, then run a separately introduced Excel-cleanup cell on the prepared copy only. The transformation log should mark affected files with a specific transform name (for example, `copy_rename_clean_workbook`) rather than leaving them as plain copy operations.

After editing the notebook, run it end to end and leave the executed outputs in place. Do not present the step as complete until the notebook assertions pass.

## Actions (driven by QC report)

- **File operations** — Copy and rename files from `raw_data/` to `frdr_data/`, apply consistent naming conventions, fix extension casing
- **Column/field fixes** — Correct typos in column names, standardize header casing, fix inconsistent site spelling
- **Data transforms** — Fix encoding issues, standardize date formatting, apply unit conversions, clear template artifacts, or materialize derived values when identified by QC; each content-level transform must be isolated and explained in its own notebook section
- **Subset and filter** — Drop out-of-scope records, merge split files, restructure folder layout for deposit
- **Documentation** — Record every transformation applied, mapping old names/values to new ones

## FRDR file naming conventions

File names should be logical, descriptive, and brief. Include project, content, date or version number. Use alphanumeric characters only — avoid spaces or special characters. Document naming conventions in the README.

## Data Preparation report

A mandatory deliverable that the researcher reviews before approving Data Preparation. This is the Level 2 review gate. The report owns the complete picture of the prepared package — deposit scope, file inventory, transformations, and exclusions.

Generate the report from `docs/FRDR-template_DATA_PREPARATION.md`. The report must include:

- **Review instructions block** — ⚠️ preamble (see template) explaining the legend, companion README reference, and what to ignore
- **Proposed deposit scope** — Include/exclude decision for each material class, with rationale. Mark contested items with 🚩 for researcher decision.
- **`frdr_data/` file tree** — Complete directory tree of the deposit package as it exists after preparation
- **Change summary** — Total files copied, renamed, modified, excluded
- **Transformation log** — Every content-level change applied, with before → after examples (e.g., column rename, date reformat, value remap)
- **Excluded files** — What was dropped and why (out-of-scope records, duplicate blocks, ancillary files)
- **Unresolved issues** — QC issues not addressed and why (needs researcher decision, out of scope, etc.). Mark with 🚩 if researcher decision is required.

Use the `## Synthesis for Report` section of the notebook as the primary source. Do not duplicate the full file inventory from the notebook — reference the tree rendered in the report table rendering section.

Save the report to `datasets/{id}/DATA_PREPARATION.md` (not `artifacts/`). This file is a researcher-facing review document.

## Outputs

- `datasets/{id}/frdr_data/` — Deposit-ready files
- `datasets/{id}/notebooks/{id}_data_preparation.ipynb` — Reproducible transformation notebook
- `datasets/{id}/DATA_PREPARATION.md` — Researcher-facing report (generated from hardened template)
