# Data Exploration: Rogers Pass Snow Profiles

**Date:** 2026-03-11
**Notebook:** `datasets/rogers_pass_snow_profiles/notebooks/data_exploration.ipynb`

## 1. File Inventory

Total: **642 files**, **166.9 MB**

| Extension | Count | Size (MB) | Description |
|-----------|-------|-----------|-------------|
| .csv | 322 | 10.03 | SnowScope profiles + GPS exports |
| .txt | 172 | 17.83 | K-band radar (166) + IRIS (6) |
| .pnt | 79 | 62.35 | SMP binary profiles |
| .heic | 25 | 70.32 | Field photos (out of scope) |
| .pdf | 17 | 3.92 | Hazard assessments (6) + AWP permits (9) + other (2) |
| .xlsx | 13 | 2.10 | Stratigraphy (7) + spatial linkage (4) + other (2) |
| .docx | 11 | 0.37 | Site ReadMes (6) + SMP/radar ReadMes (2) + planning (3) |
| .zip | 3 | 0.01 | Zipped shapefiles |

## 2. Snow Stratigraphy XLSX (StratiTemplate)

**Files:** 7 workbooks (one per site-day, except Jour 6 has two: Christiana Ridge + Fidelity)
**Software:** openpyxl, pandas

Each workbook has 4 sheets (1000 rows x 26 cols per sheet template):

### Sheet: AVY profile
- **Structure:** Header rows 0-4 with site metadata; data starts row 5-6
- **Header fields:** DATE, TIME, ELEVATION, ASPECT, INCLINE, FOOTPEN, ORG, OBSERVER, TYPE, SKY, PRECIP, WIND, LOCATION, SITE CARACT./OBJECTIVES
- **Data columns:** HEIGHT (cm), RESISTANCE (hand hardness code), FORM (grain type code), EXTENT (grain size mm), LWC, WEIGHT, DENSITY, COMMENTS, TEMPERATURE (H, T, M, D sub-columns)
- **Grain type codes observed:** RG, MFcl, SH, DH, FC, DF, PPgp, FCxr, RGxf, IFsc, MFpc, PP, RGlr
- **Hardness codes:** F, 4F, 1F, P, K, I (standard hand hardness)
- **Elevations:** 1875-2088 m
- **Sites:** Fidelity full profile, Fidelity study plot, Jim Bay Corner, Hermit wx station, Round Hill spatial survey, Christiania Ridge, FIDELITY (Day 6)
- **Missing values:** Empty cells (None), many trailing empty rows in template

### Sheet: Stability Tests
- **Columns:** Test, Score, Grain Type, Down (cm), Fracture Char, Comments
- **Test types:** CT (Compression Test), ECT (Extended Column Test)
- **Score format:** CTE5, CTM18, CTH24, ECTN23, etc.
- **Fracture characters:** SP, RP, BRK, PC

### Sheet: Density
- **Columns:** Height (cm), Weight (g), Density (kg/m3)
- **Notes:** Formula references ("Couteau 250CC * 4", "Couteau 100CC * 10")
- **Missing:** Some density values are 0 (likely missing, not actual zero)

### Sheet: IRIS
- **Columns:** Version, Spectralon (%), Calibration Voltage 1-3 (V), Height (cm), Scan 1-3 (V), Reflectance (%), SSA (m2/kg), Ropt (mm), Field Notes
- **Versions observed:** IRIS_1, IRIS_2
- **Note:** Most IRIS sheets have only calibration data and Height/Scan 1 populated; Reflectance, SSA, Ropt columns are empty (computed post-processing needed)

## 3. IRIS TXT Files

**Files:** 6 (one per field day)
**Format:** Comma-separated, no header, two columns: `time (HH:MM:SS), value (float)`
**Encoding:** UTF-8
**Software:** pandas

| File | Day | Lines |
|------|-----|-------|
| IRIS_20250301.TXT | 2025-03-01 | 92 |
| 20250302.TXT | 2025-03-02 | varies |
| 20250303.TXT | 2025-03-03 | varies |
| 20250304.TXT | 2025-03-04 | varies |
| 20250305.TXT | 2025-03-05 | varies |
| 20250306.TXT | 2025-03-06 | varies |

- **Value range:** 0.118 to 1.988 (for Day 1 sample; represents voltage readings)
- **Missing values:** None observed
- **Note:** IRIS_20250301.TXT.docx companion document exists in Jour 1
- **Naming inconsistency:** Day 1 uses `IRIS_YYYYMMDD.TXT`, Days 2-6 use `YYYYMMDD.TXT`

## 4. SMP Binary .pnt Files (SnowMicroPen)

**Files:** 79 total
**Format:** Binary (SLF SnowMicroPenetrometer format)
**Software:** snowmicropyn (v1.2+)

| Day | Site | Count | Serial Range |
|-----|------|-------|-------------|
| Jour 1 - Fidelity | Fidelity | 4 | S35M0129-0132 |
| Jour 2 - Jim Bay | Jim Bay Corner | 18 | S35M0133-0150 |
| Jour 5 - Round Hill | Round Hill | 46 | S35M0151-0197 |
| Jour 6 - Christiana Ridge | Christiana Ridge | 11 | S35M0198-0208 |

- **SMP serial:** All serial 35 (single instrument)
- **Columns:** distance (mm), force (N)
- **Distance range:** 0 to 1700 mm
- **Force range:** 0.02 to 41.92 N
- **Samples per profile:** 3 to 411,400 (most ~400,000)
- **GPS coordinates:** Embedded in some files; 7 files have invalid GPS (-99999 sentinel)
- **Lat range (valid):** 51.234257 to 51.236523
- **Lon range (valid):** -117.707436 to -117.698845
- **Missing data:** No NaN in force values; some files have very few samples (likely aborted measurements)

## 5. SnowScope CSV Profiles

**Files:** 319 total (exported from SnowScope app)
**Format:** CSV with metadata header + depth-resolved data
**Encoding:** UTF-8
**Software:** pandas

| Directory | Day/Site | Count | Serial |
|-----------|----------|-------|--------|
| SS_SMP_20250301 | Jour 1 Jim Bay Corner | 8 | SN00328 |
| SS_SS1_20250301 | Jour 1 Jim Bay Corner | 43 | SN00328 |
| SS_SS2_hermitt_20250303 | Jour 3 Hermit | 59 | SN00328 |
| SS_SN322_20250306 | Jour 5 Round Hill | 98 | SN00322 |
| SS4_christridge_20240306 | Jour 6 Christiana Ridge | 111 | SN00322 + SN00304 |

### Metadata header (21 fields)
Key fields: `name`, `elevation (m)`, `collectionTime`, `collectionTime (Unix Time)`, `creator name`, `Location` (lat,lon), `serialNum`, `profileDepth (mm)`, `FW_version`, `PCB_version`, `temperature`

- **Creator:** Francis Gauthier (all files)
- **Serial numbers:** 00304, 00322, 00328 (3 SnowScope instruments)
- **Firmware:** 2.4.1
- **PCB:** v2.7

### Data section
- **Columns:** `depth (mm)`, `hardness (kPa)`, `optical Reflectance Avg` (optional)
- **181 files** have optical reflectance; **138 files** lack it
- **Profile depths:** 81 to 2266 mm
- **Hardness range:** ~1-337 kPa
- **Optical reflectance range:** 688-2277 (arbitrary units)
- **Missing values:** `null` string in metadata fields; no NaN in data columns

### Bounding box from SnowScope GPS
- **Lat:** 51.234120 to 51.323627
- **Lon:** -117.713247 to -117.531450

## 6. K-band Radar TXT Files

**Files:** 166 total
**Format:** Text with metadata header + comma-separated I/Q data
**Encoding:** UTF-8
**Software:** pandas

| Day | Site | Count |
|-----|------|-------|
| Jour 1 | Jim Bay Corner (spatial) | 50 |
| Jour 2 | Jim Bay Corner | 42 |
| Jour 3 | Hermit | 28 |
| Jour 4 | Fidelity | 2 |
| Jour 5 | Round Hill | 44 |

### Header metadata
- **Radar No.:** 2010000058 (single instrument)
- **Start-Frequency:** 23500 MHz
- **Stop-Frequency:** 26000 MHz (Ka-band, 23.5-26 GHz)
- **Ramp Time:** 1 ms
- **Number of Samples:** 513
- **Zero Pad Factor:** 4
- **Active Channels:** I1, Q1, I2, Q2
- **Dates:** 2025-03-01 through 2025-03-05

### Data section
- **Columns:** X (m), I1, Q1, I2, Q2
- **Rows per file:** 2565 (consistent)
- **X range:** 0.0 to 7.675 m
- **I/Q values:** Integer-scale (range ~1000 to ~38 million)
- **Missing values:** None in parsed data; some files have trailing incomplete lines

**Note:** No radar files for Day 6 (Christiana Ridge).

## 7. Radar & Spatial Summary XLSX

**Files:** 4 linkage workbooks mapping measurement point numbers to instrument file IDs and GPS rover points

| File | Site | Rows | Key columns |
|------|------|------|-------------|
| Radar Fidelity point information.xlsx | Fidelity Day 1 | 13 | Mesure #, SMP, Radar, Snowscope Minute |
| 20250302_JimBayCornerSpatial.xlsx | Jim Bay Day 2 | 18 | Measure Number, Rover Number, Radar with/without surface, SMP |
| 20250303_HermitWX_RadarK.xlsx | Hermit Day 3 | 30 | POINT GNSS, LATITUDE, LONGITUDE, ELEVATION |
| Spatial Survey notes.xlsx | Round Hill Day 5 | 48 | #, GPS, Ku, K, SMP, SS |

These are critical linkage tables connecting GPS point IDs to radar file numbers, SMP measurement numbers, and SnowScope profile numbers.

## 8. GPS/Spatial CSV and Shapefiles

### GPS CSV files (3 files, RTK survey export)
**37 columns** including: Name, Longitude, Latitude, Elevation, Ellipsoidal height, Solution status, Correction type, timestamps, satellite counts, RMS values

| File | Site | Points |
|------|------|--------|
| Radar Fidelity.csv | Fidelity Day 1 | 18 |
| jimbaycorner_01032025.csv | Jim Bay Day 2 | 18 |
| ROUND HILL.csv | Round Hill Day 5 | 46 |

- **Solution status:** FIX (RTK fixed solution)
- **Correction type:** RTK
- **Antenna height:** 1.934 m (consistent)
- **Coordinate system:** Global (WGS84)

### Shapefiles (3 zipped)
Each zip contains: Points.shp, Points.cpg, Points.dbf, Points.shx

## 9. Geographic Bounding Box

Combined from all GPS sources (RTK CSVs + SnowScope embedded GPS):

| Bound | Value |
|-------|-------|
| **North** | 51.323627 |
| **South** | 51.234087 |
| **East** | -117.531450 |
| **West** | -117.713247 |
| **Elevation** | 1838-2088 m |
| **Total GPS points** | 394 |

## 10. Hazard Assessment PDFs

**6 files** (one per day), 3-page PDFs with structured morning hazard assessment form:
- Weather observations (temperature, wind, HS, precipitation)
- Avalanche hazard assessment
- Links to weather stations (Fidelity, Rogers Pass, Round Hill, Abbott)

## 11. Site ReadMe DOCX Files

**6 files** with field notes per site-day:
- 4 daily site ReadMe files (~7.5 KB each)
- 1 SMP manipulation ReadMe (Fidelity)
- 1 radar readme (Day 4)

## 12. Support/Administrative Files (out of scope)

- **Bouffe et infos/** — Food/logistics spreadsheet
- **Planning DOCX** — Campaign planning document
- **Table of content Field Books.docx** — Field book index
- **YUL parking reservation.pdf** — Travel logistics
- **StratiTemplate.xlsx** — Blank template (reference)

## 13. File Relationships

```
Spatial Survey XLSX (linkage table)
  |-- maps GPS rover # --> GPS CSV point (Lat/Lon/Elev)
  |-- maps SMP # --> .pnt file (S35M0{SMP#}.pnt)
  |-- maps Radar # --> radar_k/{NNNN}YYYYMMDD_HHMM.txt
  |-- maps SnowScope minute --> SS CSV profile

Stratigraphy XLSX
  |-- IRIS sheet links to IRIS TXT file (same day)
  |-- AVY profile covers same pit as density + stability tests

SnowScope CSV
  |-- GPS location embedded in metadata header
  |-- serialNum links to physical instrument
  |-- profileDepth correlates with SMP measurements at same point
```

## Scope Updates

### 1. Day 6 Fidelity stratigraphy file
Jour 6 contains `Fidelity_Strati_20250306.xlsx` — a stratigraphy file for Fidelity on Day 6, which was planned for Round Hill and Christiana Ridge only. The file has DATE=202500306 (typo: extra zero), minimal data (empty Stability Tests, Density, IRIS sheets), OBSERVER=AL, JM. This may be a quick re-visit to Fidelity on the last day. **Action needed:** Confirm with researcher whether this is a real observation or a mis-filed/duplicate workbook.

### 2. IRIS file naming inconsistency
Day 1 IRIS file is named `IRIS_20250301.TXT` while Days 2-6 use `YYYYMMDD.TXT` (without IRIS prefix). The IRIS data format is consistent (time, value pairs).

### 3. Hermit stratigraphy quality note
The Hermit Day 3 stratigraphy file contains the note "NOTE...THIS PROFIL IS NOT GOOD" in the SITE CARACT field. This should be documented in the README.

### 4. Ka-band radar inconsistency (Day 5)
Day 5 radar files are in a directory named `radar_ka` (not `radar_k`), suggesting these may be Ka-band rather than K-band, or the naming is inconsistent. The file format and frequency range (23.5-26 GHz) are identical. **Action needed:** Confirm frequency band designation.

### 5. No radar data for Day 6
No K-band/Ka-band radar files exist for Day 6 (Christiana Ridge). The spatial survey for Day 6 contains only SnowScope CSVs.

### 6. No GPS/shapefile for Days 3, 4, 6
RTK GPS exports (CSV + shapefile) exist only for Days 1, 2, and 5. Day 3 has coordinates embedded in its spatial XLSX. Days 4 and 6 have no standalone GPS files.

### 7. SMP data absent for Days 3 and 4
No .pnt files exist for Day 3 (Hermit) or Day 4 (Fidelity). Day 3 has SnowScope CSVs but no raw SMP binary profiles.

### 8. SnowScope location anomaly
The SnowScope GPS bounding box extends to lon=-117.531, which is significantly east of the other sites (centered around -117.70). This corresponds to the Hermit site (Jour 3) at lat~51.323, lon~-117.531, confirming Hermit is geographically distinct from the other sites.

### 9. Date in Christiana Ridge directory name
The directory `SS4_christridge_20240306` uses date 20240306 (2024) instead of 20250306 (2025). The actual data files inside have 2025 dates. This is a naming error in the directory.
