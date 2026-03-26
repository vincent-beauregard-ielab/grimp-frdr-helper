# Scope — Rogers Pass Snow Profiles

**Status:** Updated from Research and Explore Data — pending researcher review
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

### Confirmed sites

- Fidelity
- Jim Bay Corner
- Hermit
- Round Hill
- Christiana Ridge

### Bounding box from combined GPS sources

| Bound | Value |
|---|---|
| West | -117.713247 |
| East | -117.531450 |
| North | 51.323627 |
| South | 51.234087 |
| Elevation range | 1838-2088 m |

### Site/day coverage

| Day | Date | Site(s) |
|-----|------|---------|
| 1 | 2025-03-01 | Fidelity, Jim Bay Corner |
| 2 | 2025-03-02 | Jim Bay Corner |
| 3 | 2025-03-03 | Hermit |
| 4 | 2025-03-04 | Fidelity |
| 5 | 2025-03-05 | Round Hill |
| 6 | 2025-03-06 | Christiana Ridge; possible additional Fidelity revisit pending confirmation |

---

## Measurements and variables

| Data type | Instrument / format | Scope notes |
|---|---|---|
| Snow stratigraphy workbooks | StratiTemplate XLSX (7 files) | Layer height, grain type and size, hand hardness, wetness, density, temperature, stability tests |
| IRIS observations | TXT files (6 files) plus IRIS sheets in XLSX | Time/value observations used for snow specific surface area workflows |
| SnowMicroPenetrometer | `.pnt` binary profiles (79 files) | Distance and force measurements; present for Days 1, 2, 5, and 6 |
| SnowScope profiles | Snow Scope Probe (Propagation Labs) CSV exports (319 files) | Depth-resolved hardness with optional optical reflectance and embedded GPS |
| FMCW radar transects | TXT files (166 files) | 24 GHz class radar measurements with I/Q traces; no Day 6 radar files observed |
| Spatial linkage tables | XLSX (4 files) | Maps rover points to radar, SMP, and SnowScope measurements |
| GPS / spatial survey exports | CSV (3 files) and zipped shapefiles (3 files) | RTK point locations and elevations |
| Supporting field documentation | PDFs and DOCX files | Hazard assessments and site notes remain a boundary decision rather than core measurement data |

---

## Data boundaries

### In scope for deposit (confirmed)

- StratiTemplate snow stratigraphy workbooks
- IRIS TXT files
- SMP `.pnt` files
- SnowScope CSV exports
- FMCW radar measurement TXT files
- Spatial linkage XLSX workbooks
- RTK GPS CSV exports
- Zipped shapefile packages

### Pending researcher decision

- Morning hazard assessment PDFs
- Site-level ReadMe DOCX files and other field-note style documentation

### Out of scope

- HEIC field photos
- Food, logistics, travel, and planning documents
- Blank reference templates and other administrative support files

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
