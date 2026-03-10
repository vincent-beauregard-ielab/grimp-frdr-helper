# Explore Data Files

Inspect data files using pandas in a Jupyter notebook. Save the notebook to `notebooks/` with dataset name in filename and save a summary to `datasets/{id}/artifacts/data_exploration.md`.

**Autonomy:** Level 3 — Notebook output is inspectable, non-destructive.

**Parallel with:** Research. These two steps are independent and should run concurrently when possible.

## Approach

Inspect the dataset by real file subtype, not only by extension. For example, a single dataset may contain:

- reference snowpit workbooks
- mapping/linkage workbooks
- instrument exports (CSV, TXT, binary)
- GNSS point files
- shapefiles or zipped shapefiles
- context/support files mixed into raw data

## For each scientific file type, document

- Column names and data types
- Enum/categorical fields and their values
- Value ranges for numeric fields
- Missing value encoding (NA, NaN, empty string, sentinel values)
- Case uniformity across text fields
- File encoding and delimiter
- Row counts / record counts where applicable
- Relationships between files when one file maps measurement IDs to another
- Software or Python packages required to read the format

## Tooling

Use Python libraries (`pandas`, `openpyxl`, `pypdf`, `pdfplumber`, and format-specific parsers) for all data inspection so that every step is captured reproducibly in the notebook. Reserve document-creation skills (xlsx, pdf, docx) for producing output artifacts, not for reading data.

## README alignment

The data exploration outputs should provide the file-derived facts needed for the FRDR README sections:

- Data & file overview
- Methodological information tied to actual stored formats
- Data-specific variable/codebook sections
- Missing-data and unit documentation

## Delegation

Consider parallelizing by file type group (e.g., Excel workbooks, CSVs, shapefiles, GNSS files) when the dataset is large enough to benefit. Each subagent inspects its file group and returns a structured summary (columns, types, ranges, missing values, encoding). The main agent assembles summaries into `data_exploration.md` and the consolidated notebook. Keep cross-file relationship analysis (e.g., linkage between instrument files and GPS files) in the main agent, since it requires outputs from multiple subagents.

## Outputs

- `notebooks/{id}_data_exploration.ipynb`
- `datasets/{id}/artifacts/data_exploration.md`
