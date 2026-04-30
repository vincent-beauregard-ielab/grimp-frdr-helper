
# Quality Control Report: Rogers Pass Snow Profiles

**Date:** 2026-03-24 (researcher review applied 2026-04-28; preparation update applied 2026-04-29)
**Status:** Researcher review applied (PR #2). All Open items resolved.

## Issues

| Issue | Status | Action |
|---|---|---|
| Raw folders use spaces, mixed case, and inconsistent site tokens | Resolved | Prepared package uses standardized FRDR folder names |
| Day 1 IRIS file naming differs from Days 2-6 | Resolved | Renamed to `20250301_fidelity_iris_raw.txt` |
| Day 6 SnowScope folder typo uses `20240306` and `christridge` | Resolved | Prepared folder is `20250306_christiana_ridge_snowscope` |
| DOCX field notes are not deposit-friendly | Resolved | Converted eight DOCX files to UTF-8 TXT |
| Scientific and administrative material are mixed in raw package | Resolved | Only in-scope scientific/support files were copied to `frdr_data/` |
| Day 6 Fidelity stratigraphy workbook may be misfiled or a revisit | Resolved | Confirmed revisit at same Fidelity site five days after Day 1; kept with `_revisit` filename (PR #2). |
| Radar band terminology (`radar_k` vs `radar_ka`) is inconsistent | Resolved | Folder standardized to `radar_FMCW_K`; band confirmed K-band, center 24.5 GHz (PR #2). |
| Hazard assessment PDFs are still undecided | Resolved | Excluded as out of scope per researcher review (PR #2). |
| Some raw SMP headers contain invalid GPS sentinels | Resolved | Prepared `.pnt` copies are byte-identical to raw files; sentinel values are documented for interpretation |
| Some template-derived workbook cells contain placeholder zeros | Resolved | Prepared stratigraphy workbooks clear blank density-template formulas and materialize observed density values |

## Raw-data issue details and cleanup starting points

The table above records the preparation decision. The sections below describe the raw-data problems in more detail and provide conservative cleanup starting points. In all cases, `raw_data/` should remain the unmodified source of record. Cleanup should be reproducible from the raw files into `frdr_data/` and documented in the README/QC artifacts.

## SMP GPS header sentinels

SMP `.pnt` files are proprietary binary SnowMicroPenetrometer files. Each file has a fixed-size binary header before the force samples. The header stores metadata such as timestamp, SMP serial number, WGS84 latitude, WGS84 longitude, WGS84 height, hemisphere flags, and instrument settings.

A header sentinel is a placeholder value written into a metadata field when the instrument or export software does not have a valid value. It is not an observed coordinate. In these raw SMP files, the sentinel value is `99999`, stored in GPS-related header fields:

- `gps.wgs84.latitude`: expected valid range is -90 to 90 degrees.
- `gps.wgs84.longitude`: expected valid range is -180 to 180 degrees.
- `gps.wgs84.height`: stored as height in centimetres; `99999` indicates no valid height rather than a real elevation.
- Hemisphere flags for the seven files with invalid latitude/longitude are `A` / `A`, rather than `N` / `W`.

Note: the binary value is stored as `99999`; some readers may report the latitude or longitude as `-99999` after applying invalid hemisphere flags. Either representation should be interpreted as the same missing-coordinate sentinel, not as a real coordinate.

Raw-data findings:

| Raw field | Raw value observed | Affected files | Interpretation |
|---|---:|---:|---|
| WGS84 latitude | `99999` | 7 of 79 `.pnt` files | Invalid coordinate sentinel |
| WGS84 longitude | `99999` | 7 of 79 `.pnt` files | Invalid coordinate sentinel |
| WGS84 height | `99999` | 79 of 79 `.pnt` files | Missing height sentinel |

The seven raw files with invalid latitude and longitude are:

- `Jour 1 - Fidelity/Fidelity Radars and SMP/S35M0129.pnt`
- `Jour 1 - Fidelity/Fidelity Radars and SMP/S35M0131.pnt`
- `Jour 2 - Jim Bay/Spatial Survey - SMP and Radar K/SMP/S35M0133.pnt`
- `Jour 5 - Round Hill/Spatial Survey/SMP/S35M0192.pnt`
- `Jour 5 - Round Hill/Spatial Survey/SMP/S35M0194.pnt`
- `Jour 5 - Round Hill/Spatial Survey/SMP/S35M0196.pnt`
- `Jour 6 - RoundHill and Christiana Ridge/SMP/S35M0205.pnt`

Cleanup starting point from raw untransformed data:

- Copy `.pnt` files byte-for-byte into `frdr_data/`; do not edit proprietary SMP binaries during preparation.
- Document the `99999` GPS header sentinels in the README and QC report so users do not interpret them as real coordinates or elevations.
- Coordinates should not be invented inside the `.pnt` files. If linkage workbooks or GPS CSV files provide measurement locations, describe that relationship in the documentation rather than overwriting SMP binary headers.

## Stratigraphy workbook density placeholder zeroes

The placeholder-zero issue comes from the `Density` sheet in the seven stratigraphy workbooks. The relevant columns are:

- Column A: `Height`.
- Column B: `Weight (g)`.
- Column C: `Density (kg.m3)` or equivalent label.

The template computes density in column C from the source weight in column B. Most formulas are of the form `=B{row}*4`. When column B is blank, Excel evaluates the formula as `0`, which can look like an observed density of zero even though no sample weight was recorded. These zeroes are template-derived calculation artifacts, not field observations.

Raw-data findings:

| Prepared workbook name | Raw workbook source | Blank source-weight formulas | Observed formulas |
|---|---|---:|---:|
| `20250301_fidelity_stratigraphy.xlsx` | `Jour 1 - Fidelity/Strati_20250301_fidelity.xlsx` | 10 | 19 |
| `20250302_jim_bay_corner_stratigraphy.xlsx` | `Jour 2 - Jim Bay/20250302_JimBay_StratiTemplate.xlsx` | 9 | 20 |
| `20250303_hermit_stratigraphy.xlsx` | `Jour 3 - Hermit/20250303_Hermit.xlsx` | 9 | 20 |
| `20250304_fidelity_stratigraphy.xlsx` | `Jour 4 - Fidelity/20250304_StratiTemplate.xlsx` | 9 | 18 |
| `20250305_round_hill_stratigraphy.xlsx` | `Jour 5 - Round Hill/20250305_Strati.xlsx` | 5 | 24 |
| `20250306_christiana_ridge_stratigraphy.xlsx` | `Jour 6 - RoundHill and Christiana Ridge/CRidge_Strati_20250306.xlsx` | 16 | 13 |
| `20250306_fidelity_revisit_stratigraphy.xlsx` | `Jour 6 - RoundHill and Christiana Ridge/Fidelity_Strati_20250306.xlsx` | 29 | 0 |

Examples of template-derived blank-source formulas include `Density!C41 =B41*4`, `Density!C45 =B45*4`, and `Density!C53 =B53*4` where the corresponding `Weight (g)` cell in column B is blank. One malformed-looking raw formula also appears in `20250304_fidelity_stratigraphy.xlsx`: `Density!C5 =B7*4`; because its source weight is blank, the cleanup treats it as a blank template formula rather than an observation.

Cleanup starting point from raw untransformed data:

- Preserve the original workbooks in `raw_data/`.
- For prepared workbook copies, clear `Density` sheet column C formulas when the referenced/source `Weight (g)` cell is blank.
- For formulas with a recorded weight in column B, either leave the formula intact or materialize it as a numeric density value; if materialized, document the conversion so downstream users know the value was calculated from the recorded weight.
- Do not treat a displayed `0` from a blank-source formula as a measured density value.
