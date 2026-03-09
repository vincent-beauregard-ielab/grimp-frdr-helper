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

## Agent tasks

### Elicitation

Ask questions to understand the dataset: what data was collected, how it is structured, what instruments were used, what processing was applied, and how files should be organized for deposit.

Use `docs/project_context.md` for GRIMP/MOACC context and `docs/controlled_vocabulary.md` for standard terminology.

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

Use the research artifact (`artifacts/research.md`) and data exploration outputs (`artifacts/data_exploration.md` + notebook) as sources. Use `datasets/example/README.txt` as a reference for tone and level of detail.

Save output to `datasets/{id}/README.txt`.

### Quality control

Explore data files and validate integrity. Check for:

- Consistent column names and data types across files
- Unexpected missing values or encoding issues
- Value range outliers
- Filename/folder naming consistency
- Typos in column/sheet names (fix when found)
- Inconsistent site spelling, date formatting, or extension casing
- Placeholder/template values that look like real observations
- Truncated or suspiciously short sensor files
- Missing spatial metadata or broken links between instrument files and GPS/linkage files
- Repeated data blocks or other format quirks that must be documented for reuse

Save QC report to `datasets/{id}/artifacts/qc_report.md`.
