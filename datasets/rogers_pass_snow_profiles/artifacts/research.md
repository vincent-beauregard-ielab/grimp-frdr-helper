# Research — Rogers Pass Snow Profiles

**Status:** Done
**Dataset id:** rogers_pass_snow_profiles
**Primary source:** `papers/madore_jean-benoit_PhD_2023.pdf`

---

## Dataset overall description

This dataset contains multi-instrument snow profile observations collected during an intensive six-day field campaign (2025-03-01 to 2025-03-06) at Rogers Pass, Glacier National Park, British Columbia, Canada. The campaign was conducted by the Groupe de Recherche Interdisciplinaire sur les Milieux Polaires (GRIMP) at Université de Sherbrooke in collaboration with Parks Canada's Avalanche Control Program at Glacier National Park.

Rogers Pass, located in the Selkirk Mountains of British Columbia, is one of the snowiest inhabited areas in Canada, with snow depths regularly exceeding 4 m at upper elevations. Parks Canada has operated the world's largest mobile artillery avalanche control program at Rogers Pass since 1961, protecting the Trans-Canada Highway and Canadian Pacific Railway from avalanche hazards. The Mount Fidelity snow study plot (1905 m elevation) is a long-standing reference site for snowpack monitoring in the area.

The dataset captures the physical state of the seasonal snowpack using five complementary measurement systems: traditional snow stratigraphy profiles (StratiTemplate Excel workbooks), infrared integrating sphere (IRIS) observations for snow specific surface area, SnowMicroPenetrometer (SMP) high-resolution hardness profiles, Snow Scope Probe digital penetrometer profiles for rapid spatial hardness surveys, and frequency-modulated continuous-wave (FMCW) K-band radar measurements for snow depth and snow water equivalent retrieval. Observations were collected at five study sites: Fidelity, Jim Bay Corner, Hermit, Round Hill, and Christiana Ridge.

GRIMP was founded in 2014 by Professor Alexandre Langlois at the Department of Applied Geomatics, Université de Sherbrooke. The group is affiliated with CARTEL (Centre d'applications et de recherches en télédétection) and the Centre d'études nordiques (CEN). GRIMP's avalanche research axis focuses on avalanche hazard assessment, snow profile observation, and stability testing, with a long-standing collaboration with Parks Canada at Rogers Pass.

The methodology for stratigraphy, IRIS, SMP, and radar follows the same protocols documented in Madore (2023), an integrated study of water percolation in the snowpack at Glacier National Park. The 2025 campaign extends earlier fieldwork (2018-2019 seasons) at the same general study area, adding the Snow Scope Probe (Propagation Labs) as a new instrument not present in the 2018-2019 campaigns.

---

## README input capture

### Title
Snow profile observation datasets, Rogers Pass, Glacier National Park, British Columbia, Canada

### People and institutions

| Role | Name | Affiliation | ORCID |
|------|------|-------------|-------|
| Lead author | Jean-Benoit Madore | Université de Sherbrooke, Dept. géomatique appliquée; Centre d'études nordiques | 0000-0002-2292-1519 |
| Lead author / Supervisor | Alexandre Langlois | Université de Sherbrooke, Dept. géomatique appliquée; GRIMP; Centre d'études nordiques | 0000-0002-9966-205X |
| Author (tentative) | Benjamin Imbach | UQAR | TBD |
| Author (tentative) | Francis Gauthier | UQAR | TBD |
| Author (tentative) | Julien Meloche | Université de Sherbrooke | TBD |
| Author (tentative) | Cécile Meyer | Université de Sherbrooke | TBD |
| Author (tentative) | Rachel Hale | TBD | TBD |
| Author (tentative) | Maxime Paquette | Université de Sherbrooke | TBD |
| Collaborator | Parks Canada — Avalanche Control Program, Glacier National Park | Government of Canada | — |

**Contact:** Jean-Benoit Madore (email TBD from researcher)

### Collection dates
2025-03-01 to 2025-03-06 (6 field days)

### Geographic coverage
- **Place name:** Rogers Pass, Glacier National Park, Selkirk Mountains, British Columbia, Canada
- **Country:** Canada
- **Province:** British Columbia
- **Sites:** Fidelity (~1905 m), Jim Bay Corner, Hermit, Round Hill, Christiana Ridge
- **Bounding box:** TBD — to be extracted from GPS/shapefile data in Explore Data step

### Instruments and acquisition protocols

#### 1. Snow stratigraphy profiles (StratiTemplate)

Traditional manual snow pit observations recording layer-by-layer snow properties: grain type and size (classified per ICSSG, Fierz et al. 2009), hand hardness, temperature profile, density profile (by cutting known-volume samples and weighing), wetness, and layer boundaries. Observations follow the Canadian Avalanche Association's Observation Guidelines and Recording Standards (OGRS; CAA, 2016). Data are recorded in StratiTemplate, an Excel-based snow stratigraphy workbook. One workbook per site-day; 7 files total.

#### 2. InfraRed Integrating Sphere (IRIS)

The IRIS is a laser-based instrument that measures shortwave infrared (SWIR) hemispherical reflectance (albedo) of snow samples using an integrating sphere at wavelengths of 1310 nm and 1550 nm. From these reflectance measurements, snow specific surface area (SSA, in m^2/kg) and optical equivalent grain size are derived. The instrument was designed and validated by Montpetit et al. (2012), who reported measurement accuracy of ~7% compared to X-ray micro-computed tomography reference measurements, with good reproducibility for snow densities above 200 kg/m^3. Measurements are taken at each layer identified in the snow pit wall. One TXT output file per field day; 6 files total.

#### 3. SnowMicroPenetrometer (SMP)

The SMP is a portable, motor-driven, high-resolution snow penetrometer developed at the WSL Institute for Snow and Avalanche Research SLF (Schneebeli & Johnson, 1998; Schneebeli et al., 1999). It drives a conical tip (5 mm diameter, 60-degree included angle) into the snowpack at a constant speed of 20 mm/s, recording penetration resistance force (0-42 N range) at 4-micrometer intervals (250 measurements per millimeter, 5 kHz sampling rate). The effective layer resolution is approximately 1.8 mm. The SMP provides an objective, high-resolution record of snowpack mechanical stratigraphy that complements the manual snow pit profile. Output files are in proprietary .pnt binary format. Multiple profiles per site-day; 79 files total.

#### 4. Snow Scope Probe (SnowScope)

The Snow Scope Probe is a digital snow penetrometer manufactured by Propagation Labs. It consists of a sensor "bullet" attached to a collapsible probe (similar in size and weight to an avalanche probe; 385 g for 220 cm, 475 g for 300 cm). When probed into the snowpack, it measures depth-resolved snow hardness using force sensors sampling at over 5000 Hz. The instrument produces hardness profiles (3-550 kPa range) with a depth resolution of approximately 3 mm (minimum identifiable layer thickness 1.5 mm) and a hardness resolution of 3 kPa. Depth error is typically 2.3% mean and 5% maximum. An optional optical reflectance channel records near-infrared backscatter at each depth step. Data are transmitted wirelessly to the companion Snow Scope App (iOS/Android) and exported as CSV files with a 21-field metadata header (serial number, firmware version, PCB version, GPS coordinates, collection time, profile depth) followed by a depth-resolved measurement table.

The 2025 campaign used three Snow Scope units (serial numbers 00304, 00322, 00328; firmware 2.4.1; PCB v2.7), operated by Francis Gauthier (UQAR). A total of 319 CSV profiles were collected across five site-days. Of these, 181 files include the optical reflectance channel and 138 do not. Profile depths range from 81 to 2266 mm.

The Snow Scope Probe is new to the 2025 campaign and was not part of the instrument suite described in Madore (2023). An independent evaluation of the instrument was presented by Hagenmuller et al. (2024) at the International Snow Science Workshop (ISSW) in Tromsø, Norway.

#### 5. K-band FMCW radar

A compact 24 GHz frequency-modulated continuous-wave (FMCW) radar, based on the commercial IMST Sentire sR-1200 Series module (IMST GmbH, Kamp-Lintfort, Germany). Key specifications: center frequency 24 GHz (K-band), bandwidth 2.5 GHz, field of view 65 degrees azimuth by 24 degrees longitudinal (as used mounted on a tower at the Fidelity site in previous campaigns). The radar retrieves snow depth (uncertainty ~2 cm) and snow water equivalent (SWE, uncertainty ~5%) from the radar return signal. In the 2025 field campaign, the radar is used for spatial transects across study sites. The system is lightweight (<500 g with battery), low-cost, and connects to a Raspberry Pi or Arduino controller. Reference design paper: Pomerleau et al. (2020). Output files are TXT and CSV.

#### 6. Spatial surveys (GPS + transect data)

Spatial survey data linking SMP, SnowScope, and radar measurements to geographic coordinates along transects at each study site. Data formats include XLSX, CSV, and zipped shapefiles (SHP). GPS coordinates are in geographic decimal degrees (WGS84 assumed).

### Standards and software

- **ICSSG:** International Classification for Seasonal Snow on the Ground (Fierz et al., 2009) — grain type and size classification used in snow pit profiles
- **OGRS:** Observation Guidelines and Recording Standards for Weather, Snowpack and Avalanches (CAA, 2016) — field observation protocol followed during snow pit work
- **CAAML:** Canadian Avalanche Association Markup Language (V5.0/V6.0) — XML standard for snow profile data exchange; used in the earlier published dataset (DOI: 10.20383/103.01523) but the current dataset deposits raw Excel-format profiles, not CAAML-converted files
- **SNOWPACK model:** Multilayer thermodynamic snow cover model developed at SLF (Bartelt & Lehning, 2002) — referenced in the thesis methodology for simulating snowpack evolution; not directly used in this raw dataset but relevant context for the research program

### Processing level

Raw as collected. Files are unprocessed field instrument outputs. No processing pipeline has been applied. SnowScope CSV files are direct exports from the Snow Scope App.

### Related publications and datasets

- Madore, J.-B. (2023). *Etude integrée de la percolation de l'eau dans le manteau neigeux du Parc national des Glaciers, Colombie-Britannique, Canada.* PhD thesis, Université de Sherbrooke. — Primary methodological reference for this dataset.
- Imbach, B., Madore, J.-B., Jones, A., & Brown, R. (2022). Snow profile observation datasets, Glacier National Park, British Columbia, Canada. FRDR. DOI: 10.20383/103.01523. — Earlier GRIMP dataset from the same study area (2018-2019 seasons), deposited in CAAML format. Confirmed unrelated to the current 2025 dataset.

### Sharing / access context

- **License:** CC BY-NC 4.0
- **Repository:** FRDR (Federated Research Data Repository)
- **Embargo:** None anticipated
- **Parks Canada:** Collaborator providing site access and operational context for the avalanche program. The collaboration is research-based (not a data-sharing agreement requiring special licensing).

### Unresolved README fields

- Full author list beyond Madore and Langlois — affiliations and ORCIDs for tentative authors
- Contact email for Jean-Benoit Madore
- Funding sources (NSERC Discovery Grant likely, CFI for MOACC infrastructure, but award numbers not confirmed)
- CRDC 2020 field_of_research code — candidate: RDF10508 (Cryosphere processes) or RDF1050802 (Glaciology), to be confirmed
- Precise bounding box coordinates (from Explore Data step)
- Whether HEIC field notebook photos and morning hazard assessment PDFs are included (deferred from Scope)

---

## Citable references

### Instruments

1. **Montpetit, B., Royer, A., Langlois, A., Cliche, P., Roy, A., Champollion, N., Picard, G., Domine, F., & Obbard, R.** (2012). New shortwave infrared albedo measurements for snow specific surface area retrieval. *Journal of Glaciology*, 58(211), 941-952. https://doi.org/10.3189/2012JoG11J248
   — Design and validation of the IRIS (InfraRed Integrating Sphere) instrument.

2. **Schneebeli, M., & Johnson, J. B.** (1998). A constant-speed penetrometer for high-resolution snow stratigraphy. *Annals of Glaciology*, 26, 107-111. https://doi.org/10.3189/1998AoG26-1-107-111
   — Original design of the SnowMicroPenetrometer (SMP).

3. **Schneebeli, M., Pielmeier, C., & Johnson, J. B.** (1999). Measuring snow microstructure and hardness using a high resolution penetrometer. *Cold Regions Science and Technology*, 30(1-3), 101-114. https://doi.org/10.1016/S0165-232X(99)00030-0
   — SMP measurement methodology and microstructure interpretation.

4. **Pomerleau, P., Royer, A., Langlois, A., Cliche, P., Courtemanche, B., Madore, J.-B., Picard, G., & Lefebvre, E.** (2020). Low cost and compact FMCW 24 GHz radar applications for snowpack and ice thickness measurements. *Sensors*, 20(14), 3909. https://doi.org/10.3390/s20143909
   — Design and validation of the K-band FMCW radar system (IMST Sentire sR-1200 Series).

5. **Hagenmuller, P., Reuter, B., van Herwijnen, A., & Dual, J.** (2024). Evaluation of the snow penetrometer SCOPE. *Proceedings, International Snow Science Workshop (ISSW)*, Tromsø, Norway.
   — Independent evaluation of the Snow Scope Probe's hardness measurement performance and layer detection capability.

### Standards and classifications

6. **Fierz, C., Armstrong, R. L., Durand, Y., Etchevers, P., Greene, E., McClung, D. M., Nishimura, K., Satyawali, P. K., & Sokratov, S. A.** (2009). *The international classification for seasonal snow on the ground.* UNESCO-IHP, IHP-VII Technical Documents in Hydrology No. 83, IACS Contribution No. 1. https://unesdoc.unesco.org/ark:/48223/pf0000186462
   — ICSSG: grain type and size classification standard used in snow pit profiles.

7. **Canadian Avalanche Association.** (2016). *Observation Guidelines and Recording Standards for Weather, Snowpack and Avalanches (OGRS).* Revelstoke, BC, Canada: Canadian Avalanche Association. https://cdn.ymaws.com/www.avalancheassociation.ca/resource/resmgr/standards_docs/ogrs2016web.pdf
   — Field observation protocol standard followed during snow pit work.

### Models (contextual)

8. **Bartelt, P., & Lehning, M.** (2002). A physical SNOWPACK model for the Swiss avalanche warning: Part I: numerical model. *Cold Regions Science and Technology*, 35(3), 123-145. https://doi.org/10.1016/S0165-232X(02)00074-5
   — SNOWPACK thermodynamic snow cover model used in the broader GRIMP research program.

### Thesis

9. **Madore, J.-B.** (2023). *Etude integrée de la percolation de l'eau dans le manteau neigeux du Parc national des Glaciers, Colombie-Britannique, Canada.* PhD thesis, Université de Sherbrooke.
   — Primary methodological reference; describes all instruments, field protocols, and study sites used in this dataset.

---

## Glossary

| Term | Tag | Definition |
|------|-----|------------|
| IRIS | instrument | InfraRed Integrating Sphere. Laser-based instrument measuring SWIR hemispherical reflectance at 1310 nm and 1550 nm for snow SSA retrieval. Accuracy ~7% vs. micro-CT. Reference: Montpetit et al. (2012). |
| SMP | instrument | SnowMicroPenetrometer. Motor-driven penetrometer; 5 mm conical tip, 60-degree angle, 20 mm/s constant speed, 4 um sampling interval, force range 0-42 N, ~1.8 mm layer resolution. Developed at SLF. Reference: Schneebeli & Johnson (1998). |
| FMCW radar | instrument | Frequency-Modulated Continuous-Wave radar. IMST Sentire sR-1200 Series, 24 GHz center frequency, 2.5 GHz bandwidth, K-band. Retrieves snow depth (2 cm uncertainty) and SWE (5% uncertainty). Weight <500 g. Reference: Pomerleau et al. (2020). |
| SnowScope | instrument | Snow Scope Probe. Digital snow penetrometer by Propagation Labs. Collapsible probe with sensor bullet; 5000+ Hz sampling; hardness range 3-550 kPa; depth resolution ~3 mm; minimum layer thickness 1.5 mm; optional optical reflectance channel. Weight 385-475 g. CSV output via Snow Scope App. Reference: Hagenmuller et al. (2024). |
| StratiTemplate | instrument | Excel-based workbook template for recording manual snow pit stratigraphy observations (grain type, size, hardness, density, temperature, wetness). |
| SSA | variable | Specific Surface Area of snow grains (m^2/kg). Measured by IRIS from SWIR reflectance. Controls snow optical properties and metamorphism rates. |
| Penetration resistance | variable | Force (N) measured by the SMP as the conical tip penetrates the snowpack. Proxy for snow mechanical hardness at high spatial resolution. |
| SWE | variable | Snow Water Equivalent. Mass of water per unit area in the snowpack (kg/m^2 or mm w.e.). Retrieved from K-band radar. |
| Snow depth | variable | Total depth of the snowpack (cm or m). Retrieved from K-band radar or measured manually. |
| Optical reflectance | variable | Near-infrared backscatter measured by the Snow Scope Probe at each depth step (arbitrary units). Present in 181 of 319 SnowScope CSV files in this dataset. |
| Snow stratigraphy | technique | Layer-by-layer characterization of the snowpack including grain type/size, hardness, density, temperature, and wetness. Follows ICSSG and OGRS standards. |
| ICSSG | standard | International Classification for Seasonal Snow on the Ground (Fierz et al., 2009). Defines grain type symbols, size classes, and snow property classification. UNESCO-IHP Technical Document No. 83. |
| OGRS | standard | Observation Guidelines and Recording Standards for Weather, Snowpack and Avalanches (CAA, 2016). Canadian standard for field snow and avalanche observations. |
| CAAML | standard | Canadian Avalanche Association Markup Language. XML schema for electronic exchange of snow profile and avalanche data. V5.0/V6.0 supported by IACS. Not used in this deposit (raw Excel format). |
| SNOWPACK | acquisition | Multilayer thermodynamic snow cover model (SLF). Simulates mass, energy, and momentum balance. Used in the broader GRIMP research program. Reference: Bartelt & Lehning (2002). |
| GRIMP | organization | Groupe de Recherche Interdisciplinaire sur les Milieux Polaires. Founded 2014 by A. Langlois, Université de Sherbrooke. Research axes: snow dynamics, avalanche, permafrost, atmospheric monitoring. |
| MOACC | initiative | Multidisciplinary Observatory for Arctic Climate Change. CFI-funded GRIMP infrastructure project at CHARS, Cambridge Bay, Nunavut. |
| Parks Canada ACP | organization | Parks Canada Avalanche Control Program at Glacier National Park. Operates the world's largest mobile artillery avalanche control program at Rogers Pass since 1961. Collaborator for field site access. |
| Mount Fidelity | acquisition | Long-standing snow study plot at 1905 m elevation in the Selkirk Mountains, Glacier National Park. Reference site for snowpack monitoring. |

---

## Source notes

| Claim | Source |
|-------|--------|
| IRIS measures SWIR reflectance at 1310 and 1550 nm; 7% accuracy vs. micro-CT | Montpetit et al. (2012); Madore thesis Ch. 3 |
| SMP: 5 mm tip, 60-degree cone, 20 mm/s, 4 um resolution, 0-42 N range | Schneebeli & Johnson (1998); Madore thesis Ch. 3 |
| FMCW radar: IMST Sentire sR-1200, 24 GHz, 2.5 GHz bandwidth, snow depth 2 cm uncertainty, SWE 5% uncertainty | Pomerleau et al. (2020); Madore thesis Ch. 6 |
| Fidelity study site at 1905 m, Selkirk Mountains | Madore thesis Ch. 3 |
| Parks Canada operates world's largest mobile artillery avalanche control at Rogers Pass since 1961 | Parks Canada website; Madore thesis Ch. 1 |
| GRIMP founded 2014 by A. Langlois, Université de Sherbrooke | project_context.md |
| Thesis supervisors: A. Langlois (UdeS), C. Fierz (SLF) | Madore thesis title page |
| Field protocols follow OGRS (CAA, 2016) and ICSSG (Fierz et al., 2009) | Madore thesis Ch. 3 |
| SNOWPACK model used for snowpack simulation in the research program | Madore thesis Ch. 5; Bartelt & Lehning (2002) |
| Madore ORCID: 0000-0002-2292-1519 | orcid.org |
| Langlois ORCID: 0000-0002-9966-205X | orcid.org; The Cryosphere (2024) publication |
| Madore affiliation: UdeS Dept. géomatique appliquée + Centre d'études nordiques | Madore thesis; CEN profile; CARTEL profile |
| Langlois affiliation: UdeS Dept. géomatique appliquée + GRIMP + CEN | grimp.ca; ResearchGate |
| License: CC BY-NC 4.0 | Scope elicitation (researcher confirmed) |
| Unrelated to DOI 10.20383/103.01523 | Scope elicitation (researcher confirmed) |
| Campaign dates: 2025-03-01 to 2025-03-06 | Scope definition (file dates) |
| Sites: Fidelity, Jim Bay Corner, Hermit, Round Hill, Christiana Ridge | Scope definition |
| CRDC candidate: RDF10508 (Cryosphere processes) or RDF1050802 (Glaciology) | StatCan CRDC 2020 v2.0 classification |
| SnowScope: digital snow penetrometer by Propagation Labs; specs from manufacturer website | propagationlabs.com/specs |
| SnowScope: 3 units (00304, 00322, 00328); FW 2.4.1; PCB v2.7; creator Francis Gauthier; 319 CSVs | data_exploration.md §5 (file header metadata) |
| SnowScope: independent evaluation at ISSW 2024 | Hagenmuller et al. (2024); propagationlabs.com/blog |

---

## Scope updates

The following clarifications are noted:

- The 2025 campaign uses the same stratigraphy, IRIS, SMP, and radar instruments and methodology as Madore (2023) thesis work from 2018-2019 seasons, but adds the Snow Scope Probe as a new instrument not present in the earlier campaigns. The SnowScope is not documented in the thesis.
- Charles Fierz (SLF, Davos) was co-supervisor for Madore's PhD but his involvement in the 2025 campaign is unknown. He should not be listed as author unless confirmed by the researcher.
- Funding sources were not definitively identified. NSERC Discovery Grant and CFI (for MOACC) are likely but award numbers require researcher confirmation.
