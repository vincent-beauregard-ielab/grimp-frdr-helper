# Rogers Pass Snow Profiles Data Exploration

## Scope and method

This summary was produced by inspecting the raw package under `datasets/rogers_pass_snow_profiles/raw_data/Rogers Pass March 2024-2025` with `pandas`, `openpyxl`, and `snowmicropyn`.

The goal here is not to clean or rename the files yet. It is to document what is actually present, how it is structured, and which facts are ready for the FRDR README.

## Inventory summary

### Scientific data and directly related mapping files

- `13` `.xlsx`
- `322` `.csv`
- `172` text files split into `166` lower-case `.txt` and `6` upper-case `.TXT`
- `79` `.pnt`
- `3` shapefile ZIP packages

### Context or support material mixed into the raw package

- `11` `.docx`
- `17` `.pdf`
- `25` HEIC images split across `.HEIC` and `.heic`

### Top-level folders

- `Jour 1 - Fidelity`
- `Jour 2 - Jim Bay`
- `Jour 3 - Hermit`
- `Jour 4 - Fidelity`
- `Jour 5 - Round Hill`
- `Jour 6 - RoundHill and Christiana Ridge`
- `AWP`
- `Bouffe et infos`

The day-based organization is useful for human navigation but means the FRDR README will need to explain relationships across folders by both `day` and `instrument`.

## File relationships

### Reference snowpit workbooks

There are `8` stratigraphy workbooks sharing the same structure:

- `StratiTemplate.xlsx` (blank template)
- `Jour 1 - Fidelity/Strati_20250301_fidelity.xlsx`
- `Jour 2 - Jim Bay/20250302_JimBay_StratiTemplate.xlsx`
- `Jour 3 - Hermit/20250303_Hermit.xlsx`
- `Jour 4 - Fidelity/20250304_StratiTemplate.xlsx`
- `Jour 5 - Round Hill/20250305_Strati.xlsx`
- `Jour 6 - RoundHill and Christiana Ridge/CRidge_Strati_20250306.xlsx`
- `Jour 6 - RoundHill and Christiana Ridge/Fidelity_Strati_20250306.xlsx`

These workbooks contain:

- `AVY profile`
- `Stability Tests`
- `Density`
- `IRIS`

They are the most complete source for manual snowpit documentation.

### Spatial-survey mapping files

These single-sheet workbooks and GNSS CSV files map IDs across instruments:

- `Jour 1 - Fidelity/Fidelity Radars and SMP/Radar Fidelity point information.xlsx`
- `Jour 2 - Jim Bay/Spatial Survey - SMP and Radar K/20250302_JimBayCornerSpatial.xlsx`
- `Jour 3 - Hermit/Spatial_Hermitt/20250303_HermitWX_RadarK.xlsx`
- `Jour 5 - Round Hill/Spatial Survey/Spatial Survey notes.xlsx`
- `Jour 1 - Fidelity/Fidelity Radars and SMP/Radar Fidelity.csv`
- `Jour 2 - Jim Bay/Spatial Survey - SMP and Radar K/jimbaycorner_01032025.csv`
- `Jour 5 - Round Hill/Spatial Survey/GPS information/ROUND HILL.csv`

These files are essential for explaining which SMP, radar, SnowScope, and GPS records belong together.

### Instrument subtypes found in the raw package

- SnowScope profile CSV exports: `319`
- GNSS CSV exports: `3`
- Radar text exports in `radar_k` / `radar_ka`: `164`
- IRIS plain-text exports: `6`
- SMP binary profiles: `79`

## Data type findings

## 1. Stratigraphy workbooks (`.xlsx`)

### Common structure

Filled stratigraphy workbooks consistently use four sheets:

- `AVY profile`
- `Stability Tests`
- `Density`
- `IRIS`

This is the core codebook structure for the manual snowpit portion of the dataset.

### `AVY profile`

Observed fields include:

- date
- time
- elevation
- aspect
- incline
- location
- sky
- precip
- wind
- layered snowpit rows with `HEIGHT`, `RESISTANCE`, `FORM`, `EXTENT`, `Ѳ (LWC)`, `WEIGHT`, `DENSITY`, and comments
- temperature rows such as `AIR`, `SURFACE`, and successive depth labels

Observed reference profile locations and metadata:

- 2025-03-01, `Fidelity full profile`, elevation `1875`
- 2025-03-02, `Jim Bay Corner`, elevation `1889`, aspect `ESE`, incline `27`
- 2025-03-03, `Hermit wx station`, elevation `1950`, aspect `E`, incline `23`
- 2025-03-04, `Fidelity study plot`, elevation `1875`, aspect `N`, incline `flat`
- 2025-03-05, `Round Hill spatial survey`, elevation `2051`, aspect `N`
- 2025-03-06, `Christiania Ridge`, elevation `2088`, aspect `N`, incline `30`

### `Stability Tests`

Columns are consistent:

- `Test`
- `Score`
- `Grain Type`
- `Down`
- `Facture Char,`
- `Comments`

Observed content:

- some files are empty
- others include `CT`, `ECT`, and score strings such as `CTE5`, `ECTN23`, `H23`, `M14`
- comments reference buried weak layers or dates such as `Jan 30th`

### `Density`

Typical columns:

- `Height` or `Heigh`
- `Weight (g)`
- `Density (kg.m³)`

Findings:

- nominal sheet shape is around `61` rows
- density values are numeric when populated
- observed density ranges across filled workbooks run from `76` to `472 kg.m-3`
- many rows alternate between a height row and a weight / density row
- some `0` values appear in otherwise empty template-like rows, so zero is not always a true physical observation

### `IRIS`

Typical columns:

- `Version`
- `Spectralon (%)`
- `Calibration Voltage 1 (V)`
- `Calibration Voltage 2 (V)`
- `Calibration Voltage 3 (V)`
- `Height (cm)`
- `Scan 1 (V)`
- `Scan 2 (V)`
- `Scan 3 (V)`
- `Reflectance (%)`
- `SSA (m².kg-1)`
- `Ropt (mm)`
- field-note columns

Findings:

- sheet sizes vary from `9` to `24` rows
- calibration rows often use Spectralon references `99`, `60`, `40`, `20`, and `5`
- many cells are blank in partially completed workbooks
- `IRIS_1` and `IRIS_2` both appear in the `Version` field

### Missing values and formatting issues

- blanks dominate in template or partially filled rows
- some files use `0` in density template rows
- the day 6 Fidelity workbook has a likely date typo: `202500306`
- location spelling is inconsistent: `Christiana` / `Christiania`
- folder naming is inconsistent: `Round Hill` / `RoundHill`

## 2. SnowScope profile CSVs (`319` files)

### Structure

SnowScope files are not flat CSV tables. They contain:

1. a `GENERAL INFO` key-value block
2. a `SCOPE PROFILE` key-value block
3. a profile table beginning at:
   - `depth (mm),hardness (kPa),optical Reflectance Avg`, or
   - `depth (mm),hardness (kPa),`

### Metadata fields observed

- `elevation (m)`
- `profilePrivacy`
- `collectionTime`
- `collectionTime (Unix Time)`
- `creator name`
- `Location`
- `testNum`
- `serialNum`
- `profileDepth (mm)`
- `batteryCapacity`
- `errorCode`
- `temperature`
- `FW_version`
- `PCB_version`

### Consistency

- file count inspected: `319`
- creator name is always `Francis Gauthier`
- firmware version is always `2.4.1`
- error code is always `0`
- serial numbers present: `00304`, `00322`, `00328`

### Variable ranges

- `depth (mm)`: `1` to `2266`
- `hardness (kPa)`: `0.0` to `579.23`
- `profileDepth (mm)` metadata: `81` to `2266`

### Optical reflectance availability

- SN00328 files include numeric `optical Reflectance Avg`
- SN00322 files retain a third column but use literal `null`
- across all parsed rows:
  - rows with numeric optical reflectance: `334762`
  - rows with missing optical reflectance: `268342`

### Geographic coverage

- files with valid `Location`: `311`
- files with missing `Location`: `8`
- latitude range from file metadata: `51.2341198` to `51.3236271`
- longitude range from file metadata: `-117.7132470` to `-117.5314499`

### Missing-value encoding

- blank lines between metadata and profile table
- literal `null` in metadata and optical-reflectance field

## 3. GNSS CSV exports (`3` files)

These are ordinary tabular CSV files with `37` columns such as:

- `Name`
- `Description`
- `Longitude`
- `Latitude`
- `Ellipsoidal height`
- RTK quality metrics
- satellite counts
- timestamps

Observed row counts:

- `Radar Fidelity.csv`: `18`
- `jimbaycorner_01032025.csv`: `22`
- `ROUND HILL.csv`: `43`

These files are critical for geolocating radar, SMP, and SnowScope measurements because the `.pnt` files themselves do not carry usable coordinates.

## 4. Radar text exports (`164` files)

### Folder variants

- `radar_k`
- `radar_ka`
- one small `Jour 4 - Fidelity/Radar K` folder with two readme-linked measurements

### Header metadata

All parsed radar files share the same metadata values:

- start frequency: `23500 MHz`
- stop frequency: `26000 MHz`
- ramp time: `1 ms`
- number of samples: `513`
- zero pad factor: `4`
- active channels: `I1, Q1, I2, Q2`
- `Tic = 14991`

### Table structure

Each file contains repeated blocks beginning with:

- `X (m), I1, Q1, I2, Q2`

Every parsed radar file contains:

- `5` repeated table blocks
- `513` rows per block
- `2565` numeric rows total per file

Observed variable ranges across all parsed rows:

- `X (m)`: `0.0` to `7.675392`
- `I1`: `0` to `77093910`
- `Q1`: `83` to `74822123`
- `I2`: `69` to `66754050`
- `Q2`: `56` to `66329455`

### Important note

The header says `Number of Samples: 513`, but the stored files actually contain five repeated `513`-row blocks. The README should explain this explicitly because a naive reader will otherwise assume a single sweep per file.

## 5. IRIS plain-text exports (`6` files)

Plain-text IRIS files appear as two-column time series:

- time string, then
- numeric value

Examples:

- `13:47:26, 0.815`
- `15:13:36, 1.985`

Findings:

- file count: `6`
- row counts per file: `52` to `92`
- numeric value range: `0.006` to `2.002`

These exports are much less self-describing than the workbook `IRIS` sheets, so both forms should be documented together in the README.

## 6. SMP binary profiles (`79` files)

Parsed with `snowmicropyn`.

Findings:

- profile count: `79`
- nontrivial sample-count range: `16423` to `411400`
- one likely bad / truncated file has only `3` samples:
  - `Jour 5 - Round Hill/Spatial Survey/SMP/S35M0196.pnt`
- maximum distance range across files: `0.0083` to `1699.996 mm`
- maximum force range across files: `0.0269` to `41.9168 N`

Coordinate metadata issue:

- all parsed `.pnt` files resolve to missing or invalid latitude / longitude in `snowmicropyn`
- spatial linkage must therefore come from the companion GPS files and survey-note workbooks

## 7. Shapefile ZIPs (`3` files)

Observed files:

- `Jour 1 - Fidelity/Fidelity Radars and SMP/Radar Fidelity.shp.zip`
- `Jour 2 - Jim Bay/Spatial Survey - SMP and Radar K/jimbaycorner_01032025.shp.zip`
- `Jour 5 - Round Hill/Spatial Survey/GPS information/ROUND HILL.shp.zip`

These are strong candidates for ancillary spatial data in the FRDR package.

## 8. Support and administrative material

Mixed into the raw tree but likely not core data:

- AWP permit PDFs
- meal-planning workbook in `Bouffe et infos`
- parking reservation PDF
- HEIC field photos
- day-level readme/docx notes

Some of the docx notes are scientifically useful because they explain the number of points collected and the relationship between instruments. They should at least be mined for README text even if they are not deposited.

## Naming and consistency issues

QC-relevant issues found during exploration:

- `Round Hill` vs `RoundHill`
- `Christiana` vs `Christiania`
- mixed `.txt` and `.TXT`
- mixed `.HEIC` and `.heic`
- `Fidelity_Strati_20250306.xlsx` likely contains mistyped date `202500306`
- some workbook columns vary slightly, for example `Height` vs `Heigh`
- many SnowScope CSVs use `null` literals instead of empty cells
- radar files contain repeated table blocks not obvious from the header

## README-ready conclusions

The FRDR README can already document:

- the campaign date range and site list
- the main instrument families
- the raw package structure by day and by data type
- workbook sheet structure and the main variable groups
- SnowScope metadata fields, hardness units, and optional optical-reflectance field
- radar file header fields and the repeated-block structure
- IRIS text-export structure
- SMP binary dependency on `snowmicropyn`
- the need to use companion GPS files for spatial linkage

Still needing owner confirmation rather than more file parsing:

- which support files should be deposited
- final authoritative site spellings
- whether Ka-band and K-band should be described as distinct instruments or as folder-level naming
- whether any of the raw formats will be normalized before FRDR deposit
