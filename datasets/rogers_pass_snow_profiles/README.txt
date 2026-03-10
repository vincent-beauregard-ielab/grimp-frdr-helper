This README.txt file was generated on 2026-03-09 by Codex

--------------------
GENERAL INFORMATION
--------------------

1. Title of Dataset:

Pending owner confirmation.
Working title: Rogers Pass snow profiles and spatial snow-property surveys, British Columbia, Canada, March 2025

2. Author Information
	A. Principal Investigator Contact Information
		Name: Pending owner confirmation
		Institution: Pending owner confirmation
		Email: Pending owner confirmation

	B. Associate or Co-investigator Contact Information
		Name: Jean-Benoit Madore
		Institution: Universite de Sherbrooke / GRIMP
		Email: Pending owner confirmation

		Name: Alexandre Langlois
		Institution: Universite de Sherbrooke / GRIMP
		Email: Pending owner confirmation

		Name: Benjamin Imbach
		Institution: Universite du Quebec a Rimouski
		Email: Pending owner confirmation

Additional author order, contributor list, and any Parks Canada attribution remain pending owner confirmation.

3. Date of data collection (single date, range, approximate date):

2025-03-01 to 2025-03-06

4. Geographic location of data collection:

Rogers Pass region, British Columbia, Canada, including Fidelity, Jim Bay Corner, Hermit weather station, Round Hill, and Christiania Ridge.
Verified SnowScope coordinates span about 51.2341198 to 51.3236271 latitude and -117.7132470 to -117.5314499 longitude.

5. Information about funding sources that supported the collection of the data:

Pending owner confirmation. Local files link the campaign to GRIMP snow and avalanche research, but no deposit-ready funding wording was confirmed.

---------------------------
SHARING/ACCESS INFORMATION
---------------------------

1. Licenses/restrictions placed on the data:

Pending owner confirmation.

2. Links to publications that cite or use the data:

No dataset-specific publication was confirmed from local files as of 2026-03-09.
Related methodology sources include the local Madore PhD thesis and Pomerleau et al. 2020, Sensors, https://doi.org/10.3390/s20143909

3. Links/relationships to ancillary data sets or software packages:

- Reference FRDR dataset in `datasets/example/`, DOI 10.20383/103.01523
- OGRS 2024: https://www.avalancheassociation.ca/resource/resmgr/docs/ogrs/ogrs2024web.pdf
- CAAML context: https://caaml.org/Schemas/SnowProfileIACS/
- `snowmicropyn` for `.pnt` reuse

5. Was data derived from another source? yes/no

No. This package contains direct field observations plus supporting linkage files.

	A. If yes, list source(s):

Not applicable.

6. Recommended citation for this dataset:

Pending owner confirmation and DOI assignment.
Draft form: Author list pending. (2025). Rogers Pass snow profiles and spatial snow-property surveys, British Columbia, Canada, March 2025. Federated Research Data Repository. doi: pending

---------------------
DATA & FILE OVERVIEW
---------------------

1. File List

The proposed deposit should preserve the day-based folder structure because the raw package is organized by field day rather than by instrument.

   A. Filename: Jour 1 - Fidelity/
      Short description: Reference snowpit workbook, IRIS text export, Fidelity fixed-site SMP support files, and Jim Bay Corner spatial survey subfolders with SnowScope, SMP, and radar data.

   B. Filename: Jour 2 - Jim Bay/
      Short description: Reference snowpit workbook, IRIS text export, linkage workbook, GNSS CSV, shapefile ZIP, and spatial survey radar and SMP folders.

   C. Filename: Jour 3 - Hermit/
      Short description: Reference snowpit workbook, IRIS text export, linkage workbook, SnowScope folder, and radar folder.

   D. Filename: Jour 4 - Fidelity/
      Short description: Reference snowpit workbook, IRIS text export, two radar text exports, and radar field notes.

   E. Filename: Jour 5 - Round Hill/
      Short description: Reference snowpit workbook, IRIS text export, spatial survey workbook, GNSS CSV, shapefile ZIP, SMP folder, SnowScope folder, and radar_ka folder.

   F. Filename: Jour 6 - RoundHill and Christiana Ridge/
      Short description: Two snowpit workbooks, one IRIS text export, one SMP folder, and one SnowScope spatial-survey folder.

   G. Filename: README.txt
      Short description: FRDR documentation for package scope, file relationships, methods, standards, and QC notes.

2. Relationship between files, if important:

- Snowpit workbooks are the reference records for each day and contain the most complete manual observations.
- SnowScope CSVs, SMP `.pnt` files, radar text exports, and IRIS `.TXT` files are the instrument outputs for fixed-site or spatial-survey measurements.
- GNSS CSVs and linkage workbooks connect radar, SMP, SnowScope, and profile locations and are required because `.pnt` files do not carry usable coordinates.
- Shapefile ZIPs are companion spatial files for the GNSS outputs and are best treated as ancillary support.

3. Additional related data collected that was not included in the current data package:

Recommended for exclusion unless the owner requests a broader archival package:

- AWP permit PDFs
- logistics workbook in `Bouffe et infos/`
- parking reservation PDF
- campaign planning document
- morning hazard assessment PDFs
- HEIC field photos

4. Are there multiple versions of the dataset? yes/no

No deposited version exists yet in this repository.

---------------------------
METHODOLOGICAL INFORMATION
---------------------------

1. Description of methods used for collection/generation of data:

This six-day Rogers Pass field campaign combined reference snowpit observations with lighter spatial surveys. The package includes manual snowpit records, density and stability observations, IRIS-based snow optical measurements, SnowScope hardness-depth profiles, SnowMicroPen penetration-force profiles, FMCW radar exports, and GNSS-based spatial linkage.

2. Methods for processing the data:

The repository currently holds the raw package plus inspection artifacts. Files have been inventoried and parsed for documentation, but the scientific files have not been normalized into a common open format.

3. Instrument- or software-specific information needed to interpret the data:

- Spreadsheet software or `openpyxl` / `pandas` is needed for `.xlsx`.
- SnowScope CSVs contain metadata sections followed by the profile table and should not be read as flat CSVs without preprocessing.
- `.pnt` files require `snowmicropyn` or equivalent tooling.
- Radar text exports contain header metadata plus five repeated 513-row data blocks per file.
- Standard GIS software can read the GNSS CSVs and shapefile ZIPs.

4. Standards and calibration information, if appropriate:

- OGRS provides the main manual-observation vocabulary context.
- CAAML is relevant as interoperability context, but this package is currently stored in raw workbook, CSV, text, and binary formats.
- IRIS worksheets contain calibration rows with Spectralon reference values.

5. Environmental/experimental conditions:

Late-winter alpine snow conditions in the Rogers Pass region at Fidelity, Jim Bay Corner, Hermit weather station, Round Hill, and Christiania Ridge.

6. Describe any quality-assurance procedures performed on the data:

QC in this repository included subtype-based inventory, workbook and text parsing, value-range checks, review of missing-value conventions, and identification of naming inconsistencies, placeholder rows, truncated files, and spatial-linkage constraints. See `artifacts/qc_report.md`.

7. People involved with sample collection, processing, analysis and/or submission:

Confirmed from local notes and metadata:
- Jean-Benoit Madore
- Alexandre Langlois
- Benjamin Imbach
- Francis Gauthier
- Violaine Paquette
- Francis Meloche
- Hans-Peter Marshall
- Joachim Meyer
- Julien Meloche

-----------------------------------------------------------------
DATA-SPECIFIC INFORMATION FOR: Stratigraphy workbooks (`.xlsx`)
-----------------------------------------------------------------

1. Number of variables:

Varies by sheet. Filled workbooks consistently contain `AVY profile`, `Stability Tests`, `Density`, and `IRIS`.

2. Number of cases/rows:

Seven filled field workbooks plus one blank template were identified. Density sheets are typically about 61 rows. IRIS sheets range about 9 to 24 rows.

3. Missing data codes:
        blank cell        not observed or not filled
        0                sometimes a template placeholder in density rows

4. Variable List:

    A. Name: AVY profile fields
       Description: Date, time, elevation, aspect, incline, location, weather, layered snowpit rows, and temperature rows.

    B. Name: Stability test fields
       Description: Test type, score, grain type, depth-related fields, and comments.

    C. Name: Density fields
       Description: Height, weight, and density columns.

    D. Name: IRIS fields
       Description: Calibration voltages, reflectance, SSA, Ropt, height, and note fields.

-----------------------------------------------------------------
DATA-SPECIFIC INFORMATION FOR: SnowScope profile exports (`.csv`)
-----------------------------------------------------------------

1. Number of variables:

Common metadata fields include `elevation (m)`, `collectionTime`, `creator name`, `Location`, `testNum`, `serialNum`, `profileDepth (mm)`, `errorCode`, `temperature`, `FW_version`, and `PCB_version`. The profile table uses `depth (mm)`, `hardness (kPa)`, and sometimes `optical Reflectance Avg`.

2. Number of cases/rows:

319 files. Observed `profileDepth (mm)` ranges from 81 to 2266.

3. Missing data codes:
        blank line        section separator
        null             missing metadata or missing optical reflectance

4. Variable List:

    A. Name: depth (mm)
       Description: Profile depth coordinate.

    B. Name: hardness (kPa)
       Description: Snow hardness output from SnowScope.

    C. Name: optical Reflectance Avg
       Description: Optional optical field; numeric in SN00328 files and `null` in SN00322 files.

    D. Name: serialNum / FW_version / errorCode
       Description: Device and acquisition metadata.

--------------------------------------------------------------------
DATA-SPECIFIC INFORMATION FOR: GNSS CSV exports and linkage workbooks
--------------------------------------------------------------------

1. Number of variables:

GNSS CSV exports contain 37 columns. Linkage workbooks vary by day because they act as survey notes and crosswalks between instrument identifiers.

2. Number of cases/rows:

GNSS CSV row counts:
- `Radar Fidelity.csv`: 18
- `jimbaycorner_01032025.csv`: 22
- `ROUND HILL.csv`: 43

3. Missing data codes:
        blank cell        no value entered

4. Variable List:

    A. Name: Name
       Description: Survey point identifier.

    B. Name: Longitude / Latitude
       Description: Geographic coordinates for linked observations.

    C. Name: Ellipsoidal height
       Description: Elevation-related coordinate field.

    D. Name: linkage workbook fields
       Description: Day-specific fields used to match radar, SMP, SnowScope, and survey-point identifiers.

----------------------------------------------------------
DATA-SPECIFIC INFORMATION FOR: IRIS text exports (`.TXT`)
----------------------------------------------------------

1. Number of variables:

2 columns: time string and numeric value.

2. Number of cases/rows:

6 files. Parsed row counts range from 52 to 92.

3. Missing data codes:
        none explicitly observed

4. Variable List:

    A. Name: time
       Description: Time-of-day string for each IRIS record.

    B. Name: value
       Description: Numeric IRIS output value.

---------------------------------------------------------------
DATA-SPECIFIC INFORMATION FOR: Radar text exports (`.txt/.TXT`)
---------------------------------------------------------------

1. Number of variables:

Header metadata plus five numeric columns: `X (m)`, `I1`, `Q1`, `I2`, `Q2`.

2. Number of cases/rows:

164 files. Each contains 5 repeated blocks of 513 numeric rows.

3. Missing data codes:
        none explicitly observed

4. Variable List:

    A. Name: X (m)
       Description: Distance axis.

    B. Name: I1 / Q1
       Description: First radar channel pair.

    C. Name: I2 / Q2
       Description: Second radar channel pair.

    D. Name: header settings
       Description: Start and stop frequency, ramp time, sample count, zero pad factor, active channels, and tic value.

----------------------------------------------------------
DATA-SPECIFIC INFORMATION FOR: SnowMicroPen profiles (`.pnt`)
----------------------------------------------------------

1. Number of variables:

Binary format interpreted through `snowmicropyn` or equivalent tooling.

2. Number of cases/rows:

79 profiles. One likely truncated file, `Jour 5 - Round Hill/Spatial Survey/SMP/S35M0196.pnt`, contains only 3 samples.

3. Missing data codes:
        invalid or missing coordinate metadata        use GNSS CSVs and linkage workbooks instead

4. Variable List:

    A. Name: distance
       Description: Penetration distance in the snow profile.

    B. Name: force
       Description: Penetration force.

    C. Name: coordinate metadata
       Description: Not reliable in this package.
