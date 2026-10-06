# Data exploration — rogers_pass_snow_profiles, period 2025-2026

Source notebook: `notebooks/data_exploration_2025-2026.ipynb` (built by `scripts/build_exploration_notebook_2025-2026.py`, executed end to end). Inputs: `raw_data/2025-2026/` (read-only) and the published v1 baseline `published/v1/` (read-only). Literature context: `artifacts/2025-2026/research.md`.

---

## 1. Inventory

567 files in 8 day folders (two without data: `DAY5_RestDay_20260307` is empty, `DAY6_ReposeEtFilm_20260308` holds one hazard PDF and photos only), `templates/`, and one root file.

| Class | Files | In scope | Notes |
|---|---|---|---|
| Dual Ku-band radar (`dku`) | 175 | yes | new instrument; 5 empty files |
| K-band radar (`Radar_K`, `ka`) | 141 | yes | same unit as v1; 2 empty files |
| SnowScope CSV | 89 | yes | |
| SMP `.pnt` | 48 | yes | |
| Stratigraphy workbooks | 14 | yes | expanded template |
| IRIS TXT | 13 | yes | two formats (see §4) |
| Field readmes / notes (`.docx`) | 8 | yes, converted to text as in v1 | 6 day readmes, GPS readme, K-band readme, field-book index |
| GNSS exports (KML, KMZ, CSV) | 6 | yes | |
| Spatial linkage workbooks | 4 | yes | |
| Photos (HEIC/JPG) | 57 | no | v1 precedent |
| Hazard / risk assessment PDFs | 9 | no | v1 precedent |
| Templates | 3 | no | blank StratiTemplate, hazard form, photo checklist |
| **Total** | **567** | **498** | |

Empty (0-byte) files: `Day1/ka/03_03_2026/000020250903_1636.txt`, `…/000120250903_1637.txt`, `Day2/dku/0831_13GHz_FITO_01_V_30deg.txt`, `0831_17GHz_FITO_01…`, `0832_13GHz_FITO_02…`, `DAY4/dku/0862_13GHz_JBTR_15…`, `0862_17GHz_JBTR_15…`.

## 2. Stratigraphy workbooks (StratiTemplate)

14 workbooks (+ blank template). Count confirmed against the earlier exercise (14, not 15).

**Template change since v1.** v1 workbooks have 4 sheets (`AVY profile`, `Stability Tests`, `Density`, `IRIS`). 2025-2026 workbooks add instrument linkage sheets, with inconsistent names across files:

| Content | Sheet names found |
|---|---|
| Blade hardness gauge | `BHG` (11 files) |
| SMP linkage | `smp` (10) |
| Dual-Ku linkage | `dku` (3), `Dual KU` (5) |
| K-band linkage | `Radar K` (5), `RadarK` (1), `Radar K GPS` (1) |
| SnowScope linkage | `SS` (9), `SnowScope` (1), `Snowscope` (1) |
| GNSS | `GPS` (1) |
| Second IRIS unit | `IRIS_3` (1) |

The `AVY profile` layer table keeps the v1 columns (`HEIGHT, RESISTANCE, FORM, EXTENT, Ѳ (LWC), WEIGHT, DENSITY, COMMENTS & TEST DATA, TEMPERATURE`) in 11 workbooks; one upper-snowpack workbook uses a variant with `BHG`, `IRIS Depth`, `Irish Value` columns; two have the header row shifted.

**Header fields (`AVY profile`)** — values as found:

| Workbook | Date | Elevation | Location / observers | Remark |
|---|---|---|---|---|
| `RoundHill.xlsx` | 2026-03-03 | blank | JM-AL | header shifted (ELEVATION reads "SKY") |
| `uppersnowpackstability.xlsx` | 2026-03-03 | 2040 | MC | |
| `FidelityStation_2023-03-04.xlsx` | 2026-03-04 | 1905 | MCD, AL, VP, NA | **file name says 2023** |
| `GopherButte_2026-03-04.xlsx` | 2026-03-04 | 1930 | Gopher Butte; MC, KH, JM | |
| `RoundHill_bottom.xlsx` | **2026-04-03** | blank | jb | **day/month swapped** (Day 2 = 2026-03-04) |
| `20260305_RogersPass.xlsx` | 20260305 | blank | NA, KH, JBM, MCD | date as number |
| `20260305_Round Hill Upper Snowpack.xlsx` | 20260305 | 2058 | | |
| `GopherButte_upperSnowpack.xlsx` | 2026-03-06 | 1925 | **"Fidelity"**; MC, JBM | location contradicts file name |
| `JimBayFullProfile.xlsx` | 20260306 | 1868 | NM-AL | |
| `RoundHill_upperSnowpack.xlsx` | 20260306 | 2052 | BI, JBM, MC | |
| `2026-03-09_Hermit_SurfacePit1_StratiTemplate.xlsx` | 2026-03-09 | 2125 | Hermit Meadow; MC, KH | |
| `2026-03-09_Hermit_SurfacePit2_StratiTemplate.xlsx` | — | — | — | **header empty**; only Density/IRIS rows beyond template defaults (see QC) |
| `20260309_HermitMedow.xlsx` | 2026-03-09 | 2113 | "Hermit Medow"; BI, AL, JBM | spelling |
| `20260310_Round Hill upper snowpackl.xlsx` | 20260310 | blank | Round Hill; MC, MS, NaA, KH | "MS" not in team list |

Date formats mix datetime cells and `YYYYMMDD` numbers. Observer initials "MS" and "NaA" are not in the readme team list (to ask).

## 3. Instrument linkage

Spatial workbooks map transect points to instrument identifiers:

| Workbook | Points | Columns | Identifiers missing on disk (same day) |
|---|---|---|---|
| `Spatial_Round_Hill.xlsx` (03-03) | 21 rows / 18 points | GPS, Dual KU, Radar K, SMP, SS, HS1–3 | none |
| `JimBay_Spatial.xlsx` (03-06) | 18 | GPS, Dual KU, Radar K, SMP, SS, HS | Dual KU 846, 860; SMP 784 |
| `20260309_HermitMeadow_Spatial.xlsx` | 24 | GPS, Radar K 1–3, SS, HS 1–3 | none |
| `20260310_RoundHill_Spatial.xlsx` | 18 | GPS, Radar K, Dual KU, HS | Dual KU 862 (exists on Day 4, not Day 8; Day 8 counters 863–880) |

Workbook linkage sheets: `RoundHill.xlsx` and `RoundHill_bottom.xlsx` `dku` sheets reference counters 780–789 that exist nowhere (real ranges 790–800 Day 1, 819–829 Day 2) — same finding as the earlier exercise (A2). Other unresolved references: SMP 170 (`RoundHill.xlsx`), 756 (`FidelityStation…`), 764–766 (`20260305_RogersPass.xlsx`, no SMP files at all on Day 3), 773–774 (`JimBayFullProfile.xlsx`); dual-Ku 818 (`FidelityStation…`, belongs to Day 1), 68 and 832 (`JimBayFullProfile.xlsx`). The linkage check uses a crude numeric filter; QC must confirm each case.

## 4. IRIS

13 TXT files, two formats **by unit**, not by period:

- IRIS-2: 4 columns `date, time, "IRIS", voltage` (6 files).
- IRIS-1 and IRIS-3: 2 columns `time, voltage` (7 files) — same as all v1 files.

Voltages 0.10–2.04 V. Rows 18–126 per file. File naming is free-form (`IRIS2_20260303_fullProfile.TXT`, `IRIS#1-Gopher Butte TP/20260304.TXT`, `IRIS2 _HermitMedow.TXT`); unit number is in the name or folder.

## 5. SMP

48 `.pnt` profiles (Day 1: 26, Day 2: 6, Day 4: 16), all SMP serial 35 (`S35M0732`–), read with `snowmicropyn`. 211,389–411,400 samples, max depth 1700 mm. Timestamps in UTC, consistent with folder dates. GPS in header for 46 profiles; `S35M0736` and `S35M0782` have the no-fix sentinel (-99999).

## 6. SnowScope

89 CSV profiles, serials 00249 and 00374 (v1: 00304, 00328), creators Benjamin Imbach (53) and Megan Cramb (36). Profile depths 442–2462 mm.

Format vs v1: two new header keys (`Max Profile Speed (m/s)`, `Profile Time (sec)`); third table column is unnamed and **empty in all 89 files** (v1: `optical Reflectance Avg` filled in 181 of 319 files). Collection time is in local time with time-zone name in text.

Location: 7 profiles (Day 2: 3, Day 4: 4) carry a location 45 km east (51.4155, -117.0087, app elevation 806 m) — stale phone position, excluded from the extent. The 4 Day 3 profiles at 51.3013, -117.5160 (1303 m) are the **Rogers Pass** full-profile site, not outliers.

## 7. K-band radar

141 files with content + 2 empty, all radar no. 2010000058, 23.5–26 GHz, 513 samples — identical unit and settings to v1 `radar_FMCW_K/`. Stored as `ka/` (Days 1, 2, 4) and `Radar_K/` (Days 7, 8) — **one instrument, two folder names** (user expectation confirmed). Subfolders are named `DD_MM_YYYY`; Day 7 subfolder reads `10_03_2026` and Day 8 `11_03_2026`, one day later than the day folders. **Clock not set**: file names and headers carry 2025-09-03 (`ka`) / 2025-09-04 (`Radar_K`); real dates come from day folders. Hermit Meadows: three measurements per transect point (72 files / 24 points).

## 8. Dual Ku-band radar (new)

175 files, all matching `<counter>_<13|17>GHz_<site>_<point>_<pol>_<angle>deg.txt`. Two IMST sensors: device 500230001 (13 GHz, 12.5–14.5 GHz) and 600230001 (17 GHz, 16.5–18.5 GHz); polarization V only; 50 chirps per file (4 RX channels); timestamps ISO, UTC, consistent with folder dates.

| Day | Site code | Meaning (inferred) | Files | Counters | Angles |
|---|---|---|---|---|---|
| 03-03 | RHFP | Round Hill full profile | 22 | 790–800 | 0–50° by 5° |
| 03-03 | RHTR | Round Hill transect | 36 | 801–818 | 30° |
| 03-04 | FIFP | Fidelity full profile | 22 | 819–829 | 0–50° |
| 03-04 | FITO | Fidelity tower | 5 (+ empty) | 830–832 | 30° |
| 03-06 | JBFP | Jim Bay full profile | 24 | 833–844 | 0–50° |
| 03-06 | JBTR | Jim Bay transect | 30 | 847–862 | 30° |
| 03-10 | RHUT | Round Hill upper transect | 36 | 863–880 | 30° |

Counter 832 has only the 13 GHz file. No dual-Ku data on Days 3 and 7 (consistent with readmes).

## 9. GNSS

Emlid Reach RS2, RTK FIX (Hermit CSV: 24/24 FIX, horizontal RMS ~0.01 m). Exports: KMZ (Day 1, 19 points, 17 without height), KML (Days 2, 4, 7, 8), CSV (Day 7 only). Ellipsoidal heights 1822–2110 m. v1 used the same Emlid CSV export (2025-2026 adds `Code description`, `Device serial number`, `Device type`). No CSV exists for Days 1, 2, 4, 8 (KML only, fewer attributes). No GPS for the Rogers Pass profile (Day 3) other than SnowScope app positions.

## 10. Scope dimensions (file-derived)

**Sites and coordinates (WGS84, EPSG:4326):**

| Site | Day(s) | Lat | Lon | Elevation (m) | Source |
|---|---|---|---|---|---|
| Round Hill | 03-03, 03-05, 03-06, 03-10 | 51.2350–51.2353 | -117.7078 to -117.7070 | 2024–2059 (SnowScope/workbook), 2038–2044 ellips. | GNSS, SMP, SnowScope |
| Fidelity | 03-04 | 51.2364–51.2365 | -117.7009 to -117.7007 | 1864 ellips., 1905 workbook | GNSS, SMP |
| Gopher Butte | 03-04, 03-06 | ~51.24 | ~-117.70 | 1919–1930 | SnowScope, workbook |
| Rogers Pass | 03-05 | 51.3013 | -117.5160 | ~1303 | SnowScope app only |
| Jim Bay Corner | 03-06 | 51.2342–51.2347 | -117.6993 to -117.6987 | 1822–1873 | GNSS, SMP, workbook |
| Hermit Meadows | 03-09 | 51.3304–51.3311 | -117.5309 to -117.5300 | 2099–2125 | GNSS, workbook |

**Bounding box 2025-2026:** west -117.7078, east -117.5160, south 51.2342, north 51.3311.
**Combined with v1** (v1: W -117.7304, S 51.2274, E -117.4670, N 51.3284): **W -117.7304, S 51.2274, E -117.4670, N 51.3311**.
**Elevation 2025-2026:** ~1303–2125 m (Rogers Pass lowest). Combined: 1303–2125 m. Heights mix ellipsoidal (GNSS), app (SnowScope) and workbook values; the README must state this.

**Temporal:** 2026-03-03, 03-04, 03-05, 03-06, 03-09, 03-10 confirmed from SMP, dual-Ku and IRIS timestamps. No data 03-07, 03-08. K-band radar dates unusable (clock).

**Measurement domain:** dual-Ku 12.5–18.5 GHz, K-band 23.5–26 GHz, 0–50° incidence; snow depth to 3.40 m (Jim Bay full profile, readme) and HS columns in spatial workbooks; SMP to 1.7 m; SnowScope to 2.46 m.

## 11. Cross-period comparison (v1 → 2025-2026)

| Aspect | v1 (published) | 2025-2026 raw | Consequence for packaging |
|---|---|---|---|
| Instrument folders | iris, radar_FMCW_K, snow_stratigraphy, snowmicropenetrometer, snowscope, spatial_reference, documentation | same classes + **dual-Ku** | add a `radar_FMCW_dual_Ku/` folder (name to decide) |
| K-band folder name | `radar_FMCW_K/` | `ka/`, `Radar_K/` | harmonize to `radar_FMCW_K/` |
| K-band dates | correct in file | clock wrong (2025-09) | document; keep raw names or rename with real dates (decision) |
| Folder naming | `<datatype>/<YYYYMMDD>_<site>` | day folders, free-form | apply v1 convention |
| Stratigraphy template | 4 sheets | 6–9 sheets, inconsistent names | keep content; document sheet names; consider harmonizing names in prepared copies |
| IRIS format | 2 columns | 2 or 4 columns (by unit) | document both formats |
| SnowScope format | reflectance column (181/319 files) | reflectance always empty; 2 new header keys | document |
| SnowScope serials | 00304, 00328 | 00249, 00374 | document |
| GNSS | Emlid CSV + zipped shapefile | KML/KMZ (+1 CSV) | decide: export CSV from KML for consistency, or deposit KML |
| Spatial linkage | `*_spatial_linkage.xlsx` | `*Spatial*.xlsx` + linkage sheets in workbooks | rename to v1 convention |
| Field notes | `.txt` (converted, French) | `.docx` (French) | convert to `.txt` as in v1 |
| Sites | Fidelity, Jim Bay Corner, Hermit, Round Hill, Christiana Ridge | + Rogers Pass, Gopher Butte, Hermit Meadows (≠ Hermit, ~800 m north) | site list per period in README |
| Elevation range | 1832–2088 m | 1303–2125 m | update README/METADATA |

## 12. Discrepancies and items for QC

1. Empty files: 2 K-band, 5 dual-Ku.
2. K-band radar clock wrong; subfolder dates of Days 7 and 8 one day off.
3. Dual-Ku linkage 780–789 in two workbooks (no such files) — earlier exercise A2.
4. Other unresolved linkage references (§3).
5. `RoundHill_bottom.xlsx` date 2026-04-03 (day/month swap).
6. `FidelityStation_2023-03-04.xlsx` file name year.
7. `GopherButte_upperSnowpack.xlsx` LOCATION "Fidelity".
8. `Hermit_SurfacePit2` header empty (earlier exercise A3).
9. `GopherButte_2026-03-04.xlsx` stability tests identical to `RoundHill.xlsx` (earlier exercise A1) — to re-verify in QC.
10. SnowScope stale location (7 files); reflectance column empty.
11. SMP no-fix GPS in 2 files.
12. Day 1 KMZ: 17/19 points without height.
13. No GNSS for the Rogers Pass profile; elevation only from the SnowScope app.
14. Observer initials "MS", "NaA" not in team list.
15. Inconsistent linkage sheet names.

## Scope updates

- Elevation range extended to ~1303 m (Rogers Pass site, valley floor) — README §4 and `METADATA.yaml` updated.
- Bounding box north edge 51.3311 confirmed (Hermit Meadows); east edge unchanged from v1.
- "Hermit" (v1) and "Hermit Meadows" (2026) kept as distinct sites.
- `ka` confirmed as the K-band radar, not a new instrument.

## README updates

- §4 Geographic location: 2025-2026 extent and elevation range replaced by file-derived values.
