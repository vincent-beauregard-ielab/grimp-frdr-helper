# Rogers Pass Snow Profiles Research Notes

## Dataset overall description

This dataset documents a six-day snow field campaign conducted in Rogers Pass, British Columbia, from 2025-03-01 to 2025-03-06. The campaign combined full snowpit observations with instrumented spatial surveys at Fidelity, Jim Bay Corner, Hermit weather station, Round Hill, and Christiana Ridge. The raw package includes snow stratigraphy workbooks, density and stability observations, SnowScope profile exports, SnowMicroPen (`.pnt`) files, FMCW radar text exports, IRIS outputs, GNSS point files, and contextual field notes.

The scientific objective is to characterize snow stratigraphy, density, hardness, grain properties, liquid-water-related structure, and short-range spatial variability relevant to avalanche forecasting and snow remote sensing. The local source material ties the campaign to GRIMP avalanche and snow-remote-sensing work at Universite de Sherbrooke. The broader research context is the group’s long-running snowpack modeling and radar work in Rogers Pass; the PhD thesis by Jean-Benoit Madore describes the same study region, repeated Fidelity measurements, manual snow profiles, IRIS-based grain measurements, and 24 GHz FMCW radar observations used to study percolation and stratigraphy.

The dataset appears to mix two observation modes described in the thesis and field notes:

- `heavy` reference profiles: full snowpit, density, IRIS, and stability tests at fixed or repeat sites;
- `light` spatial surveys: portable SnowScope, SMP, radar, and GNSS measurements collected along short transects.

Verified geographic coverage from file metadata spans approximately:

- latitude `51.2341198` to `51.3236271`
- longitude `-117.7132470` to `-117.5314499`

The campaign is clearly part of GRIMP research. A direct funding statement for this specific March 2025 campaign is not yet confirmed from local materials. `docs/project_context.md` links GRIMP’s snow work to avalanche research in Rogers Pass and lists MOACC research themes, but MOACC should be treated as contextual vocabulary until the dataset owner confirms that this campaign was funded or reported under MOACC.

## README input capture

### Candidate dataset title

Working title:

`Rogers Pass snow profiles and spatial snow-property surveys, British Columbia, Canada, March 2025`

This title is descriptive enough for FRDR, but the final title still needs owner confirmation, especially whether Fidelity repeat profiles and Christiana Ridge exploratory data should be in the same deposit.

### People, institutions, and likely roles

Confirmed from local documents:

- Jean-Benoit Madore, Universite de Sherbrooke / GRIMP: campaign lead, radar and snow research context
- Alexandre Langlois, Universite de Sherbrooke / GRIMP: field participant and GRIMP lead
- Benjamin Imbach, UQAR: field participant, profile observations
- Francis Gauthier, GRIMP: repeated creator name in SnowScope exports; field participant
- Violaine Paquette: field participant
- Francis Meloche: field participant during early campaign days
- Hans-Peter Marshall: Round Hill spatial day participant with radar measurements
- Jo Meyer and Julien Meloche: Round Hill / day 6 participants
- Catherine Brown and Parks Canada staff are mentioned in context notes but not yet confirmed as dataset authors

Likely contributor organizations:

- GRIMP / Universite de Sherbrooke
- UQAR
- Parks Canada, for site access and Rogers Pass avalanche operations context

### Collection period and geography

Verified collection dates in files and day readmes:

- 2025-03-01: Fidelity and Jim Bay Corner spatial work
- 2025-03-02: Jim Bay Corner
- 2025-03-03: Hermit weather station
- 2025-03-04: Fidelity study plot
- 2025-03-05: Round Hill
- 2025-03-06: Christiana Ridge and Fidelity

Sites confirmed in workbook and note text:

- Fidelity / Mount Fidelity
- Jim Bay Corner
- Hermit weather station
- Round Hill
- Christiana Ridge / Christiania Ridge

Note the spelling inconsistency `Christiana` vs `Christiania` in the raw files.

### Scientific and methodological context

Local thesis evidence supports the following interpretation:

- Rogers Pass manual snow observations follow OGRS-style snowpit practice with grain type, grain size, hardness, density, temperature, liquid-water-related observations, and compression tests.
- The IRIS workflow is used to derive snow optical / grain metrics from calibrated reflectance measurements.
- A 24 GHz FMCW radar is used for snow stratigraphy, wetting-front, crust, and SWE-related work at Fidelity and in portable spatial deployments.
- SnowMicroPen measurements provide high-resolution penetration-force profiles.

The day-level notes show how instruments were combined operationally:

- 2025-03-01: 4 SMP, 8 radar, and 8 SnowScope measurements at the Fidelity profile site, then 23 spatial observations above Jim Bay Corner
- 2025-03-02: full profile plus 12 GPS-linked SMP and radar points at Jim Bay Corner
- 2025-03-03: full profile plus a spatial survey around Hermit Wx
- 2025-03-05: one full profile and a large Round Hill spatial survey; field note says 43 points with multiple radars, SMP, and SnowScope

### Instruments, standards, and software to mention in the README

Likely instruments:

- SnowScope probe
- SnowMicroPen (SMP)
- IRIS snow optical measurement workflow
- FMCW radar at K-band / Ka-band naming in folders, with local thesis context for 24 GHz FMCW radar
- RTK / rover GNSS for spatial point locations

Likely standards:

- OGRS for manual snow, weather, and avalanche observation vocabulary
- CAAML as the main snow-profile interoperability target already used in the published reference dataset

Likely software / packages relevant for reuse:

- spreadsheet software or `openpyxl` / `pandas` for `.xlsx`
- `pandas` for CSV and radar text parsing
- `snowmicropyn` for `.pnt`
- software able to read CAAML if the dataset is later converted

### File and folder relationship notes already known

The raw package is organized by campaign day rather than by instrument. Within each day:

- a stratigraphy workbook records the reference snowpit
- instrument-specific subfolders hold spatial survey data
- single-sheet workbooks or GPS CSVs map measurement IDs across radar, SMP, SnowScope, and GNSS
- readme/docx files describe daily field operations and sampling intent

Administrative material is mixed into the same raw tree:

- AWP permit PDFs
- meal-planning workbook
- parking reservation PDF

These should probably not be part of the scientific FRDR deposit.

### Related works and reference resources

- Published reference dataset in `datasets/example/`: Glacier National Park CAAML snow profiles, DOI `10.20383/103.01523`
- Madore PhD thesis (local): provides Rogers Pass methodology, SNOWPACK context, IRIS use, and 24 GHz radar setup
- Pomerleau et al. 2020 Sensors paper on compact 24 GHz FMCW radar: `https://doi.org/10.3390/s20143909`
- OGRS 2024 PDF cited by the example README: `https://www.avalancheassociation.ca/resource/resmgr/docs/ogrs/ogrs2024web.pdf`
- CAAML schema landing page: `https://caaml.org/Schemas/SnowProfileIACS/`
- SnowScope product page: `https://www.propagationlabs.com/products/snowscope-probe`
- SLF SnowMicroPen page: `https://slf.ch/en/services-and-products/snowmicropen-smp/`

### Open questions for README drafting

- Final dataset title and author order
- Principal investigator contact and public contact email
- Exact license for this deposit
- Whether Parks Canada is a formal co-author, contributor, or contextual partner
- Whether the deposit should include HEIC photos and day readmes as supporting documentation
- Whether shapefile ZIPs will be included as ancillary spatial files
- Whether any files will be transformed to open formats before deposit
- Whether this campaign should explicitly name a grant or CFI / MOACC funding source

## Glossary

- `CAAML` (`standard`): Cryosphere and avalanche XML schema used widely for interoperable snow-profile data.
- `compression test` (`technique`): Manual snow stability test recorded in the stratigraphy workbooks.
- `density profile` (`variable`): Vertical snow density observations recorded in the `Density` sheets.
- `FMCW radar` (`instrument`): Frequency-modulated continuous-wave radar used for stratigraphy and wetting-front detection.
- `Fidelity` (`acquisition`): Main repeat Rogers Pass study site used for fixed-profile and radar work.
- `GNSS` (`instrument`): Positioning workflow used to geolocate spatial survey measurements.
- `GRIMP` (`organization`): Groupe de recherche interdisciplinaire en milieu polaire.
- `hardness (kPa)` (`variable`): Snow resistance output in SnowScope CSV profiles.
- `IRIS` (`instrument`): Infrared reflectance-based snow measurement workflow represented in workbook `IRIS` sheets and text exports.
- `Jim Bay Corner` (`acquisition`): Spatial survey site used on 2025-03-01 and 2025-03-02.
- `OGRS` (`standard`): Observation Guidelines and Recording Standards used for Canadian avalanche field observations.
- `optical reflectance` (`variable`): SnowScope output field used in SN00328 files; absent in SN00322 exports.
- `Ropt` (`variable`): Optical grain-radius-style metric present in workbook `IRIS` sheets.
- `Round Hill` (`acquisition`): High-elevation site used for one full profile and a large spatial survey.
- `snowpit` (`technique`): Excavated profile used to document stratigraphy, temperature, density, and stability.
- `SNOWPACK` (`processing`): Thermodynamic snow model used in the broader Rogers Pass research program described in the thesis.
- `SnowMicroPen` (`instrument`): High-resolution penetrometer for snow-force profiles stored as `.pnt`.
- `SnowScope` (`instrument`): Portable probe generating hardness-depth CSV profiles, with some exports also carrying optical reflectance.
- `SSA` (`variable`): Specific surface area field in workbook `IRIS` sheets.
- `stratigraphy` (`variable`): Layered description of snow structure, grain form, and hardness.

## Source notes

- `datasets/rogers_pass_snow_profiles/docs/scope.yaml`: confirms dataset identity, raw-data source path, and initial site list.
- `datasets/rogers_pass_snow_profiles/docs/meeting notes/MOACC Rencontre Jean-Benoit nouveau dataset.md`: confirms required metadata categories, controlled-vocabulary ideas, and upload workflow expectations.
- `datasets/rogers_pass_snow_profiles/raw_data/.../*.docx` day readmes: confirm daily field objectives, team composition, and multi-instrument sampling sequences.
- `papers/madore_jean-benoit_PhD_2023.pdf`, thesis chapter 3: describes Rogers Pass station context, heavy vs light sampling logic, OGRS-style profile observations, IRIS use, and the 24 GHz FMCW radar setup.
- `papers/madore_jean-benoit_PhD_2023.pdf`, appendix references: links the radar work to the 24 GHz FMCW literature and GRIMP co-authored papers.
- `docs/project_context.md`: provides GRIMP, FRDR, and reference-dataset context.
