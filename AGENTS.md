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

Before running or creating Jupyter notebooks, ensure JupyterLab is running:

```bash
uv run scripts/jupyter_mcp.py
```

## Agent tasks

### Elicitation

Ask questions to understand the dataset: what data was collected, how it is structured, what instruments were used, what processing was applied, and how files should be organized for deposit.

Use `docs/project_context.md` for GRIMP/MOACC context and `docs/controlled_vocabulary.md` for standard terminology.

### Research

Gather quotes and claims from documents (papers, web sources, knowledge base) to describe the dataset's variables, methodology, and file structure. The output serves as context for README drafting and quality control.

**Sources to use:**

- Papers in `papers/`
- Web searches for instrument specs, standards (CAAML, OGRS), and related publications
- `docs/project_context.md` for organizational context
- `datasets/example/` as a reference for format and content

**Output format:**

Save results to `datasets/{id}/artifacts/research.md` with sections:

- **Dataset overall description** — Scope, research objective, organizational context, umbrella initiative
- **Glossary** — Key terms tagged as `instrument`, `variable`, `technique`, `acquisition`, `processing`, `initiative`, or `organization`

### Explore data files

Inspect data files using pandas in a Jupyter notebook. For each file, document:

- Column names and data types
- Enum/categorical fields and their values
- Value ranges for numeric fields
- Missing value encoding (NA, NaN, empty string, sentinel values)
- Case uniformity across text fields
- File encoding and delimiter

Use Anthropic xlsx/pdf skills for Excel and PDF files.

Save notebook to `notebooks/` with dataset name in filename.

### Draft FRDR README

Generate the dataset README from `docs/FRDR-template_README.txt`, filling in:

- General information (title, authors, dates, geographic location, funding)
- Sharing/access (license, citation, related datasets)
- Data & file overview (file list with descriptions, naming conventions)
- Methodological information (acquisition methods, processing steps, instruments, software)
- Data-specific sections (variable lists, missing data codes, units)

Use the research artifact (`artifacts/research.md`) and data exploration notebook as sources. Use `datasets/example/README.txt` as a reference for tone and level of detail.

Save output to `datasets/{id}/README.txt`.

### Quality control

Explore data files and validate integrity. Check for:

- Consistent column names and data types across files
- Unexpected missing values or encoding issues
- Value range outliers
- Filename/folder naming consistency
- Typos in column/sheet names (fix when found)

Save QC report to `datasets/{id}/artifacts/qc_report.md`.
