This README.txt file was generated on 2026-03-24 by Codex; researcher review applied 2026-04-28 (PR #2)

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
        Email: alexandre.langlois2@usherbrooke.ca

        Name: Benjamin Imbach
        Institution: UQAR, Laboratoire de geomorphologie et de gestion des risques en montagne (LGGRM)
        Email: Benjamin.Imbach@uqar.ca

        Name: Francis Gauthier
        Institution: UQAR, Laboratoire de geomorphologie et de gestion des risques en montagne (LGGRM)
        Email: Francis_Gauthier@uqar.ca

        Name: Francis Meloche
        Institution: UQAR, Laboratoire de geomorphologie et de gestion des risques en montagne (LGGRM); WSL Institut pour l'etude de la neige et des avalanches SLF; ETH Zurich, Chair of Alpine Mass Movements
        Email: fmeloche@ethz.ch

        Name: Violaine Paquette
        Institution: Universite de Sherbrooke, Groupe de Recherche Interdisciplinaire sur les Milieux Polaires (GRIMP)
        Email: Violaine.Paquette@USherbrooke.ca

        Name: Kate Hale
        Institution: The University of British Columbia, Snow Water Resources Laboratory
        Email: kate.hale@ubc.ca

        Name: Hans-Peter Marshall
        Institution: Boise State University, Cryosphere, Geophysics and Remote Sensing, CryoGARS
        Email: hpmarshall@boisestate.edu

        Name: Joachim Meyer
        Institution: Boise State University, Cryosphere, Geophysics and Remote Sensing, CryoGARS
        Email: jmeyer@boisestate.edu

        Name: Julien Meloche
        Institution: Environnement et Changement climatique Canada

3. Date of data collection (single date, range, approximate date):

2025-03-01 to 2025-03-06

4. Geographic location of data collection:

Rogers Pass, Glacier National Park, Selkirk Mountains, British Columbia, Canada.
Bounding box (WGS84, EPSG:4326): west -117.7304, south 51.2274, east -117.4670, north 51.3284.
Elevation range represented by GPS and snow-profile metadata: 1832-2088 m.
Study sites represented in the prepared package are Fidelity, Jim Bay Corner, Hermit, Round Hill, and Christiana Ridge.

5. Information about funding sources that supported the collection of the data:

Fonds de recherche du Quebec - Nature et technologie (FRQNT). Fonds des nouvelles initiatives de recherche et de sauvetage.

---------------------------
SHARING/ACCESS INFORMATION
---------------------------

1. Licenses/restrictions placed on the data:

These data are prepared for release under the Creative Commons Attribution-NonCommercial 4.0 International (CC BY-NC 4.0) license:
https://creativecommons.org/licenses/by-nc/4.0/

2. Links to publications that cite or use the data : None

3. Links/relationships to ancillary data sets or software packages:

- `snowmicropyn` is a python packagerecommended for reading `.pnt` files: https://pypi.org/project/snowmicropyn/


5. Was data derived from another source? No

6. Recommended citation for this dataset:

Madore, J.-B., Langlois, A., Imbach, B., Gauthier, F., Meloche, F., Paquette, V., Hale, K., Marshall, H.-P., Meyer, J., Meloche, J. (2026). Snow profile observation datasets, Rogers Pass, Glacier National Park, British Columbia, Canada. Federated Research Data Repository. DOI pending.

---------------------
DATA & FILE OVERVIEW
---------------------

1. File List

   Naming convention:
   - Standardized folder names use `<datatype>/<YYYYMMDD>_<site>` or `<datatype>/<YYYYMMDD>_<site>_<content>`.
   - Standardized top-level file names use `<YYYYMMDD>_<site>_<content>.<ext>`.
   - Instrument-native file names inside measurement folders were preserved where they already encode acquisition identifiers, for example `s35m0151.pnt`, `2025-03-05_1738_Profile105_SN00322.csv`, or `054820250302_1554.txt`.

   A. Filename: snow_stratigraphy/
      Short description: Seven raw Excel workbooks containing manual snow-pit observations, one workbook per site-day. Representative files are `20250301_fidelity_stratigraphy.xlsx`, `20250303_hermit_stratigraphy.xlsx`, and `20250306_christiana_ridge_stratigraphy.xlsx`. Each workbook has four sheets: `AVY profile`, `Stability Tests`, `Density`, and `IRIS`.

   B. Filename: iris/
      Short description: Six daily IRIS raw text exports, renamed to `20250301_fidelity_iris_raw.txt` through `20250306_christiana_ridge_iris_raw.txt`. Each file is a two-column plain-text time series (`time`, `value`) used to support IRIS layer observations.

   C. Filename: snowmicropenetrometer/
      Short description: Four day-site folders containing 79 SnowMicroPenetrometer `.pnt` profiles. Folder names are `20250301_fidelity/`, `20250302_jim_bay_corner/`, `20250305_round_hill/`, and `20250306_christiana_ridge/`. Representative files are `s35m0129.pnt`, `s35m0150.pnt`, and `s35m0208.pnt`.

   D. Filename: snowscope/
      Short description: Five standardized SnowScope folder names containing 319 CSV profile files. Representative folders are `20250301_jim_bay_corner_snowscope/`, `20250305_round_hill_snowscope/`, and `20250306_christiana_ridge_snowscope/`. Representative files are `14-45_2025_3_1_Profile14_SN00328_.csv` and `2025-03-06_1649_Profile100_SN00304.csv`.

   E. Filename: radar_FMCW_K/
      Short description: Five day-site folders containing 166 FMCW K-band radar text exports (center 24.5 GHz, sweep 23.5-26 GHz). Representative folders are `20250302_jim_bay_corner/`, `20250304_fidelity/`, and `20250305_round_hill/`. Representative files are `052820250302_1505.txt`, `059820250304_1338.txt`, and `056720250302_1625.txt`.

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

- Morning hazard assessment PDFs were excluded.
- HEIC field notebook photos were excluded.
- Administrative material such as logistics spreadsheets, planning documents, and travel files was excluded.
- A blank `StratiTemplate.xlsx` workbook and an `IRIS_20250301.TXT.docx` companion file were excluded because they do not add unique observed data to the deposit.

4. Are there multiple versions of the dataset? No

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

Compact 24 GHz FMCW radar measurements were collected along spatial transects using the radar architecture described by Pomerleau et al. (2020, Low cost and compact FMCW 24 GHz radar applications for snowpack and ice thickness measurements, https://doi.org/10.3390/s20143909). The system is a K-band FMCW radar with center frequency 24.5 GHz and a bandwidth of 2.5 GHz (sweep 23.5-26 GHz). Raw files are stored in the `radar_FMCW_K/` folder and preserve the original header metadata and sampled I/Q signal table.

SnowScope profiles were acquired with the Snow Scope Probe (Propagation Labs), a digital snow penetrometer consisting of a sensor bullet on a collapsible probe. The instrument measures depth-resolved hardness at over 5000 Hz sampling, with a hardness range of 3–550 kPa, a depth resolution of approximately 3 mm, and a minimum resolvable layer thickness of 1.5 mm. An optional optical reflectance channel records near-infrared backscatter at each depth step; 181 of the 319 profiles in this package include that channel. Data are exported as CSV files from the companion Snow Scope App, with a 21-field metadata header (serial number, firmware version, PCB version, GPS coordinates, collection time, profile depth) followed by a depth-resolved measurement table. Linkage workbooks and RTK GPS exports were collected to georeference the radar, SMP, and SnowScope transects and to map acquisition point numbers to files.

2. Methods for processing the data:

Data contained in the prepared package are raw exports from the field campaign, with no numeric editing applied to the scientific files 🔔. Minor quality-control related modifications were made during preparation to standardize the package structure, but the scientific content of the files was not altered.

Quality control modifications are documented in `artifacts/qc_report.md`; all open items were resolved during researcher review (PR #2, 2026-04-28).

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
- GPS exports are obtained by RTK acquisition and should be treated as WGS84 geographic coordinates.

GPS coordinates are WGS84 geographic (EPSG:4326). Elevation values are ellipsoidal heights.

5. Environmental/experimental conditions:

The campaign covered five Rogers Pass sites between 1832 m and 2088 m elevation. SnowScope profile depths in the prepared package range from 81 mm to 2266 mm, and SMP profile depths extend to 1700 mm. Manual snow-pit temperature entries preserved in the workbooks span approximately -8.5 to 2.0 degrees C. The Hermit field notes and workbook metadata indicate that the Day 3 profile quality was poor and should be interpreted cautiously.

6. Describe any quality-assurance procedures performed on the data:

Quality assurance during preparation focused on packaging and interpretability rather than on altering scientific measurements. The prepared package:
- standardizes folder names and filenames for deposit consistency;
- preserves raw instrument formats and numeric content;
- converts ancillary DOCX notes to plain text for accessibility.

The following items were resolved during researcher review (PR #2, 2026-04-28):
- Day 6 Fidelity revisit workbook confirmed as a revisit (same site, five days later); kept with `_revisit` filename.
- Radar band confirmed K-band; folder standardized to `radar_FMCW_K/` with center frequency 24.5 GHz.
- Morning hazard assessment PDFs excluded as out of scope.

Remaining items documented but not altered:
- Some raw SMP file headers contain invalid GPS sentinels (-99999); these were documented and left unchanged.
- Some template-derived workbook cells contain placeholder zeros; flagged for a final researcher passthrough before deposit.

7. People involved with sample collection, processing, analysis and/or submission:

Field participants include Jean-Benoit Madore, Alexandre Langlois, Benjamin Imbach, Francis Gauthier, Francis Meloche, Violaine Paquette, Kate Hale, Hans-Peter Marshall, Joachim Meyer, and Julien Meloche. Parks Canada staff are referenced in the notes as operational collaborators for site access and logistics.

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
DATA-SPECIFIC INFORMATION FOR: radar_FMCW_K/
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
