# AGENTS.md

Agents assist GRIMP researchers in archiving and documenting research datasets for deposit on FRDR. They generate metadata artifacts, inspect data files, and retrieve relevant information from literature, web sources, and helper modules.

## Project organization

* **`datasets/{id}/`** — First class. Each directory is one dataset to be uploaded to FRDR. Contains data files, the FRDR README, `about.yaml` (dataset identity), and `artifacts/` (research notes, extracted metadata, QC reports). `datasets/example/` is a reference template based on the published Rogers Pass snow profile dataset (DOI: 10.20383/103.01523).

* **`notebooks/`** — First class. All data exploration and manipulation must be done reproducibly in Jupyter notebooks.

* **`docs/`** — Project-level documentation: `project_context.md` (GRIMP/MOACC/FRDR context), `FRDR-template_README.txt` (README template), `controlled_vocabulary.md` (keywords).

* **`papers/`** — Domain literature (PDFs) relevant to GRIMP research.

* **`utils/`** — Python helper modules (e.g. `frdr_metadata.py` for fetching metadata from published FRDR datasets).

* **`scripts/`** — Utility scripts. `jupyter_mcp.py` starts JupyterLab with the token expected by the MCP server.

## Constraints

All documentation and results written in English.

Code is Python. Dependencies managed by `uv` in project `.venv`. Run code using `uv run`.

If local tooling expects a project `.env`, create it from `.env.example` before running `uv run`.

Before running or creating Jupyter notebooks, ensure JupyterLab is running:

```bash
uv run scripts/jupyter_mcp.py
```

## Human-in-the-loop

Default autonomy level is **Level 2** (agent proposes, human reviews). Autonomy scales inversely with reversibility.

| Level | Label | Pattern |
|-------|-------|---------|
| 1 | Agent assists | Agent drafts, human does everything |
| 2 | Agent proposes | Agent produces artifact, human reviews & approves before it is used |
| 3 | Agent executes with gates | Agent runs autonomously, pauses at checkpoints for human approval |
| 4 | Agent autonomous | Agent runs end-to-end, human spot-checks |

**Per-step autonomy targets:**

| Step | Level | Rationale |
|------|-------|-----------|
| Scope definition | 2 | Agent proposes scope from files + context, researcher validates |
| Research | 3 | Low risk — gathering quotes. Human spot-checks |
| Explore data | 3 | Notebook output is inspectable, non-destructive |
| Quality control | 2 | Findings need human judgment before action |
| Data preparation | 2 | Modifies files — researcher must approve transforms |
| Draft README | 2 | Public-facing artifact, needs careful review |
| Deposit | 1 | Researcher drives, agent assists. Irreversible action |

Start all steps at Level 2 and selectively promote to Level 3 as the team gains confidence. Do not plan for Level 4 until the workflow is well established.

## Agent tasks

### Scope definition

Define the boundaries of what will be archived on FRDR and described by the metadata. This step is iterative — it runs first but gets refined after Research and Explore Data as new information emerges.

**The scope must capture:**

- **Temporal extent** — Date range of observations or data collection periods
- **Spatial extent** — Geographic area, sites, coordinate systems
- **Measurements and variables** — What was measured, with what instruments, at what resolution
- **Data boundaries** — Which files are in scope for deposit vs. ancillary/excluded
- **Processing level** — Raw, cleaned, derived, or a mix

**Sub-activities:**

1. **Elicitation** — Ask questions to understand the dataset: what data was collected, how it is structured, what instruments were used, what processing was applied, and how files should be organized for deposit. Use `docs/project_context.md` for GRIMP/MOACC context and `docs/controlled_vocabulary.md` for standard terminology.

2. **Scope document** — Produce a concise scope statement summarizing the above dimensions. Save to `datasets/{id}/artifacts/scope.md`.

The scope document is a living artifact. Update it when Research or Explore Data reveals information that changes the boundaries (e.g., discovering additional file types, revised date ranges, or out-of-scope records).

### Research

Gather quotes and claims from documents (papers, web sources, knowledge base) to describe the dataset's variables, methodology, and file structure. The output serves as context for README drafting and quality control, so it must capture the non-tabular information required by the FRDR README template.

**Sources to use:**

- Papers in `papers/`
- Web searches for instrument specs, standards (CAAML, OGRS), and related publications
- `docs/project_context.md` for organizational context
- `datasets/example/` as a reference for format and content

**Output format:**

Save results to `datasets/{id}/artifacts/research.md` with sections:

- **Dataset overall description** — Scope, research objective, organizational context, umbrella initiative
- **README input capture** — Candidate title, people/institutions/roles, collection dates, geographic coverage, instruments, standards, processing stages, related publications/datasets/software, file-relationship notes, and unresolved README fields
- **Glossary** — Key terms tagged as `instrument`, `variable`, `technique`, `acquisition`, `processing`, `initiative`, `organization`, or `standard`
- **Source notes** — Brief claim-to-source mapping for later README drafting

The research artifact should answer as many FRDR README sections as possible before file parsing begins, especially:

- General information
- Sharing/access context
- Methodological context
- Standards and software context
- Related identifiers and ancillary-resource context

**Delegation:** Research is highly parallelizable. Spawn subagents concurrently for:

- **Papers subagent** — Read and extract claims from PDFs in `papers/`
- **Web subagent** — Search for instrument specs, standards, and related publications
- **Context subagent** — Read `docs/project_context.md`, `docs/controlled_vocabulary.md`, and `datasets/example/` for organizational and format context

The main agent merges subagent outputs into the final `research.md`.

### Explore data files

Inspect data files using pandas in a Jupyter notebook. Save the notebook to `notebooks/` with dataset name in filename and save a summary to `datasets/{id}/artifacts/data_exploration.md`.

Inspect the dataset by real file subtype, not only by extension. For example, a single dataset may contain:

- reference snowpit workbooks
- mapping/linkage workbooks
- instrument exports (CSV, TXT, binary)
- GNSS point files
- shapefiles or zipped shapefiles
- context/support files mixed into raw data

For each scientific file type, document:

- Column names and data types
- Enum/categorical fields and their values
- Value ranges for numeric fields
- Missing value encoding (NA, NaN, empty string, sentinel values)
- Case uniformity across text fields
- File encoding and delimiter
- Row counts / record counts where applicable
- Relationships between files when one file maps measurement IDs to another
- Software or Python packages required to read the format

Prefer available xlsx/pdf skills for Excel and PDF files when they exist in the current environment. If they are unavailable, fall back to local Python tooling such as `pandas`, `openpyxl`, `pypdf`, `pdfplumber`, and format-specific parsers.

The data exploration outputs should provide the file-derived facts needed for the FRDR README sections:

- Data & file overview
- Methodological information tied to actual stored formats
- Data-specific variable/codebook sections
- Missing-data and unit documentation

**Delegation:** Parallelize by file type group. Spawn one subagent per distinct format category (e.g., Excel workbooks, CSVs, shapefiles, GNSS files). Each subagent:

1. Inspects its file group in a dedicated notebook section or scratch notebook
2. Returns a structured summary (columns, types, ranges, missing values, encoding)

The main agent assembles summaries into `data_exploration.md` and the consolidated notebook. Keep cross-file relationship analysis (e.g., linkage between instrument files and GPS files) in the main agent, since it requires outputs from multiple subagents.

### Draft FRDR README

Generate the dataset README from `docs/FRDR-template_README.txt`, filling in:

- General information (title, authors, dates, geographic location, funding)
- Sharing/access (license, citation, related datasets)
- Data & file overview (file list with descriptions, naming conventions)
- Methodological information (acquisition methods, processing steps, instruments, software)
- Data-specific sections (variable lists, missing data codes, units)

Make sure the draft also accounts for:

- Relationship between files and folders
- Ancillary or excluded files
- Standards and calibration notes
- Quality-assurance notes
- Any format-specific software requirements

Use the scope document (`artifacts/scope.md`), research artifact (`artifacts/research.md`), data exploration outputs (`artifacts/data_exploration.md` + notebook), and data preparation notebook as sources. The README should describe the deposit-ready files in `frdr_data/`, not the raw originals. Use `datasets/example/README.txt` as a reference for tone and level of detail.

Save output to `datasets/{id}/README.txt`.

### Quality control

Explore data files and validate integrity. QC **flags issues and recommends actions** but does not modify data — all fixes happen in Data Preparation.

Check for:

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

For each issue found, the QC report should specify:

- **What** — The issue and where it occurs (file, column, row)
- **Impact** — How it affects deposit quality or reusability
- **Recommended action** — What Data Preparation should do (fix, document, exclude, or flag for researcher)

Save QC report to `datasets/{id}/artifacts/qc_report.md`.

### Data preparation

Prepare data files for FRDR deposit by acting on issues identified in Quality Control. This step transforms raw data into deposit-ready files while preserving originals.

**IMPORTANT: This step is non-destructive to original data.** All operations read from `datasets/{id}/raw_data/` and write to `datasets/{id}/frdr_data/`. Never modify files in `raw_data/`.

**All data preparation must be captured in a Jupyter notebook** saved to `notebooks/` with dataset name in filename (e.g., `notebooks/{id}_data_preparation.ipynb`) for reproducibility.

**Actions (driven by QC report):**

- **File operations** — Copy and rename files from `raw_data/` to `frdr_data/`, apply consistent naming conventions, fix extension casing
- **Column/field fixes** — Correct typos in column names, standardize header casing, fix inconsistent site spelling
- **Data transforms** — Fix encoding issues, standardize date formatting, apply unit conversions when identified by QC
- **Subset and filter** — Drop out-of-scope records, merge split files, restructure folder layout for deposit
- **Documentation** — Record every transformation applied, mapping old names/values to new ones

**Output:**

- `datasets/{id}/frdr_data/` — Deposit-ready files
- `notebooks/{id}_data_preparation.ipynb` — Reproducible transformation notebook
- `datasets/{id}/artifacts/verification_report.md` — Human-readable verification report (see below)
- Update `datasets/{id}/artifacts/qc_report.md` with a "Resolved" status for each addressed issue

**Verification report** — A mandatory deliverable that the researcher reviews before approving Data Preparation. This is the Level 2 review gate. The report must include:

- **Change summary** — Total files copied, renamed, modified, excluded
- **File inventory** — Side-by-side comparison of `raw_data/` vs `frdr_data/` (file count, names, sizes)
- **Structural changes** — For each modified file: rows before/after, columns before/after, sheets/tables before/after
- **Transformation log** — Every change applied, with before → after examples (e.g., column rename, date reformat, value remap)
- **Excluded data** — What was dropped and why (out-of-scope records, duplicate blocks, ancillary files)
- **Unresolved issues** — QC issues that were not addressed and why (needs researcher decision, out of scope, etc.)
