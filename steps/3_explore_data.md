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

## Scope dimensions to extract from files

For each dimension, extract file-derived values and compare against the literature-derived values from `research.md` (marked `literature-derived` there). Note any discrepancies.

### Spatial
- Distinct site names as they appear in the data (column values, folder names, filenames)
- Coordinates from GNSS files or coordinate columns: compute bounding box (min/max lat, lon), note CRS
- Elevation range (min, max) from elevation columns or GNSS data
- Cross-check against literature site table in `research.md`; flag any site names or coordinates that differ

### Temporal
- Actual date range from date columns or filenames (not metadata claims — read the data)
- Collection periods: contiguous date blocks, gaps, multi-day or multi-season structure
- Any timestamps outside the expected range (potential out-of-scope records)

### Measurement domain
- Radiometric or spectral range (wavelength, frequency/bandwidth for radar, bit depth for imagery)
- Depth or vertical extent (snow depth, pit depth, altitude AGL)
- Taxonomic scope (species or functional groups, if biological data is present)
- Any other domain-specific bounds relevant to reuse (e.g., temperature range of observations, slope angle range for snowpits)

### Notebook deliverable
The notebook must include a **scope summary section** with:
- A site table (site name, N records, coordinate range, elevation range, date range)
- A temporal coverage cell (date histogram or sorted unique dates per site)
- For spatial data: a simple map or bounding-box printout confirming file-derived extent

### METADATA.yaml update
After extracting bounding box and date range from files, update `datasets/{id}/METADATA.yaml` with confirmed values. If these differ from the provisional values set by Research (Step 2) or Scope Definition (Step 1), note the discrepancy in `data_exploration.md`.

## README alignment

The data exploration outputs should provide the file-derived facts needed for the FRDR README sections:

- Data & file overview
- Methodological information tied to actual stored formats
- Data-specific variable/codebook sections
- Missing-data and unit documentation

## Delegation

Consider parallelizing by file type group (e.g., Excel workbooks, CSVs, shapefiles, GNSS files) when the dataset is large enough to benefit. Each subagent inspects its file group and returns a structured summary (columns, types, ranges, missing values, encoding). The main agent assembles summaries into `data_exploration.md` and the consolidated notebook. Keep cross-file relationship analysis (e.g., linkage between instrument files and GPS files) in the main agent, since it requires outputs from multiple subagents.

## README stub-filling

As Explore Data produces the file inventory and structural summaries, update the corresponding `⚠️ [placeholder]` stubs in `datasets/{id}/README.txt` directly (Data & file overview, naming conventions, variable lists). Note each update in a `## README updates` section at the bottom of `data_exploration.md`. This keeps README.txt as the living scope document — no separate scope artifact.

## Outputs

- `notebooks/{id}_data_exploration.ipynb`
- `datasets/{id}/artifacts/data_exploration.md`
- Direct updates to `datasets/{id}/README.txt` stubs (file overview, naming conventions sections)
- Updates to `datasets/{id}/METADATA.yaml` (confirmed bounding box, confirmed date range)
