# Data Exploration — RogersPass_2025-2026

Step 3 of the GRIMP FRDR deposit workflow. Full inspection method, code, and captured output live in
`notebooks/RogersPass_2025-2026_data_exploration.ipynb`. This document is the structured summary.

Inspected: `datasets/RogersPass_2025-2026/raw_data/` (~385 MB, 8 day folders + `templates/` + one
loose logistics file). Tools used: `pandas`, `openpyxl`, `snowmicropyn`, `pdfplumber`, `zipfile`/`re`
(for KML/KMZ/docx, since no dedicated parser is in this project's dependency set). A representative
sample was opened in depth per file type across multiple days; full-tree `pathlib.rglob`/`os.walk`
counts were used for accurate whole-dataset inventory.

**Cross-reference note:** `artifacts/research.md` (Research step, run in parallel) was read for
comparison. Several of its literature-derived open items are resolved or partially resolved by the
file evidence below — see "Cross-check against research.md" at the end of each scope section.

---

## 1. File inventory

### By extension (whole dataset)

| Extension | Count | File type |
|---|---|---|
| `.txt`/`.TXT` | 329 | Radar logs (`dku`, `ka`, `Radar_K`), IRIS logs |
| `.csv` | 90 | SnowScope profiles (89), 1 GPS RTK export (Hermit Meadows, duplicates its sibling KML) |
| `.pnt` | 48 | SnowMicroPen binary profiles |
| `.heic` | 47 | Fieldbook/snowpit photos (iPhone format) |
| `.xlsx` | 19 | Stratigraphy workbooks (15) + spatial-linkage workbooks (4) |
| `.pdf` | 10 | Morning hazard/risk-assessment forms |
| `.jpg` | 10 | Fieldbook/snowpit photos (older device / GPS unit photos) |
| `.docx` | 9 | Per-day field-team readmes (7), 1 radar sub-readme, 1 field-notebook table of contents |
| `.kml` | 4 | GPS RTK survey exports |
| `.kmz` | 1 | GPS waypoint export (Day1, different app/format) |

### By day folder

| Day folder | Date | Files | Instrument subfolders present | Data collected? |
|---|---|---|---|---|
| `Day1_RoundHill_03-03-2026` | 2026-03-03 | 150 | Fieldbook_photos, GPS_pts, IRIS, dku, ka, smp, snowscope | Yes — full profile + 18-pt spatial transect |
| `Day2_Fidelity_RH_04-03-2026` | 2026-03-04 | 61 | Fieldbook_photos, GPS_pts, IRIS, dku, ka, smp, snowscope | Yes — 3 site profiles |
| `DAY3_RoundHill Drone and Rogers Pass_05-03-2026` | 2026-03-05 | 25 | Fieldbook_photos, IRIS, snowscope | Partial — **no radar/SMP/GPS folders** (drone flights cancelled; see field readme) |
| `DAY4_JimBay-RoundHill-GopherButte_20260306` | 2026-03-06 | 140 | Field_Book_Photos, GPS_pts, IRIS, Snowscope, dku, ka, smp | Yes — 2-team day, 16-pt transect + full profile |
| `DAY5_RestDay_20260307` | 2026-03-07 | **0** | none | **No — confirmed empty, rest day** |
| `DAY6_ReposeEtFilm_20260308` | 2026-03-08 | 1 | none (1 loose PDF) | **No — hazard PDF only, "repose et film" (rest/filming) day** |
| `DAY7_HermitMeadows_20260309` | 2026-03-09 | 122 | Field_books_photos, GPS_pts, IRIS, Radar_K, snowscope | Yes — 24-pt transect + full profile + 2 surface profiles |
| `DAY8_Fidelity_20260310` | 2026-03-10 | 64 | Field_books_photos, GPS, IRIS, Radar_K, dku | Yes — 18-pt transect + upper-snowpack profile |

**Only 6 of the 8 day-folders contain scientific data.** DAY5 and DAY6 are confirmed non-collection
days from actual file contents (not just naming), consistent with their "RestDay"/"ReposeEtFilm"
folder names.

Instrument-folder naming is **inconsistent across days** and should be normalized during Data
Preparation:
- GPS: `GPS_pts` (Day1, Day2, DAY4, DAY7) vs `GPS` (DAY8) vs `GPS pts` (templates, with a space).
- K-band/Ku-band radar: `dku` + `ka` pair (Day1, Day2, DAY4) vs single `Radar_K` folder (DAY7, DAY8)
  — same measurement type (radar readings at a transect point, 3 positions per point per
  `Radar_K/READ ME.docx`), different naming, and DAY8 has no separate `ka`.
- Photos: `Fieldbook_photos` / `Field_Book_Photos` / `Field_books_photos`.
- Snowscope: `snowscope` (lowercase, most days) vs `Snowscope` (DAY4).

Out of FRDR deposit scope per researcher decision, confirmed present but not inventoried further:
`templates/` (all instrument subfolders empty except a 1-file `Photos of Snowpit` readme docx, plus
a template PDF and `StratiTemplate.xlsx`), and `Write in the Rain - table of content.docx`
(top-level, indexes a paper field notebook).

---

## 2. Excel workbooks (19 files, 2 distinct types)

Both types match `templates/StratiTemplate.xlsx`'s sheet structure exactly.

### 2a. Stratigraphy/reference workbook (15 files, one per snowpit/site visit)

Multi-sheet, sheet names vary slightly in capitalization/naming across files but always include:
`AVY profile`, `Stability Tests`, `Density`, `IRIS`, plus (when the site had that instrument)
`smp`, `dku`/`Dual KU`, `RadarK`/`Radar K`, `SS`/`Snowscope`/`SnowScope`, `BHG`, occasionally `GPS`.

| Sheet | Content | Columns / structure | Notes |
|---|---|---|---|
| `AVY profile` | Manual snow-pit header + stratigraphy + temperature profile | DATE, TIME, ELEVATION, ASPECT, INCLINE, OBSERVER, SKY, PRECIP, WIND; then HEIGHT / RESISTANCE / FORM / EXTENT / LWC(Ѳ) / WEIGHT / DENSITY / COMMENTS by depth; separate TEMPERATURE block (H, T, M, D by height) | Free-text grain-form codes (F, 4F+, 1F, P…) and grain-type codes (PP, R, SH, Fc…) per ICSSG; **no explicit missing-value token** — blank cell = not recorded. Elevation cell blank in several files. |
| `Stability Tests` | Compression/extended-column test results | Test (CT/ECT, mixed case), Score (e.g. M13, H24 — letter=fracture quality, number=tap count), Grain Type, Facture Char. (rp/sc/sp…), Down (cm), Comments | `Test` column case is **not uniform** (`ct`, `CT`, `Ect`, `ECT` all appear in one file). |
| `Density` | Wedge-cutter density-by-height | Height (cm), Weight (g), Density (kg·m⁻³), plus a small side-table of cutter-volume formulas (250cc ×4, 100cc ×10) | Alternating blank/filled rows (height row, then weight/density row) — a 2-row-per-measurement layout, not a flat table. |
| `IRIS` | Processed SSA readings | Version, Spectralon (%), 3x Calibration Voltage, Height (cm), 3x Scan (V), Reflectance (%), SSA (m²·kg⁻¹), Ropt (mm), Field Notes, plus a separate height/HS column | Sparsely filled — many derived columns (Reflectance, SSA, Ropt) blank in the raw sheet, likely computed downstream. |
| `smp` | **SMP file-number linkage** | e.g. `Top of profile (cm): 0` → SMP file 732, `170` → 735, then a plain numbered list (733, 734…) | Maps snowpit height markers to SMP `.pnt` file numbers for that pit. |
| `dku` | **dku file-number linkage** | Angle (0-50°, 5° steps) → Number (file counter, e.g. 780-789); separate `Radar height` cell | Maps radar angle sweep to `dku` filenames' leading counter. |
| `RadarK` / `Radar K` | **Radar file-number linkage** | Single free-text cell, e.g. `"Radar K: 003-004-005"` | Lists the 3 file numbers (3 positions per point, per the radar sub-readme). |
| `SS` | **Snowscope point linkage** | Single free-text cell, e.g. `"SS Points:60-62-63"` | Lists SnowScope testNum IDs for that pit. |
| `BHG` | Secondary mini hardness profile | HEIGHT, "BHG 1" (triplet values like `2.03-1.83-2.42`) | Sparse, alternating-row layout like Density. Meaning of "BHG" not resolved from file contents alone — flag for Research/researcher. |

**Relationship confirmed:** the stratigraphy workbook's `smp`/`dku`/`RadarK`/`SS` sheets are a
**linkage table** from the pit to the instrument's raw files — e.g. `RoundHill.xlsx`'s `smp` sheet
references SMP files 732-735, and `smp/S35M0732.pnt` exists in the same day folder and covers that
exact site (coordinate 51.2351, -117.7074, see §4).

**Header cross-check (date/elevation/aspect) across all 15 files** confirms internal DATE matches
the day-folder date in every case **except one**: `Day2_Fidelity_RH_04-03-2026/RoundHill_bottom.xlsx`
has DATE cell `2026-04-03` — a **day/month transposition** (should read `2026-03-04`). Pit elevations
recorded range **1868-2125 m** (several files leave elevation blank).

**Filename anomalies:**
- `FidelityStation_2023-03-04.xlsx` — filename year is `2023` (typo); internal DATE cell confirms
  `2026-03-04`.
- `20260310_Round Hill upper snowpackl.xlsx` — stray trailing "l".

**Structural note:** column layout is not byte-identical across all 15 files despite sharing the
same template (a few header cells shift by one column between files) — a light structural QC pass
is recommended before batch-parsing all 15 into one table.

### 2b. Spatial/linkage workbook (4 files, single `Sheet1`)

One row per point along a spatial-survey transect. Columns (present in most, some files omit
Dual KU or use 1-3 Radar K sub-columns): `# | GPS | Dual KU | Radar K | SMP | SS | HS(1-3)`.
`GPS` is the point number resolved to lat/lon in the day's `GPS_pts`/`GPS` KML/CSV file (§4); the
other columns are the corresponding instrument-file measurement numbers; `HS1`/`HS2`/`HS3` are
1-3 replicate manual snow-height probe readings (cm) at that point.

Files: `Spatial_Round_Hill.xlsx` (18 rows), `JimBay_Spatial.xlsx` (16 rows + 2 comment rows),
`20260309_HermitMeadow_Spatial.xlsx` (24 rows), `20260310_RoundHill_Spatial.xlsx` (18 rows).

**Missing-value encoding is inconsistent within this file type**: blank cell, the literal string
`n.a`, and pandas `NaN` all appear as "no value" in the same workbook (`JimBay_Spatial.xlsx`, point
`12*`, Dual KU column = `n.a`).

**Important field-team comment cell** (`JimBay_Spatial.xlsx`, below the data table):
> "Comment Snowscope: Measure ID 271-272-273-274-275 are unmatched. The date do not match the
> recording timestamp and there is 1 missing ID."

This independently corroborates a SnowScope data-quality issue also described in the DAY4 field
readme (§7) — treat as a known, pre-flagged gap for Quality Control, not a new discovery.

**Note:** the spatial-workbook SMP/Dual KU/Radar K numbering series is **separate from** the
stratigraphy-workbook's numbering for the same day (e.g. `RoundHill.xlsx` references SMP 732-735,
`Spatial_Round_Hill.xlsx` references SMP 739-757) — these are two distinct measurement campaigns
per day (fixed-point full profile vs. spatial-survey transect), not conflicting/duplicate IDs.

---

## 3. Radar instrument logs (`dku`, `ka`, `Radar_K` — 329 `.txt` files)

Two radar systems, one plain-text file per single measurement, `#`-comment-style header + data:

**`dku` (dual-frequency Ku-band radar).** Filename:
`{counter}_{freq}GHz_{site}_{angle idx}_V_{angle}deg.txt` (e.g. `0790_13GHz_RHFP_00_V_00deg.txt`).
Header fields: Radar Frequency (13GHz or 17GHz), Measurement counter, Site Name, Radar Angle,
Measurement ID, Polarization (V), **Timestamp (ISO 8601, correct and consistent with the true field
date)**, Device Number, Frontend Connected, Firmware Version/Revision/Date, Min/Max Frequency (Hz),
Signal Type, TX/RX Channel Selection, TX/RX Power Setting. Angle sweep 0-50° in 5° steps at most
sites. Row/sample count of the waveform body not fully characterized (large, ~51k lines observed
in one sample) — reserve full-format documentation for Data Preparation if `dku` is retained in the
deposit.

**`ka` / `Radar_K` (K-band radar, ~23.5-26 GHz).** Filename: `{counter}{device-date}_{device-time}.txt`
(e.g. `000020250903_1636.txt`). Header: Date, Time of creation, Radar No. (device serial), Interface,
Start/Stop-Frequency (MHz), Ramp Time (ms), Normalization, Attenuation (dB), Number of Samples (513),
Zero Pad Factor, Active Channels (I1, Q1, I2, Q2), Tic. Body: `X (m), I1, Q1, I2, Q2` CSV block (raw
IQ waveform vs. range, ~513-2600 rows depending on padding).

**Critical discrepancy — radar clock not synced:** every `ka`/`Radar_K` file inspected has a
device-embedded Date/filename timestamp of `2025-09-0x` (03 or 04) — **months earlier and in a
different year** than the true field dates (2026-03-xx). The `dku` radar's `Timestamp` header field,
by contrast, is correct. **Folder/site naming, not the `ka`/`Radar_K` file timestamp, is the only
reliable date source for this instrument.** Flag prominently for Quality Control and the README's
missing-data/known-issues section.

**Empty files:** 7 of 329 `.txt` files are 0 bytes (likely failed writes on power loss):
`DAY4.../dku/0862_13GHz_JBTR_15_V_30deg.txt`, `.../0862_17GHz_JBTR_15_V_30deg.txt`,
`Day1.../ka/000020250903_1636.txt`, `.../000120250903_1637.txt`,
`Day2.../dku/0831_13GHz_FITO_01_V_30deg.txt`, `.../0831_17GHz_FITO_01_V_30deg.txt`,
`.../0832_13GHz_FITO_02_V_30deg.txt`. List as known gaps in Data Preparation rather than silently
dropping.

**Software needed:** none beyond a text/CSV reader — no proprietary format.

---

## 4. SnowMicroPen binary profiles (`smp/*.pnt` — 48 files)

Binary SnowMicroPen format. **Requires `snowmicropyn.Profile.load()`** (Python, already in this
project's `.venv`) — not human-readable as plain text. Each file provides:

| Field | Example | Notes |
|---|---|---|
| `timestamp` | `2026-03-03 19:21:00+00:00` | UTC, correct/consistent with true field date |
| `coordinates` | `(51.2351189, -117.7074432)` | Onboard GNSS fix, WGS84 (lat, lon) |
| `samples` | DataFrame, columns `distance` (mm), `force` (N) | ~4.1 µm depth resolution (411,400 samples over ~1700 mm in the sampled file) |

Filename pattern `S{device}M{counter}.pnt` (e.g. `S35M0732.pnt`) — the counter matches the SMP
linkage numbers recorded in the stratigraphy/spatial workbooks (§2). No missing-value token — each
row is a real (distance, force) pair; force is non-negative, ranged ~0.02-1.5 N in the sampled file.

**File count per day:** Day1 = 26, DAY4 = 16, Day2 = 6, total 48. Matches the instrument-coverage
table in §1 — no SMP on DAY3/DAY7/DAY8.

---

## 5. IRIS (specific surface area) logs

Plain-text `.txt`/`.TXT`, no header row, comma-delimited: `date, time, "IRIS", voltage`, e.g.
`2026-3-3,  16:56:46,  IRIS,  2.014`. UTF-8/ASCII. One row per scan/calibration reading (typically
3 replicate readings per calibration/measurement step). Row counts per file range roughly 15-90.
No explicit missing-value token — every row is a complete reading. On multi-site days, files live
in per-site subfolders (e.g. `IRIS/IRIS#2-RH/IRIS2_20260304.TXT`, `IRIS/IRIS-2_JimBayCorner_
FullProfile_20260306/20260306JimBayCorner.TXT`); on single-site days they sit flat in `IRIS/`.
Timestamps consistent with true field dates. Processed SSA/reflectance values live in the
stratigraphy workbook's `IRIS` sheet (§2), not in this raw log.

---

## 6. SnowScope hardness-profile CSVs (`snowscope/*.csv` — 89 files)

Structured CSV: `GENERAL INFO` metadata block, then `SCOPE PROFILE` metadata block, then a
`depth (mm), hardness (kPa),` data table at 1 mm resolution (trailing comma/empty 3rd column in
every data row — a formatting quirk, not a real field).

**Metadata fields:** name (usually `null`), elevation (m, decimal — device-computed, not
necessarily GNSS-grade), aspect/air temperature/slope angle (usually `null`, not recorded),
profilePrivacy, totalSnowDepth (usually `null`), collectionTime (human-readable + Unix time, correct
and consistent with true field dates), creator name, org name (`null`), **Location (lat, lon —
onboard GNSS fix, independent of the RTK survey files)**, Max Profile Speed, Profile Time, testNum
(profile ID), serialNum (device), profileDepth (mm), batteryCapacity, errorCode, temperature (°C),
firmware/PCB version.

- **Device serials:** two physical units, `00249` and `00374`.
- **Creators recorded:** Megan Cramb, Benjamin Imbach (per-file operator attribution — useful for
  Data Preparation's provenance/creator metadata, separate from the top-level author list).
- **profileDepth range:** 442-2462 mm across the 89 files.
- **GNSS sentinel value found:** the exact coordinate `(51.4155194, -117.0087479)` — ~30 km
  northeast of every other spatial source in this dataset — repeats identically across several
  different profile IDs/timestamps (e.g. profiles 102-104, 2026-03-05, in
  `Day2_Fidelity_RH_04-03-2026/snowscope/Gopher_Butte/`; profiles 272-273, 2026-03-06, in
  `DAY4.../Snowscope/JimBay_FullProfile/`). This is a **fixed "no GNSS fix" sentinel emitted by the
  device firmware**, not a real position — exclude these rows from any spatial analysis/QC and
  document as the SnowScope missing-location encoding.
- **Separate finding:** `Day2_Fidelity_RH_04-03-2026/snowscope/Gopher_Butte/*.csv` files carry an
  internal `collectionTime` of **2026-03-05** (DAY3's date) rather than 2026-03-04 (Day2's folder
  date) — a folder/date mismatch to flag alongside the `RoundHill_bottom.xlsx` transposition (§2).

Once the sentinel rows are excluded, onboard-GNSS coordinates are consistent with the RTK survey
bounding box (§7).

---

## 7. GNSS survey files (`GPS_pts`/`GPS` — 4 KML, 1 KMZ, 1 CSV) and scope summary

Two different GNSS data sources are mixed across days:

- **Emlid Reach RS2 RTK survey exports** (Day2, DAY4, DAY7, DAY8): KML and/or CSV, WGS84
  (`Global CS`), decimal-degree lat/lon, ellipsoidal height (m), `Solution status` = `FIX` (RTK
  fixed), device serial, per-point averaging start/end UTC-offset timestamps. This is the
  authoritative coordinate source for the spatial-transect linkage workbooks (§2).
- **Day1 (`RH_TR_2026.kmz`)** is a **different format**: a Gaia GPS (iOS app) waypoint export
  (`<atom:name>GaiaGPS running on iOS</atom:name>`), no RTK, **elevation hard-coded to `0.00 m`**
  (not usable), only lat/lon meaningful. Placemark names are human waypoint labels with local
  timestamps ("Wpt 2026-03-03 11:59:41 5"), not a coordinate-table format.

### Site table (file-derived)

| Site (as named in data) | Days visited | GNSS points | Lat range | Lon range | Elevation range (m) |
|---|---|---|---|---|---|
| Round Hill | Day1, Day2, DAY3, DAY4, DAY8 | 18 (Day1, GaiaGPS) + 19 (DAY8, RTK) | 51.23423-51.23531 | -117.70780 – -117.70699 | 1822-2058 (pit) / 2040-2044 (DAY8 GNSS) |
| Fidelity (Fidelity Station) | Day2, DAY3, DAY8 | 3 (Day2 RTK) | 51.23648 | -117.70082 – -117.70080 | 1864-1905 |
| Jim Bay (Jim Bay Corner) | DAY4 | 19 (RTK) | 51.23423-51.23467 | -117.69928 – -117.69865 | 1822-1868 |
| Gopher Butte | Day2, DAY4 | no dedicated GPS_pts file — linked via the DAY4 Jim Bay transect / pit workbooks only | — | — | 1925-1930 (pit) |
| Hermit Meadows | DAY7 | 24 (RTK) | 51.33037-51.33108 | -117.53087 – -117.52996 | 2099-2110 (GNSS) / 2113-2125 (pit) |
| Rogers Pass (general/drone-flight reference) | DAY3 | — (drone flights cancelled) | — | — | — |

**File-derived whole-dataset bounding box (sentinel-filtered):** lat **51.23423 to 51.33108**, lon
**-117.70780 to -117.52996**, elevation **~1822-2125 m**.

### Temporal coverage

| Date | Day label | Sites | Data collected |
|---|---|---|---|
| 2026-03-03 | Day1 | Round Hill | Full profile + 18-pt spatial transect (GPS/Dual KU/Radar K/SMP/SS/HS) |
| 2026-03-04 | Day2 | Fidelity, Round Hill, Gopher Butte | 3 site profiles + upper-snowpack observations |
| 2026-03-05 | DAY3 | Round Hill, Rogers Pass | Drone flights cancelled (RTK link failure); half profile + IRIS/snowscope only |
| 2026-03-06 | DAY4 | Round Hill, Gopher Butte, Jim Bay Corner | 2-team day: surface profiles + 16-pt spatial transect + full profile |
| 2026-03-07 | DAY5 | — | **Rest day, no data** |
| 2026-03-08 | DAY6 | — | **Rest/filming day (Radio-Canada crew), 1 hazard PDF only** |
| 2026-03-09 | DAY7 | Hermit Meadows | 24-pt transect + full profile + 2 surface profiles |
| 2026-03-10 | DAY8 | Fidelity/Round Hill | 18-pt transect + upper-snowpack profile |

**Actual collection dates: 2026-03-03 to 2026-03-10 — matches the draft scope's date range exactly**,
but only 6 of the 8 calendar days within that range have data (DAY5, DAY6 do not).

### Cross-check against `research.md` (literature-derived values)

| Item | Literature-derived (research.md) | File-derived (this document) | Status |
|---|---|---|---|
| Campaign dates | 2026-03-03 to 2026-03-10 | 2026-03-03 to 2026-03-10 (6 of 8 days have data) | **Confirmed**, with the DAY5/DAY6 caveat added |
| Fidelity elevation | 1,905 m (Table 3.1) | 1,905.0 m exactly (`FidelityStation_...xlsx` AVY profile) | **Confirmed exactly** |
| Round Hill elevation | 2,100 m | 1822-2058 m across pit/GNSS readings at various Round Hill sub-locations | **Broadly consistent**, but no single file-derived reading hits exactly 2,100 m — Round Hill spans multiple measurement points at somewhat different elevations |
| Hermit ("Hermit Meadows") elevation | 1,950 m | 2099-2125 m (GNSS + pit) | **Discrepancy of ~150-175 m** — flag for researcher confirmation; possible that "Hermit" (weather station) and "Hermit Meadows" (2026 field site) are related but not identical locations |
| Jim Bay, Gopher Butte | No literature match; Gopher Butte's only web hit gives ~51°14'17"N, 117°42'10"W (≈51.238, -117.703), unrelated 2005-06 study | Jim Bay: lat 51.234-51.235, lon -117.699 – -117.699; Gopher Butte: no dedicated GPS file, pit elevation 1925-1930 m | Jim Bay's file-derived coordinates are **plausibly close** to the unrelated web reference for Gopher Butte (same general area), but this does not confirm site identity — still **to be confirmed with the researcher**, as research.md notes |
| GPS unit/accuracy | "Not mentioned in either thesis — unit type/accuracy unknown" | **Resolved:** Emlid Reach RS2, RTK `FIX` solution, WGS84, ~1 cm RMS (Day2/DAY4/DAY7/DAY8); Day1 used a different device/app (Gaia GPS on iOS, no RTK, no usable elevation) | **File evidence resolves this open item** |
| `dku` radar frequency | Inferred dual-Ku 13.5/17.5 GHz (TSMM-matching, planned per PhD thesis) | File headers confirm **13 GHz and 17 GHz** exactly | **Consistent** with the literature inference (close to the guessed 13.5/17.5 GHz) |
| `ka`/`Radar_K` radar frequency | Inferred ~24 GHz (existing Pomerleau/Laliberté system) | File headers show **23.5-26 GHz sweep** (center ≈24.75 GHz) | **Consistent** — 24 GHz falls within the observed sweep |
| Team roster — Kate Hale, Joachim Meyer | Flagged in research.md as an *unverified* lead from an external PR describing a possibly-different campaign | **Both names appear directly in this campaign's own field-team readme `.docx` files**: Kate Hale is named present on Day2 (04-03-2026) and DAY7 (09-03-2026); Joachim Meyer ("JM") is named present on Day2. Not from the external PR — from this dataset's own raw files. | **Resolves part of research.md's open item #7** — these two people did participate in the 2025-2026 campaign being documented here, independent of whatever the external PR describes |

---

## 8. Context/support files (photos, PDFs, field readmes) — not deeply parsed

- **Photos** (47 `.heic` + 10 `.jpg`, one folder per day): fieldbook and snowpit photos. Counted
  only, not opened individually — out of scope for structural documentation (image files, no
  tabular structure).
- **Hazard-assessment PDFs** (10 files, 1-3 pages, `pdfplumber`-readable text): standardized
  morning hazard/risk-assessment forms referencing avalanche.ca weather stations — Rogers Pass
  1,315 m, Fidelity 1,905 m, Round Hill 2,100 m, Hermit 1,905 m, Abbott 2,130 m. **This independently
  confirms the 1,905 m Fidelity elevation** found in the xlsx workbook. Operational/safety documents
  (team roster, weather obs, avalanche summary), not primary scientific data — presence noted, not
  deposit-scope decision (that belongs to Data Preparation).
- **Per-day field-team readme `.docx`** (7 files, French, extracted via raw `word/document.xml`
  since `python-docx` is not installed in this project's `.venv` — only `zipfile`/`re` were needed):
  narrative day logs naming the team present, weather/logistics, and known data issues. These
  independently corroborate two findings above: the DAY3 drone-flight cancellation, and the DAY4
  SnowScope IDs-271-275 linkage gap (also flagged inside `JimBay_Spatial.xlsx` itself, §2). They
  also name **Kate Hale** and **Joachim Meyer** as present on specific days (see cross-check table
  above) and list "KH"/"JM" as the observer initials in `JimBayFullProfile.xlsx`'s AVY profile
  header — consistent, corroborating evidence across two independent file types.
- **`Radar_K/READ ME.docx`** (DAY7): "Trois mesures radar ont été prises par pts de transect...à
  trois positions différentes" — confirms the Radar K-1/K-2/K-3 triplicate-per-point pattern seen
  in the Hermit Meadows spatial workbook.
- **`templates/`, `Write in the Rain - table of content.docx`**: empty instrument folders and a
  paper-notebook index — logistics only, out of FRDR deposit scope per the researcher's decision;
  not inventoried further, per task instructions.

---

## Summary of discrepancies / anomalies found (for Quality Control)

1. **`Day2_Fidelity_RH_04-03-2026/RoundHill_bottom.xlsx`**: internal DATE cell reads `2026-04-03`
   (day/month transposed; should be `2026-03-04`).
2. **`Day2_Fidelity_RH_04-03-2026/snowscope/Gopher_Butte/*.csv`**: internal `collectionTime` reads
   `2026-03-05` (DAY3's date) instead of the Day2 folder date.
3. **Filename typos**: `FidelityStation_2023-03-04.xlsx` (year typo, content confirms 2026);
   `20260310_Round Hill upper snowpackl.xlsx` (stray trailing letter).
4. **`ka`/`Radar_K` radar files**: device clock not synced — every embedded Date/filename timestamp
   reads `2025-09-0x`, months and a year off from the true 2026-03 collection dates. Folder naming
   is the only reliable date source for this instrument family.
5. **7 zero-byte `.txt` radar files** (2 `dku` on DAY4, 2 `ka` on Day1, 3 `dku` on Day2) — listed in
   §3.
6. **SnowScope GNSS sentinel value** `(51.4155194, -117.0087479)` — a fixed "no fix" placeholder
   repeating across multiple unrelated profiles; must be filtered, not treated as a real location.
7. **Known SnowScope ID gap** (Measure IDs 271-275, DAY4) — pre-flagged by the field team themselves
   in both `JimBay_Spatial.xlsx` and the DAY4 readme; carry this forward rather than re-discovering
   it.
8. **Hermit elevation discrepancy**: literature (research.md) says 1,950 m; files show 2,099-2,125 m
   for "Hermit Meadows" — ~150-175 m difference, needs researcher confirmation (possibly two related
   but distinct locations).
9. **Inconsistent instrument-folder naming** across days (GPS_pts/GPS/GPS pts; dku+ka/Radar_K;
   Fieldbook_photos variants) — recommend normalizing during Data Preparation.
10. **Day1 GPS format differs from all other days** (Gaia GPS iOS waypoints, no RTK, no usable
    elevation) vs. Emlid Reach RS2 RTK survey exports elsewhere.
11. **Two field participants not in the original team roster** (see README proposal below): Kate
    Hale (UBC) and Joachim Meyer (Boise State), named in the Day2 and DAY7 field readmes and as
    observer initials "KH"/"JM" in the DAY4 stratigraphy workbook.

---

## Proposed README.txt updates

*(For the human-in-the-loop orchestrator to apply — not edited directly here, per task instructions.
These are file-derived facts only; author/funding/methodology narrative belongs to Research's
proposal in `research.md`.)*

### Section: `DATA & FILE OVERVIEW` (currently `⚠️ [placeholder — to be filled at Step 6]`)

```
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
  no location fix; these are not real positions.
- GNSS survey files (.kml/.kmz/.csv, 6 files): spatial-transect point coordinates.
  ⚠️ 2026-03-03 uses a different GPS app/format than the other days and has no usable elevation.
- Fieldbook/snowpit photos (.heic/.jpg, 57 files) and hazard-assessment forms (.pdf, 10 files):
  supporting context, not instrument data.

🚩 File-naming conventions for instrument subfolders are not fully consistent across days (e.g.
GPS_pts vs GPS, dku+ka vs Radar_K) — researcher input needed on whether to normalize folder/file
names for the deposit package (decision for Data Preparation).
```

### Section: `4. Geographic location of data collection` — append after Research's proposed addition

```
⚠️ File-derived bounding box (from GNSS survey files, sentinel values excluded): latitude
51.23423 to 51.33108, longitude -117.70780 to -117.52996, elevation approximately 1,822-2,125 m
above sea level (WGS84).

⚠️ The Hermit Meadows elevation range confirmed from this campaign's own GNSS/pit data
(2,099-2,125 m) differs from the 1,950 m literature figure for the "Hermit" weather station
(research.md) by roughly 150-175 m — 🚩 please confirm whether these are the same location or two
distinct nearby sites.

🚩 Jim Bay: no published literature reference was found for this site name (research.md). File-derived
coordinates place it at approximately 51.234-51.235 N, -117.699 to -117.698 W, elevation 1,822-1,868 m.
Please confirm this is the intended site.
```

### Section: `2. Author Information` — addition to Research's proposal

```
⚠️ Two field participants appear directly in this campaign's own raw data (day readmes and
observer-initials fields in the stratigraphy workbooks) but are not in the original team roster
provided at Scope Definition: Kate Hale (present 2026-03-04 and 2026-03-09, per field readmes) and
Joachim Meyer (present 2026-03-04, initials "JM" recorded as an observer in
DAY4_JimBay-RoundHill-GopherButte_20260306/JimBayFullProfile.xlsx). 🚩 Confirm their role/affiliation
and whether they should be added as contributors/co-authors.
```

---

## Proposed metadata.yaml updates

```yaml
time_period:
  start: "2026-03-03"
  end: "2026-03-10"          # confirmed unchanged from draft — file-derived dates match exactly
collection_period:
  start: "2026-03-03"
  end: "2026-03-10"          # ⚠️ note in workflow/qc: 2026-03-07 and 2026-03-08 within this range have no data

geographic_coverage:
  place_name: "Rogers Pass, Glacier National Park"
  country: "Canada"
  province: "British Columbia"
  bounding_box:
    west: -117.70780
    east: -117.52996
    north: 51.33108
    south: 51.23423
  # elevation range 1822-2125 m (no dedicated elevation field in this schema; note in description text)

contributors:
  # File-derived, not yet in the roster provided at Scope Definition — role TBD, see README proposal above
  - name: "Kate Hale"
    role: "Data Collector"   # to confirm
  - name: "Joachim Meyer"
    role: "Data Collector"   # to confirm
```

---

## Outputs

- `notebooks/RogersPass_2025-2026_data_exploration.ipynb` — full inspection code + captured output,
  organized in the same 8 sections as this document.
- This file (`artifacts/data_exploration.md`).
- No direct edits made to `README.txt` or `metadata.yaml` (see proposals above) per the
  concurrent-Research-agent deviation instructions for this run.
