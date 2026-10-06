# Research — rogers_pass_snow_profiles, period 2025-2026

Extension research for version 2 (see `steps/extension.md`). Covers only what is new or changed since version 1 (`artifacts/2024-2025/research.md`, published as 10.20383/103.01634). Entries that still apply unchanged are listed under **Carried over**.

Sources: field readmes in `raw_data/2025-2026/` (`Readme_*.docx`, `GPS_pts/READ_ME.docx`, `Radar_K/READ ME.docx`, `Write in the Rain - table of content.docx`), file headers (radar), workbook sheet names, web sources listed in **Source notes**, and the earlier exercise on branch `rogerspass-2025-2026/scope-research-qc` (commit 44e55ec, `research.md`), whose claims were re-checked before reuse.

---

## Dataset overall description (what changes)

Second field campaign of the same GRIMP program at Rogers Pass, Glacier National Park: 2026-03-03 to 2026-03-10 (no data on 2026-03-07, rest day, and 2026-03-08, rest and filming day). Same objective as v1: multi-instrument snow profiles to validate radar retrievals of snow depth, stratigraphy and SWE against manual pits and penetrometers, in collaboration with Parks Canada's avalanche control program.

New in 2025-2026:

- **Dual Ku-band FMCW radar** (13 and 17 GHz), multi-angle measurements at full-profile sites and along spatial transects.
- **Blade Hardness Gauge (BHG)** measurements recorded in the stratigraphy workbooks.
- **Upper-snowpack stability profiles** (surface pits with stability tests) for a student project (Megan Cramb), at Round Hill, Gopher Butte and Hermit Meadows.
- **New sites:** Rogers Pass (full profile, 2026-03-05), Gopher Butte, Hermit Meadows (replaces "Hermit" from v1; to be confirmed as the same or a different site).
- **Expanded StratiTemplate:** linkage sheets for every instrument (`smp`, `Dual KU`/`dku`, `Radar K`, `SS`, `BHG`, `GPS`) in addition to v1's `AVY profile`, `Stability Tests`, `Density`, `IRIS`.
- **IRIS comparison:** two IRIS units (IRIS-2 and IRIS-3) compared at the Rogers Pass profile (2026-03-05; sheet `IRIS_3`).

Collected but not in the raw data folder (ancillary, not deposited):

- **Drone (UAV) flights** at Round Hill and Fidelity (2026-03-03 cancelled after RTK connection problems; 2026-03-05 partially flown, one flight line missing; 2026-03-09 not flown, missing propellers). No drone files in `raw_data/2025-2026/`.
- **Federal Sampler SWE measurements** at Jim Bay Corner by Kate Hale and Joachim Meyer (2026-03-06, stopped after the tool broke). No dedicated file found; check workbooks during Explore Data.

---

## Scope dimensions

### Spatial

| Site | 2025-2026 dates | Activities | Coordinates | Status |
|---|---|---|---|---|
| Round Hill | 03-03, 03-04, 03-05, 03-06, 03-10 | Full profile, 18-point spatial transect (03-03), upper-snowpack profiles, drone | to extract from GPS/workbooks | `to-be-confirmed-from-files` |
| Fidelity | 03-04 | Full profile, dual-Ku 30° measurements on the tower | Emlid base at Fidelity: 51.23628296 N, -117.70073797 W, ellipsoidal height 1866.417 m (manually entered) | `literature-derived` (field readme) |
| Gopher Butte | 03-04, 03-06 | Upper-snowpack stability profiles | to extract | `to-be-confirmed-from-files` |
| Rogers Pass | 03-05 | Full profile (165 cm), IRIS-2/IRIS-3 comparison | to extract | `to-be-confirmed-from-files` |
| Jim Bay Corner | 03-06 | Full profile (340 cm), 16-point spatial transect, Federal Sampler | to extract | `to-be-confirmed-from-files` |
| Hermit Meadows | 03-09 | Full profile, 24-point transect, 2 surface pits | to extract | `to-be-confirmed-from-files` |

Literature elevations from v1 research still apply for Fidelity (1905 m) and Round Hill (2100 m). "Hermit" (1950 m station in Madore 2023) vs "Hermit Meadows" (approx. 1100 m ascent from the highway per field readme): check whether they are the same location before merging site names across periods.

Ellipsoidal heights from the Emlid base (1866 m at Fidelity) differ from orthometric station elevations (1905 m); the README must state the height reference for each period.

### Temporal

- 2026-03-03 to 2026-03-10, six field days. `literature-derived` (field readmes, folder names)
- The Hermit Meadows readme is dated "11 mars 2026" while its folder and files say 2026-03-09: probably written two days later. `to-be-confirmed-from-files`
- The K-band radar clock was not set: `Radar_K` and `ka` files carry 2025-09-03/04 timestamps. Real dates come from folder names. Same unit as v1 (whose v1 timestamps were correct). `file-derived`

### Measurement domain

- Dual Ku-band radar: 12.5–14.5 GHz (13 GHz unit) and 16.5–18.5 GHz (17 GHz unit), 2 GHz bandwidth, V polarization, incidence angles 0–50° in 5° steps at full-profile sites, 30° on transects and on the Fidelity tower. `file-derived` (headers)
- K-band radar: 23.5–26 GHz, unchanged from v1. `file-derived`
- Full-profile depths: 165 cm (Rogers Pass), 340 cm (Jim Bay Corner); upper-snowpack profiles under 150 cm. `literature-derived` (field readmes)

---

## README input capture

### People (2025-2026 field team, from field readmes)

| Name | Affiliation (from readmes / v1) | Role in 2026 | In v1 author list |
|---|---|---|---|
| Jean-Benoit Madore | Université de Sherbrooke | Full profiles, coordination | yes |
| Alexandre Langlois | Université de Sherbrooke | Full profiles, drone team | yes |
| Benjamin Imbach | UQAR | Profiles, drone preparation | yes |
| Violaine Paquette | Université de Sherbrooke | Full profiles, transects | yes |
| Kate Hale | University of British Columbia | Stratigraphy (Rogers Pass), Federal Sampler | yes |
| Joachim Meyer | Boise State University | Upper snowpack, drone, Federal Sampler | yes |
| Nicolas Marchand | Université de Sherbrooke (to confirm) | Drone, profiles, transects | no |
| Nicolas Allet | Université de Sherbrooke (to confirm) | Transects, dual-Ku tower measurements | no |
| Megan Cramb | to confirm | Upper-snowpack stability profiles (student project) | no |
| Marie-Clara Delage | to confirm | Full profiles, IRIS-2/IRIS-3 comparison | no |

v1 authors not listed in 2026 readmes: Francis Gauthier, Francis Meloche, Hans-Peter Marshall, Julien Meloche.

Authorship of v2 (new authors, order) is a researcher decision; the PR reviewer is asked to complete and correct this list.

Not authors (context only): Parks Canada Avalanche Control Section (ACS) — morning meetings, avalanche control near study sites; a Radio-Canada film crew (*Découverte*) accompanied the team on 2026-03-09.

### Instruments (new or changed)

1. **Dual Ku-band FMCW radar (`dku`, "Dual KU")** — IMST sR13-12VHe (13 GHz, device 500230001) and sR17-12VHe (17 GHz, device 600230001) sensors, delivered to GRIMP in early 2025. Raw text files with a `# === Measurement Header ===` block (frequency, counter, site code, angle, polarization, UTC-like ISO timestamp, firmware, ramp settings, range bins) followed by chirp blocks of 4 RX channels. File naming: `<counter>_<13|17>GHz_<site code>_<point>_<pol>_<angle>deg.txt`. Protocol: multi-angle sweeps 0–50° at full-profile sites (11 angles), single 30° measurements along transects and on the Fidelity tower. Context: ground-based analog of the dual-frequency Ku-band SAR proposed for Canada's Terrestrial Snow Mass Mission (TSMM). Processing software: to ask the researcher.
2. **Blade Hardness Gauge (BHG)** — thin-blade penetration resistance gauge (Fraser Instruments), based on Borstad & McClung (2011). Recorded per layer in the `BHG` sheet (triplets of readings). Also requested in photos for the student project.
3. **GNSS** — Emlid receivers (base + rover) controlled with the Emlid Flow app, RTK fix, base coordinates entered manually at Fidelity. Receiver model not stated (do not assume). RTK link problems on 2026-03-03, so no GPS for the first Round Hill transect. v1 used RTK GPS as well (`spatial_reference/`); receiver model in v1 to compare.
4. **K-band FMCW radar** — unchanged unit (IMST sR1200-based, radar no. 2010000058, 23.5–26 GHz). New: stored in two folder names (`Radar_K`, `ka`); three measurements per transect point at three positions (Hermit Meadows); clock not set.
5. **IRIS** — unchanged method; two units (IRIS-2, IRIS-3) used and compared on 2026-03-05.
6. **SMP, SnowScope** — unchanged instruments and protocols (see v1). SnowScope linkage to transect points is incomplete at Jim Bay Corner (field readme: one missing SnowScope measurement, later ones hard to link).

### Standards and software (new)

- No new standard. OGRS and ICSSG still apply.
- Dual-Ku file reader: no public package identified; ask the researcher whether a GRIMP script exists to cite.

### Related publications and datasets (new since v1)

- No publication citing 10.20383/103.01634 was found (web search, 2026-10-06).
- Version 1 itself: `IsNewVersionOf` 10.20383/103.01634.

### Funding

v1 lists FRQNT and the Search and Rescue New Initiatives Fund. Funding for the 2026 campaign is not stated in the field files: ask the researcher (the IMST dual-Ku purchase may involve another grant, e.g. CFI).

### Unresolved README fields (2025-2026)

- v2 authors and order (researcher decision).
- 2026 funding.
- Dual-Ku processing software and whether data are raw only.
- Whether "Hermit Meadows" (2026) and "Hermit" (2025) are the same site.
- Whether drone and Federal Sampler data belong in this dataset (likely ancillary, not deposited).

---

## Citable references (new)

- Borstad, C. P., and McClung, D. M. (2011). Thin-blade penetration resistance and snow strength. *Journal of Glaciology*, 57(202), 325–336. https://doi.org/10.3189/002214311796405924 — BHG design basis.
- IMST GmbH (2025). Radar for polar research at Sherbrooke University (sR13-12VHe, sR17-12VHe Ku-band FMCW sensors). https://imst.com/news/radar-for-polar-research-at-sherbrooke-university.html — instrument description; a peer-reviewed reference should be requested from the researcher.
- Derksen, C., et al. (2019). Terrestrial Snow Mass Mission (TSMM) concept — cited in Madore (2023), pp. 117–118; full reference to obtain if the README mentions TSMM.

Carried over from v1 (unchanged): Montpetit et al. (2012) IRIS; Schneebeli & Johnson (1998), Schneebeli et al. (1999) SMP; Hagenmuller et al. (2024) SnowScope; Pomerleau et al. (2020) K-band radar; OGRS; ICSSG; `snowmicropyn`.

---

## Glossary (new terms)

| Term | Tag | Detail |
|---|---|---|
| Dual Ku (`dku`) | instrument | IMST sR13-12VHe / sR17-12VHe FMCW sensors, 12.5–14.5 and 16.5–18.5 GHz, 2 GHz bandwidth (~7.5 cm range resolution per manufacturer), H/V capable, V used in 2026. Multi-angle 0–50°. |
| BHG | instrument | Blade Hardness Gauge, thin-blade penetrometer (Borstad & McClung, 2011); force readings per layer, three insertions. |
| Emlid Flow | instrument | Emlid field app controlling an RTK base/rover pair; base coordinates entered manually. |
| Upper-snowpack stability profile | technique | Surface pit (< 1.5 m) with stability tests (CT, ECT) focused on slab conditions; 2026 student project. |
| Federal Sampler | instrument | Snow tube sampler for SWE; used briefly at Jim Bay Corner in 2026, tool broke. |
| Site codes (`RHFP`, `RHUT`, ...) | acquisition | Site/profile codes in dual-Ku file names (e.g. RHFP = Round Hill full profile, RHUT = Round Hill transect?). Full list to build in Explore Data. |
| ACS | organization | Parks Canada Avalanche Control Section, Glacier National Park. |

---

## Source notes

| Claim | Source |
|---|---|
| Team per day, roles, sites, drone and Federal Sampler events, transect sizes (18, 16, 24 points), profile depths | `raw_data/2025-2026/*/Readme_*.docx` |
| Emlid base coordinates and RTK fix mode | `Day2_Fidelity_RH_04-03-2026/GPS_pts/READ_ME.docx` |
| Three K-band measurements per transect point | `DAY7_HermitMeadows_20260309/Radar_K/READ ME.docx` |
| Field book page index per day | `Write in the Rain - table of content.docx` |
| Dual-Ku frequency ranges, device numbers, polarization, angles | dual-Ku file headers (`# === Measurement Header ===`) |
| K-band radar serial, band, wrong clock; `ka` = same unit | `Radar_K/` and `ka/` file headers vs `published/v1/radar_FMCW_K/` |
| IMST sR13-12VHe / sR17-12VHe delivered to GRIMP, 2 GHz bandwidth, 7.5 cm resolution, H/V | https://imst.com/news/radar-for-polar-research-at-sherbrooke-university.html (2025-02-11) |
| BHG based on Borstad & McClung (2011) | https://doi.org/10.3189/002214311796405924; earlier exercise (44e55ec) |
| TSMM context for dual-Ku | Madore (2023) PhD thesis pp. 117–118, via 44e55ec research |
| No citing publication for v1 DOI | web search 2026-10-06 |
| Workbook sheet sets | `openpyxl` sheet listing of `raw_data/2025-2026/**/*.xlsx` and `published/v1/**/*.xlsx` |

---

## Carried over from v1 (`artifacts/2024-2025/research.md`)

Still valid without change: dataset context and objectives; GRIMP and Parks Canada collaboration; IRIS, SMP, SnowScope, K-band radar descriptions and citations; OGRS/ICSSG standards; `snowmicropyn`; license (CC BY-NC 4.0); site descriptions for Fidelity, Round Hill, Jim Bay Corner.

Not applicable to 2025-2026: Christiana Ridge (no 2026 visit).

---

## README updates

- None applied yet. New instrument paragraphs (dual Ku, BHG, Emlid GNSS, upper-snowpack profiles) and the 2026 team go into README at Step 6, once Explore Data and QC have confirmed file coverage. Authors and funding stay open for the researcher.
