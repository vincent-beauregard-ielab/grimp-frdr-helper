This README.txt file was generated on 2026-09-24 by Paul Billecocq

--------------------
GENERAL INFORMATION
--------------------

1. Title of Dataset: Snow profile, SSA, and radar observations, Rogers Pass, Glacier National Park, British Columbia, Canada (2025-2026 winter season)

2. Author Information
	A. Principal Investigator Contact Information
		Name: Alexandre Langlois
		Institution: Universite de Sherbrooke (GRIMP, Departement de geomatique appliquee)
		Email: TBD

	B. Associate or Co-investigator Contact Information
		Name: Jean-Benoit Madore
		Institution: Universite de Sherbrooke (GRIMP)
		Email: TBD
		Role: Field data collection; IRIS/SSA, SMP, and FMCW radar methodology (author of the two source theses underlying this dataset's Fidelity/Rogers Pass measurement program)

		Name: Benjamin Imbach
		Institution: Universite du Quebec a Rimouski (UQAR)
		Email: TBD
		Role: Field data collection (also co-author of the related Glacier National Park snowpit dataset, DOI 10.20383/103.01523)

		Names: Nicolas Allet, Marie-Clara Delage, Violaine Paquette, Megan Cramb, Nicolas Marchand
		Institution: Universite de Sherbrooke (GRIMP), affiliations to confirm
		Email: TBD
		Role: Field data collection

		Names: Kate Hale, Joachim Meyer
		Institution: University of British Columbia (UBC)
		Email: TBD
		Role: Field data collection (present 2026-03-04; Kate Hale also present 2026-03-09)

	⚠️ Institutions, emails, and precise roles for the full team are still unconfirmed.


3. Date of data collection: 2026-03-03 to 2026-03-10 (2025-2026 winter field season).
⚠️ Only 6 of the 8 calendar days in this range have collected data — 2026-03-07 was a rest day and
2026-03-08 was a rest/filming day (Radio-Canada crew); both are confirmed empty of scientific data.

4. Geographic location of data collection: Rogers Pass, Glacier National Park, British Columbia, Canada.
Field sites visited: Round Hill, Fidelity, Jim Bay, Gopher Butte, Hermit Meadows.

⚠️ Site elevations from GRIMP's own weather-station records (same station names used by this campaign):
- Fidelity (Mount Fidelity): GRIMP's primary GNP research station, 1,905 m, treeline elevation on the
  east flank of Mount Fidelity. File-derived pit/GNSS readings confirm 1,905 m exactly.
- Round Hill: 2,100 m (literature), ~500 m uphill from Fidelity. File-derived readings span 1,822-2,058 m
  across several Round Hill sub-locations — broadly consistent, no single point hits exactly 2,100 m.
- Hermit Meadows: a distinct, higher-elevation site from "Hermit" station in GRIMP's records (1,950 m,
  lower down). Hermit Meadows is also a GNP summer campground; this campaign's file-derived GNSS/pit
  readings (2,099-2,125 m) are consistent with the Hermit Meadows site, not the lower Hermit station.
- Jim Bay Corner, Gopher Butte: confirmed real field sites for this campaign (not in GRIMP's prior
  published site records — new sites for this program). File-derived coordinates: Jim Bay Corner
  ~51.234-51.235 N, -117.699 to -117.698 W, elevation 1,822-1,868 m; Gopher Butte has no dedicated
  GPS file (linked via the DAY4 transect/pit workbooks only), pit elevation 1,925-1,930 m.

⚠️ File-derived whole-dataset bounding box (GNSS survey files, sentinel "no-fix" values excluded):
latitude 51.23423 to 51.33108, longitude -117.70780 to -117.52996, elevation approximately
1,822-2,125 m above sea level (WGS84).

5. Information about funding sources that supported the collection of the data:
⚠️ DECISION PENDING (PI). GRIMP's Glacier National Park/Fidelity research program has previously been
funded by the National Search and Rescue Secretariat New Initiatives Fund (SAR-NIF), the Natural
Sciences and Engineering Research Council of Canada (NSERC), the Canada Foundation for Innovation
(CFI), and the Centre d'etudes nordiques (CEN) (per Madore's 2016 MSc thesis acknowledgments). These
are candidate/plausible funders for the 2025-2026 campaign given program continuity, but the specific
grant(s)/award number(s) active for this campaign must be confirmed directly with the PI (Alexandre
Langlois) before finalizing this section.


---------------------------
SHARING/ACCESS INFORMATION
---------------------------

1. Licenses/restrictions placed on the data: ⚠️ DECISION PENDING (PI/researcher) — to be confirmed at Step 6

2. Links to publications that cite or use the data: TBD

3. Links/relationships to ancillary data sets or software packages:
⚠️ Candidate related dataset: "Snow profile observation datasets, Glacier National Park, British
Columbia, Canada" (DOI 10.20383/103.01523) — a related GNP snowpit archive by the same institutional
collaborators (Parks Canada's Andrew Jones and Catherine Brown are independently confirmed as GNP
avalanche-safety-group contacts in the Madore PhD thesis acknowledgments). Exact relation type to
confirm with researcher.

5. Was data derived from another source? No — primary field observations.

6. Recommended citation for this dataset: TBD — DOI not yet reserved

---------------------
DATA & FILE OVERVIEW
---------------------

Raw data are organized by field day (2026-03-03 to 2026-03-10), one folder per day, each containing
per-instrument subfolders. Two of the eight calendar days in the campaign window have no data:
2026-03-07 (rest day) and 2026-03-08 (rest/filming day, one administrative PDF only). Instrument
coverage varies by day; see the per-day table in artifacts/data_exploration.md.

File types present:
- Excel workbooks (.xlsx, 19 files): a master stratigraphy/snowpit datasheet per site visit
  (manual profile, stability tests, density, and linkage tables to each instrument's raw files),
  and a spatial-survey linkage workbook per multi-point transect day (GPS point number to
  instrument file numbers and manual snow-height readings).
- Radar logs (.txt, 329 files): per-measurement text files from two radar systems (folders named
  dku/ka on most days, Radar_K on 2026-03-09 and 2026-03-10).
  ⚠️ The ka/Radar_K radar's internal clock was not synced during this campaign — file-embedded
  timestamps for this instrument do not reflect the true collection date; rely on the day-folder
  name instead. Seven radar files (out of 329) are empty (0 bytes).
- SnowMicroPen profiles (.pnt, 48 files): binary penetrometer force-depth profiles, requires the
  snowmicropyn Python package to read.
- IRIS logs (.txt, specific surface area instrument): per-scan calibration/reflectance readings.
- SnowScope profiles (.csv, 89 files): hand-push penetrometer hardness-depth profiles with onboard
  GPS and device metadata per file.
  ⚠️ A small number of SnowScope files carry a fixed placeholder GPS coordinate when the device had
  no location fix; these are not real positions and are excluded from spatial analysis.
- GNSS survey files (.kml/.kmz/.csv, 6 files): spatial-transect point coordinates, recorded with an
  Emlid Reach RS2 GNSS receiver (RTK fixed solution, WGS84, ~1 cm precision) on most days.
  ⚠️ 2026-03-03 used a different device/app (Gaia GPS, consumer iOS app, no RTK) and has no usable
  elevation.
- Fieldbook/snowpit photos (.heic/.jpg, 57 files) and hazard-assessment forms (.pdf, 10 files):
  supporting context, not instrument data.

Open item: file-naming conventions for instrument subfolders are not fully consistent across days
(e.g. GPS_pts vs GPS, dku+ka vs Radar_K) — researcher input needed on whether to normalize folder/file
names for the deposit package (decision for Data Preparation).

Out of FRDR deposit scope per researcher decision: the `templates/` folder (blank field forms) and
`Write in the Rain - table of content.docx` (paper-notebook index), kept in raw_data/ for reference
only.

---------------------------
METHODOLOGICAL INFORMATION
---------------------------

Manual snow profiles were recorded following the Observation Guidelines and Recording Standards for
Weather, Snowpack and Avalanches (OGRS, Canadian Avalanche Association, 2024 ed.,
https://www.avalancheassociation.ca/) and the International Classification for Seasonal Snow on the
Ground (ICSSG; Fierz et al., 2009), recording layering, grain type/size, hardness, and temperature
(typically every 10 cm) and density (typically every 5 cm).

Specific surface area (SSA) was measured using IRIS (InfraRed Integrating Sphere), a GRIMP-built
infrared-reflectance instrument (10-cm integrating sphere, ~1310-1315 nm laser; Montpetit et al.,
2012, following Gallet et al., 2009).

Snow hardness/stratigraphy profiles were measured with two complementary penetrometers: the
SnowMicroPen (SMP; motorized, ~20 mm/s, ~0.004 mm vertical resolution; Schneebeli & Johnson, 1998;
Schneebeli et al., 1999), whose raw .pnt files are processed with the snowmicropyn Python package
(SLF); and SnowScope/SCOPE (hand-push, optical depth-sensing, 1 mm depth resolution; Hagenmuller
et al., 2024). A Blade Hardness Gauge (BHG; Borstad & McClung, 2011) was also used for a subset of
layers as a secondary, less operator-biased hand-hardness measurement.

Snow depth and internal stratigraphy were also measured with a dual-frequency FMCW radar operated at
two bands (folders dku and ka/Radar_K in the raw data). File headers confirm dku operates at 13 GHz
and 17 GHz, consistent with a dual-Ku-band system matching the planned satellite Terrestrial Snow
Mass Mission (TSMM, Derksen et al., 2019), described as planned infrastructure in Madore's 2023 PhD
thesis. File headers for ka/Radar_K show a 23.5-26 GHz sweep, consistent with GRIMP's existing 24 GHz
system (IMST Sentire sR1200; Pomerleau et al., 2020; Laliberte et al., 2018/2022), operated at
Fidelity since 2017. ⚠️ The ka/Radar_K instrument's internal clock is not synced to the true
collection date (see Data & File Overview).

Measurement locations were recorded with an Emlid Reach RS2 GNSS receiver (RTK fixed solution, WGS84,
~1 cm precision) on most days; 2026-03-03 used a different consumer GPS app (Gaia GPS, no RTK,
elevation not usable).

Open item: this section will be finalized once remaining acquisition-protocol details (exact IRIS
wavelength/protocol as operated, radar deployment geometry) are confirmed with the field team
(Quality Control step).

-----------------------------------------------------------------
DATA-SPECIFIC INFORMATION
-----------------------------------------------------------------

⚠️ [placeholder — to be filled at Step 6; per-file/per-variable codebook, see artifacts/data_exploration.md for the structural inventory already gathered]
