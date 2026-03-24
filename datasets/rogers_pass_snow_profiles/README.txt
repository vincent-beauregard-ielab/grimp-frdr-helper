This README.txt file was generated on 2026-03-24 by Codex

--------------------
GENERAL INFORMATION
--------------------

1. Title of Dataset:

Snow profile observation datasets, Rogers Pass, Glacier National Park, British Columbia, Canada

2. Author Information
    A. Principal Investigator Contact Information
        Name: Jean-Benoit Madore
        Institution: Universite de Sherbrooke, Department of Applied Geomatics; Centre d'etudes nordiques
        Email: jean-benoit.madore@usherbrooke.ca

    B. Associate or Co-investigator Contact Information
        Name: Alexandre Langlois
        Institution: Universite de Sherbrooke, Department of Applied Geomatics; GRIMP; Centre d'etudes nordiques
        Email: Pending researcher confirmation

        Additional field participants documented in the field notes include Benjamin Imbach, Francis Gauthier, Francis Meloche, Violaine Paquette, Kate Hale, Hans-Peter Marshall, Jo Meyer, and Julien Meloche. Final author list and author order are pending researcher confirmation.

3. Date of data collection (single date, range, approximate date):

2025-03-01 to 2025-03-06

4. Geographic location of data collection:

Rogers Pass, Glacier National Park, Selkirk Mountains, British Columbia, Canada.
Bounding box from the prepared package: north 51.323627, south 51.234087, east -117.531450, west -117.713247.
Elevation range represented by GPS and snow-profile metadata: 1832-2088 m.
Study sites represented in the prepared package are Fidelity, Jim Bay Corner, Hermit, Round Hill, and Christiana Ridge.

5. Information about funding sources that supported the collection of the data:

Pending researcher confirmation. Local project records indicate GRIMP / Universite de Sherbrooke support and likely MOACC-related infrastructure context, but no funder names or award numbers are confirmed in the repository.

---------------------------
SHARING/ACCESS INFORMATION
---------------------------

1. Licenses/restrictions placed on the data:

These data are prepared for release under the Creative Commons Attribution-NonCommercial 4.0 International (CC BY-NC 4.0) license:
https://creativecommons.org/licenses/by-nc/4.0/

2. Links to publications that cite or use the data:

- Madore, J.-B. (2023). Etude integree de la percolation de l'eau dans le manteau neigeux du Parc national des Glaciers, Colombie-Britannique, Canada. PhD thesis, Universite de Sherbrooke. Primary methodological reference for the Rogers Pass campaign.
- Imbach, B., Madore, J.-B., Jones, A., and Brown, C. (2025). Snow profile observation datasets, Glacier National Park, British Columbia, Canada. Federated Research Data Repository. https://doi.org/10.20383/103.01523
- Pomerleau, P. et al. (2020). Low cost and compact FMCW 24 GHz radar applications for snowpack and ice thickness measurements. Sensors. https://doi.org/10.3390/s20143909
- Montpetit, B. et al. (2012). New shortwave infrared albedo measurements for snow specific surface area retrieval. Journal of Glaciology. https://doi.org/10.3189/2012JoG11J248
- Schneebeli, M. and Johnson, J. B. (1998). A constant-speed penetrometer for high-resolution snow stratigraphy. Annals of Glaciology. https://doi.org/10.3189/1998AoG26-1-107-111
- Schneebeli, M., Pielmeier, C., and Johnson, J. B. (1999). Measuring snow microstructure and hardness using a high resolution penetrometer. Cold Regions Science and Technology. https://doi.org/10.1016/S0165-232X(99)00030-0
- Fierz, C. et al. (2009). The international classification for seasonal snow on the ground. UNESCO-IHP. https://unesdoc.unesco.org/ark:/48223/pf0000186462
- Bartelt, P. and Lehning, M. (2002). A physical SNOWPACK model for the Swiss avalanche warning: Part I: numerical model. Cold Regions Science and Technology. https://doi.org/10.1016/S0165-232X(02)00074-5

3. Links/relationships to ancillary data sets or software packages:

- This 2025 Rogers Pass package is not derived from the earlier FRDR CAAML deposit, but it is methodologically related to the earlier Glacier National Park dataset: https://doi.org/10.20383/103.01523
- `snowmicropyn` is recommended for reading `.pnt` files: https://pypi.org/project/snowmicropyn/
- `pandas` is recommended for `.csv` and `.txt` files: https://pandas.pydata.org/
- `openpyxl` is recommended for Excel workbook inspection in Python: https://openpyxl.readthedocs.io/
- QGIS can read shapefile ZIP contents after extraction: https://qgis.org/
- GeoPandas can read shapefiles in Python: https://geopandas.org/

5. Was data derived from another source? yes/no
    A. If yes, list source(s):

No. The deposit contains field-collected measurements and associated field documentation from the 2025 campaign.

6. Recommended citation for this dataset:

Madore, J.-B., Langlois, A., and collaborators (2026). Snow profile observation datasets, Rogers Pass, Glacier National Park, British Columbia, Canada. Federated Research Data Repository. DOI pending.

Pending researcher confirmation: final author list, publication year, and DOI.

---------------------
DATA & FILE OVERVIEW
---------------------

1. File List

   Naming convention:
   - Standardized folder names use `<datatype>/<YYYYMMDD>_<site>` or `<datatype>/<YYYYMMDD>_<site>_<content>`.
   - Standardized top-level file names use `<YYYYMMDD>_<site>_<content>.<ext>`.
   - Instrument-native file names inside bulk folders were preserved where they already encode acquisition identifiers, for example `s35m0151.pnt`, `2025-03-05_1738_Profile105_SN00322.csv`, or `054820250302_1554.txt`.

   A. Filename: snow_stratigraphy/
      Short description: Seven raw Excel workbooks containing manual snow-pit observations, one workbook per site-day. Representative files are `20250301_fidelity_stratigraphy.xlsx`, `20250303_hermit_stratigraphy.xlsx`, and `20250306_christiana_ridge_stratigraphy.xlsx`. Each workbook has four sheets: `AVY profile`, `Stability Tests`, `Density`, and `IRIS`.

   B. Filename: iris/
      Short description: Six daily IRIS raw text exports, renamed to `20250301_fidelity_iris_raw.txt` through `20250306_christiana_ridge_iris_raw.txt`. Each file is a two-column plain-text time series (`time`, `value`) used to support IRIS layer observations.

   C. Filename: snowmicropenetrometer/
      Short description: Four day-site folders containing 79 SnowMicroPenetrometer `.pnt` profiles. Folder names are `20250301_fidelity/`, `20250302_jim_bay_corner/`, `20250305_round_hill/`, and `20250306_christiana_ridge/`. Representative files are `s35m0129.pnt`, `s35m0150.pnt`, and `s35m0208.pnt`.

   D. Filename: snowscope/
      Short description: Five standardized SnowScope folder names containing 319 CSV profile files. Representative folders are `20250301_jim_bay_corner_snowscope/`, `20250305_round_hill_snowscope/`, and `20250306_christiana_ridge_snowscope/`. Representative files are `14-45_2025_3_1_Profile14_SN00328_.csv` and `2025-03-06_1649_Profile100_SN00304.csv`.

   E. Filename: radar/
      Short description: Five day-site folders containing 166 FMCW radar text exports. Representative folders are `20250302_jim_bay_corner/`, `20250304_fidelity/`, and `20250305_round_hill/`. Representative files are `052820250302_1505.txt`, `059820250304_1338.txt`, and `056720250302_1625.txt`. The Day 5 raw folder label `radar_ka` was standardized into the generic `radar/` deposit folder.

   F. Filename: spatial_reference/
      Short description: Ten support files that link measurements to coordinates. These include four linkage workbooks (`*_spatial_linkage.xlsx`), three RTK GPS CSV exports (`*_gps_points.csv`), and three zipped shapefile packages (`*_gps_points_shapefile.zip`).

   G. Filename: documentation/
      Short description: Eight field-note and instrument-note text files converted from DOCX to UTF-8 plain text. The contents remain in the original French. Representative files are `20250301_fidelity_jim_bay_corner_field_notes_fr.txt`, `20250304_fidelity_radar_notes_fr.txt`, and `20250306_round_hill_christiana_ridge_field_notes_fr.txt`.

2. Relationship between files, if important:

- Stratigraphy workbooks describe the reference snow pit at each site-day and provide manual layer, density, temperature, and stability-test observations.
- IRIS text files correspond to the same day/site snow-pit work and supply the raw sensor readings for IRIS measurements recorded in workbook `IRIS` sheets.
- SMP `.pnt` files, SnowScope CSV files, and radar TXT files capture spatial measurements near or around the reference snow-pit sites.
- Linkage workbooks in `spatial_reference/` connect radar measurement IDs, SMP IDs, rover/GPS point numbers, and SnowScope profiles.
- GPS CSV files and shapefile ZIPs provide point geometry for the spatial surveys.
- Documentation files explain field operations, site conditions, and instrument handling that are not obvious from the raw numeric files alone.

3. Additional related data collected that was not included in the current data package:

- Morning hazard assessment PDFs were left out of the prepared package pending researcher confirmation.
- HEIC field notebook photos were left out of the prepared package pending researcher confirmation.
- Administrative material such as logistics spreadsheets, planning documents, and travel files was excluded.
- A blank `StratiTemplate.xlsx` workbook and an `IRIS_20250301.TXT.docx` companion file were excluded because they do not add unique observed data to the deposit.

4. Are there multiple versions of the dataset? yes/no
    A. If yes, name of file(s) that was updated:
        i. Why was the file updated?
        ii. When was the file updated?

No. This README describes one prepared deposit package created from the raw campaign folder. The scientific files themselves were not numerically edited; only package structure and documentation format were standardized.

-----------------------
READING AND USING DATA
-----------------------

- `.xlsx` snow-pit and linkage workbooks can be opened in Microsoft Excel, LibreOffice Calc (https://www.libreoffice.org/), or read in Python with `openpyxl` / `pandas`.
- `.txt` IRIS files are simple comma-separated time/value pairs and can be read directly with `pandas.read_csv`.
- `.pnt` SMP files are proprietary SnowMicroPenetrometer binaries. Use `snowmicropyn` (https://pypi.org/project/snowmicropyn/) to access header metadata and the `distance` / `force` measurement table.
- SnowScope `.csv` files contain a metadata header block followed by a profile table beginning at the row `depth (mm),...`. Do not read them as a flat CSV without handling the header block first.
- Radar `.txt` files contain a metadata header followed by a five-column comma-separated table (`X (m), I1, Q1, I2, Q2`). Read the table only after the `X (m)` header row.
- GPS `.csv` files can be read with `pandas`; shapefile ZIPs should be extracted first and then read with QGIS or GeoPandas.
- Documentation `.txt` files preserve the original French field notes. No translation was applied during preparation.

---------------------------
METHODOLOGICAL INFORMATION
---------------------------

1. Description of methods used for collection/generation of data:

The deposit contains a six-day field campaign carried out from 2025-03-01 to 2025-03-06 at Fidelity, Jim Bay Corner, Hermit, Round Hill, and Christiana Ridge in Rogers Pass. Manual snow stratigraphy was recorded in StratiTemplate Excel workbooks using snow-pit protocols aligned with OGRS (Canadian Avalanche Association, 2016, Observation Guidelines and Recording Standards for Weather, Snowpack and Avalanches, https://cdn.ymaws.com/www.avalancheassociation.ca/resource/resmgr/standards_docs/ogrs2016web.pdf) and ICSSG (Fierz et al., 2009, The international classification for seasonal snow on the ground, https://unesdoc.unesco.org/ark:/48223/pf0000186462). These workbooks document layer height, grain form and size, hand hardness, liquid water content, density, and manual temperature observations.

IRIS measurements were collected alongside the snow pits using the InfraRed Integrating Sphere described by Montpetit et al. (2012, New shortwave infrared albedo measurements for snow specific surface area retrieval, https://doi.org/10.3189/2012JoG11J248). The raw exports in this package are time/value text files associated with the IRIS worksheet in each snow-pit workbook; the worksheets also preserve calibration-voltage fields and version labels (`IRIS_1` or `IRIS_2`) recorded in the field.

SnowMicroPenetrometer profiles were acquired with a constant-speed penetrometer following Schneebeli and Johnson (1998, https://doi.org/10.3189/1998AoG26-1-107-111) and Schneebeli et al. (1999, https://doi.org/10.1016/S0165-232X(99)00030-0). The instrument drives a 5 mm conical tip into the snow at approximately 20 mm/s and records penetration resistance at very high vertical resolution. This campaign collected 79 `.pnt` profiles across four site-days.

Compact 24 GHz FMCW radar measurements were collected along spatial transects using the radar architecture described by Pomerleau et al. (2020, Low cost and compact FMCW 24 GHz radar applications for snowpack and ice thickness measurements, https://doi.org/10.3390/s20143909). The raw files in this package preserve the original header metadata and the sampled I/Q signal table. The research notes describe the system as a K-band radar, while one raw folder uses the label `radar_ka`; that naming inconsistency is documented in the QC report rather than altered in the raw file content.

SnowScope observations were collected as depth-resolved hardness profiles with optional optical reflectance. The CSV header preserves device serial number, firmware version, PCB version, collection time, location, and profile depth. Linkage workbooks and RTK GPS exports were collected to georeference the radar, SMP, and SnowScope transects and to map acquisition point numbers to files.

CAAML is not used in this deposit; raw Excel, text, CSV, and binary files are preserved instead. The earlier FRDR Glacier National Park deposit used CAAML for interchange, while this package remains closer to the campaign source files. SNOWPACK is also not used directly in the deposit, but it is relevant background for the broader research program (Bartelt and Lehning, 2002, https://doi.org/10.1016/S0165-232X(02)00074-5).

2. Methods for processing the data:

Data preparation was intentionally non-destructive. Files were copied from `raw_data/` into `frdr_data/`, reorganized by data type, and renamed so the deposit uses stable English folder names and machine-readable date/site tokens. No numeric values were edited in the scientific files. The only content conversion performed during preparation was DOCX-to-TXT conversion for field and instrument notes so that ancillary documentation can be opened without proprietary software.

Specific preparation actions were:
- standardized deposit folder names and top-level filenames;
- normalized mixed-case extensions and inconsistent folder labels through the prepared-package names rather than source-file edits;
- converted 8 DOCX notes to UTF-8 plain text;
- excluded out-of-scope administrative files, photos, and unresolved hazard PDFs from the prepared package;
- preserved ambiguous raw-source issues, such as the Day 6 Fidelity revisit workbook and invalid SMP GPS sentinels, without altering source values.

3. Instrument- or software-specific information needed to interpret the data:

- StratiTemplate workbooks: multi-sheet Excel format; read with Excel, LibreOffice, `openpyxl`, or `pandas`.
- IRIS workbook sheets include instrument version labels `IRIS_1` / `IRIS_2`. Raw text exports are two-column plain text.
- SnowScope devices in this package use serial numbers 00304, 00322, 00328, firmware 2.4.1, and PCB version v2.7.
- SMP files require `snowmicropyn`; the campaign used one SMP serial family (35).
- Radar headers show radar number(s) 2010000058 and a frequency span of 23500-26000 MHz.
- GPS CSV files are RTK exports with `Latitude`, `Longitude`, `Elevation`, and quality fields such as solution status and correction type.

4. Standards and calibration information, if appropriate:

- Manual snow classification follows ICSSG grain classes and OGRS field conventions.
- IRIS sheets preserve field calibration voltages and reflectance/SSA placeholders recorded during acquisition.
- SnowScope files preserve device firmware and PCB metadata in the header block.
- GPS exports indicate RTK acquisition and should be treated as WGS84 geographic coordinates unless the researcher provides a more specific survey note.
- CAAML is referenced only as contextual interoperability background and is not a deposited file format in this package.

5. Environmental/experimental conditions:

The campaign covered five Rogers Pass sites between 1832 m and 2088 m elevation. SnowScope profile depths in the prepared package range from 81 mm to 2266 mm, and SMP profile depths extend to 1700 mm. Manual snow-pit temperature entries preserved in the workbooks span approximately -8.5 to 2.0 degrees C. The Hermit field notes and workbook metadata indicate that the Day 3 profile quality was poor and should be interpreted cautiously.

6. Describe any quality-assurance procedures performed on the data:

Quality assurance during preparation focused on packaging and interpretability rather than on altering scientific measurements. The prepared package:
- separates scientific files from administrative material;
- documents unresolved scope decisions and raw-source anomalies in `artifacts/qc_report.md`;
- standardizes folder names and filenames for deposit consistency;
- preserves raw instrument formats and numeric content;
- converts ancillary DOCX notes to plain text for accessibility.

7. People involved with sample collection, processing, analysis and/or submission:

Confirmed field participants in the site notes include Jean-Benoit Madore, Alexandre Langlois, Benjamin Imbach, Francis Gauthier, Francis Meloche, Violaine Paquette, Kate Hale, Hans-Peter Marshall, Jo Meyer, and Julien Meloche. Parks Canada staff are referenced in the notes as operational collaborators for site access and logistics. Pending researcher confirmation applies to final authorship, contact list, and funding wording.

-----------------------------------------------------------------
DATA-SPECIFIC INFORMATION FOR: snow_stratigraphy/
-----------------------------------------------------------------

1. Number of variables:
Four workbook sheets per file. The `AVY profile` sheet contains site metadata plus layer-by-layer snow observations; the `Stability Tests`, `Density`, and `IRIS` sheets contain supporting measurements.

2. Number of cases/rows:
7 workbook files. Active observation rows vary by snow pit and are embedded within 1000-row templates.

3. Missing data codes:
        blank cell        No value recorded in the field template
        0                In some density columns, likely placeholder or missing entry rather than a true zero

4. Variable List:
    A. Name: DATE / TIME / ELEVATION / ASPECT / INCLINE
       Description: Snow-pit metadata describing when and where the manual profile was recorded.

    B. Name: HEIGHT (cm) / RESISTANCE / FORM / EXTENT / LWC
       Description: Layer-by-layer stratigraphy fields describing layer depth, hand hardness, grain form, grain size, and wetness.

    C. Name: DENSITY
       Description: Density measurements from known-volume snow samples.

    D. Name: TEMPERATURE
       Description: Manual temperature profile measurements recorded in the AVY profile sheet.

-----------------------------------------------------------------
DATA-SPECIFIC INFORMATION FOR: iris/
-----------------------------------------------------------------

1. Number of variables:
2

2. Number of cases/rows:
6 files; 52-92 rows per file.

3. Missing data codes:
        blank line        Not present in prepared files

4. Variable List:
    A. Name: time
       Description: Time stamp recorded in the raw export (HH:MM:SS).

    B. Name: value
       Description: Raw IRIS measurement value associated with the time stamp.

-----------------------------------------------------------------
DATA-SPECIFIC INFORMATION FOR: snowmicropenetrometer/
-----------------------------------------------------------------

1. Number of variables:
Header metadata plus a high-resolution profile table with the main variables `distance` and `force`.

2. Number of cases/rows:
79 `.pnt` files; 3-411400 samples per file.

3. Missing data codes:
        -99999            Invalid GPS sentinel in some raw file headers

4. Variable List:
    A. Name: distance
       Description: Penetration distance in millimetres.

    B. Name: force
       Description: Penetration resistance in Newtons.

    C. Name: timestamp / coordinates / serial metadata
       Description: Header metadata read from the binary file by `snowmicropyn`.

-----------------------------------------------------------------
DATA-SPECIFIC INFORMATION FOR: snowscope/
-----------------------------------------------------------------

1. Number of variables:
Approximately 21 metadata header fields plus a profile table with 2-3 columns.

2. Number of cases/rows:
319 profile files; 81-2266 depth rows per profile table.

3. Missing data codes:
        null             Missing metadata value in the header block
        blank field      Missing profile value

4. Variable List:
    A. Name: serialNum / FW_version / PCB_version
       Description: Device identifier and firmware metadata.

    B. Name: collectionTime / collectionTime (Unix Time)
       Description: Acquisition timestamp.

    C. Name: Location
       Description: Latitude and longitude embedded in the file header.

    D. Name: depth (mm) / hardness (kPa) / optical Reflectance Avg
       Description: Depth-resolved SnowScope measurement table. `optical Reflectance Avg` appears only in a subset of profiles.

-----------------------------------------------------------------
DATA-SPECIFIC INFORMATION FOR: radar/
-----------------------------------------------------------------

1. Number of variables:
Header metadata plus a five-column numeric table.

2. Number of cases/rows:
166 files; each file contains 2565 numeric rows after the header.

3. Missing data codes:
        trailing incomplete line        Ignored when parsing; no replacement value written

4. Variable List:
    A. Name: Radar No. / Start-Frequency [MHz] / Stop-Frequency [MHz]
       Description: Instrument and acquisition settings preserved in the header.

    B. Name: X (m)
       Description: Along-trace distance coordinate.

    C. Name: I1 / Q1 / I2 / Q2
       Description: Recorded in-phase and quadrature channels from the radar export.

-----------------------------------------------------------------
DATA-SPECIFIC INFORMATION FOR: spatial_reference/
-----------------------------------------------------------------

1. Number of variables:
Varies by file. Linkage workbooks map measurement IDs and GPS points; GPS CSV files contain 37 RTK export columns; shapefile ZIPs contain standard SHP sidecar components.

2. Number of cases/rows:
10 files total: 4 linkage workbooks, 3 GPS CSV files, and 3 shapefile ZIP packages.

3. Missing data codes:
        blank cell        Not recorded in linkage workbook

4. Variable List:
    A. Name: Mesure # / SMP / Radar / Snowscope Minute
       Description: Linkage fields that connect measurement IDs across instruments.

    B. Name: Latitude / Longitude / Elevation
       Description: RTK GPS coordinates in decimal degrees and metres.

    C. Name: Name / Solution status / Correction type
       Description: GPS point identifier and RTK quality metadata.

-----------------------------------------------------------------
DATA-SPECIFIC INFORMATION FOR: documentation/
-----------------------------------------------------------------

1. Number of variables:
Narrative text files; no fixed tabular schema.

2. Number of cases/rows:
8 UTF-8 plain-text files converted from DOCX.

3. Missing data codes:
        not applicable     Free-text field notes

4. Variable List:
    A. Name: day/site heading
       Description: Human-readable identifier for the field day and site.

    B. Name: team list
       Description: Personnel named in the field note.

    C. Name: day summary / measurement summary
       Description: Narrative notes explaining what was measured, field conditions, and operational issues.
