# Scope — Rogers Pass Snow Profiles

**Status:** Approved — pending Research and Explore Data steps
**Dataset id:** rogers_pass_snow_profiles

---

## Temporal extent

| | Date |
|---|---|
| Campaign | 2024–2025 winter season, intensive field campaign |
| Collection start | 2025-03-01 |
| Collection end | 2025-03-06 |

Data files carry dates 20250301–20250306 consistently across all measurement types.

---

## Spatial extent

**Study area:** Rogers Pass, Glacier National Park, British Columbia, Canada
**Collaboration partner:** Parks Canada (Glacier National Park avalanche program)

**Sites visited** (one or more per day):

| Day | Date | Site(s) |
|-----|------|---------|
| 1 | 2025-03-01 | Fidelity, Jim Bay Corner |
| 2 | 2025-03-02 | Jim Bay Corner |
| 3 | 2025-03-03 | Hermit |
| 4 | 2025-03-04 | Fidelity |
| 5 | 2025-03-05 | Round Hill |
| 6 | 2025-03-06 | Round Hill, Christiana Ridge |

Coordinate system: Geographic (decimal degrees, WGS84 assumed).
Precise bounding box TBD — to be extracted from shapefiles and GPS data in the Explore Data step.

---

## Measurements and variables

| Data type | Instrument / format | Files |
|-----------|-------------------|-------|
| Snow stratigraphy + density profiles | StratiTemplate (Excel) | 1 XLSX per site-day; 7 files total |
| IRIS infrared observations | IRIS sensor (TXT) | 1 TXT per field day; 6 files total |
| SnowMicroPenetrometer (SMP) | SMP probe (.pnt binary, .csv) | Multiple profiles per site-day |
| K-band radar transects | Compact K-band radar (TXT, CSV) | Spatial transects per site-day |
| Spatial surveys (SMP + radar) | GPS + tabular (XLSX, CSV, SHP) | Per-site transect data |
| Morning hazard assessments | Parks Canada / GRIMP (PDF) | 1 PDF per field day; 6 files total |
| Site-level ReadMe notes | Field notes (DOCX) | 1 DOCX per site-day |
| Field notebook photos | Camera (HEIC) | Multiple per site-day — **scope TBD** |

---

## Data boundaries

### In scope for deposit (confirmed)
- Snow stratigraphy XLSX files (StratiTemplate)
- IRIS TXT data files
- SMP .pnt files and derived CSV profiles
- K-band radar TXT/CSV measurement files
- Spatial survey XLSX, CSV, and zipped SHP files

### Tentatively in scope (pending researcher decision)
- Morning hazard assessment PDFs
- Site-level ReadMe DOCX files
- Spatial survey GPS/radar README files

### Out of scope (excluded)
- `Bouffe et infos/` — Field logistics
- `Table of content Field Books.docx` — Internal organizational document
- Field notebook HEIC photos — raw scans of handwritten notes; **researcher decision needed**

---

## Processing level

Files appear to be **raw as-collected** (field measurements, unprocessed instrument outputs). No processing pipeline has been observed in the raw_data directory. Confirm with researcher.

---

## Elicitation answers

| # | Question | Answer |
|---|----------|--------|
| 1 | Title | **Pending selection** — see recommended options in scope.md |
| 2 | IRIS instrument | Find from Research step |
| 3 | HEIC field notebook photos | Deferred |
| 4 | Morning hazard assessment PDFs | Deferred |
| 5 | License | **CC BY-NC 4.0** |
| 6 | Authors | Start with Madore, Langlois — full list from Research step |
| 7 | Processing level | **Raw as collected** |
| 8 | Parks Canada relationship | Find from Research step |
| 9 | Related to DOI 10.20383/103.01523 | **No — unrelated dataset** |
| 10 | Site ReadMe DOCXes | **Include** — convert to .txt at Data Preparation step |

## Title (confirmed)

`Snow profile observation datasets, Rogers Pass, Glacier National Park, British Columbia, Canada`

## Research sources

- `papers/madore_jean-benoit_PhD_2023.pdf` — primary reference for methodology, instruments, and field protocols

## Open items (deferred to Research step)

- Parks Canada relationship (collaborator / funder / data contributor) and licence implications
- Author list beyond Madore and Langlois — affiliations and ORCIDs
- Funding sources
- Data boundaries for HEIC field notebook photos and morning hazard assessment PDFs
- Output file structure and naming conventions for processed data files
