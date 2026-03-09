# Project Context — GRIMP FRDR Helper

This document synthesizes research on the project's organizational context, the FRDR platform, metadata requirements, and the data management workflow. It serves as a reference for agents and contributors.

## 1. GRIMP — Groupe de Recherche Interdisciplinaire sur les Milieux Polaires

**Founded:** 2014 by Professor Alexandre Langlois
**Affiliation:** Department of Applied Geomatics, Universite de Sherbrooke. Associated with CARTEL (Centre d'applications et de recherches en teledetection) and Centre d'etudes nordiques (Universite Laval).

**Research axes:**

- **Snow dynamics** — Drone surveys for 3D snow mapping, passive microwave and radar remote sensing of snow and sea ice, rain-on-snow event detection.
- **Avalanche** — Avalanche hazard assessment, snow profile observation, stability testing. Collaboration with Parks Canada (Glacier National Park, Rogers Pass).
- **Permafrost** — Monitoring degradation, thermokarst lake formation, soil erosion in Arctic watersheds.
- **Atmospheric monitoring** — Ozone chemistry, aerosol/gas transport, seasonal processes affecting the Arctic tropopause.
- **Ecosystem/community** — Caribou habitat monitoring, integration of Inuit traditional knowledge.

**Key people:**

- Alexandre Langlois — Full professor, founded GRIMP, specializes in passive microwave remote sensing of Arctic snow cover.
- Alain Royer — Professor, co-director.
- Frederic Bouchard — Assistant professor, permafrost degradation and thermokarst lakes.
- Jean-Benoit Madore — Researcher, snow profile datasets, CAAML processing.
- Benjamin Imbach — Researcher (UQAR), snow profile datasets.
- Daniel Kramer — Coordinator.

**Field sites:** Cambridge Bay (Nunavut), Barnes Ice Cap, Baie-James, Chic-Chocs, Foret Montmorency, Umiujaq, Rogers Pass (BC), Canadian Prairies, Davos (Switzerland).

Sources: [grimp.ca](https://grimp.ca/), meeting notes, [CFI research story](https://www.innovation.ca/projects-results/research-stories/research-global-warming-northern-canada)

## 2. MOACC — Multidisciplinary Observatory for Arctic Climate Change

MOACC is GRIMP's flagship infrastructure project, funded by CFI.

- Located at the Canadian High Arctic Research Station (CHARS) in Ikaluktuutiak (Cambridge Bay), Nunavut.
- Goal: establish one of the largest instrumented high Arctic observatories for long-term continuous monitoring of climate change indicators.
- 10-year data acquisition and management effort.
- 10 primary researchers, 20+ collaborators, 4 Canadian universities (Sherbrooke, Toronto, Western Ontario, Montreal).
- Instruments: atmospheric lidar, sun/star photometers, radiometers, spectrometers, radar (dual-Ku), weather stations, drones.
- Data types: greenhouse gases, aerosols, clouds, snow, permafrost, atmosphere, remote sensing imagery, model outputs.

**Research themes:**

- TH1 — Snow remote sensing and ecological applications
- TH2 — Snow modeling and hydrology

Sources: meeting notes (Rencontre Jean-Benoit, Rencontre Alex), [CFI](https://www.innovation.ca/projects-results/research-stories/research-global-warming-northern-canada)

## 3. FRDR — Federated Research Data Repository

**What it is:** A bilingual (EN/FR), open-access, curated, general-purpose Canadian research data repository purpose-built for discovering and publishing research data, with support for large datasets.

**Key features:**

- Accepts all disciplines and file formats (open formats preferred).
- DOI assignment for each dataset.
- Data versioning.
- Globus Transfer integration for large file uploads.
- Post-submission curation by FRDR staff.
- Long-term preservation; temporary embargo periods available.
- Free storage for Canadian post-secondary researchers (~1 TB/person default).
- Discovery via FRDR catalog and Lunaris (national dataset discovery service).

**Who can deposit:** Faculty, librarians, and researchers at Canadian post-secondary institutions; Tri-Agency-eligible organizations; sponsored designates (grad students, postdocs, collaborators).

**File format recommendations:** CSV, NetCDF, HDF5, GeoTIFF, GeoJSON, open non-proprietary formats. Avoid ZIP for datasets (except zipped shapefiles).

Sources: [FRDR docs](https://www.frdr-dfdr.ca/docs/en/), meeting notes (Rencontre d'information avec FRDR)

## 4. FRDR Metadata Requirements

### Required fields

| Field | Description |
|---|---|
| Title | Complete name identifying the dataset |
| Description | Summary covering purpose, nature, scope, context for reuse |
| Keywords | Subject terms; can use controlled vocabularies (e.g. OCLC FAST) |
| Field of Research | Canadian Research and Development Classification (CRDC 2020 v1.0) |
| Author | Last name, first name, affiliation(s), ORCID (optional) |
| Contact | Name and email (email kept private; public contact form displayed) |
| Rights/License | Creative Commons license (CC0, CC BY 4.0, CC BY-NC, etc.) |

### Recommended fields

| Field | Description |
|---|---|
| Time Period Covered | Date range the data addresses (YYYY-MM-DD) |
| Collection Period | When data gathering occurred |
| Funding Information | Funder name, award number, award title |
| Contributor | Additional people/institutions with roles |
| Related Identifiers | DOIs/URLs to related resources with relationship types |
| Notes | File structure, instruments, software requirements |
| Geographic Coverage | Place name (GeoNames), lat/long point, bounding box |

### README file (mandatory)

FRDR curators require a README file with each dataset. The FRDR template (adapted from Cornell) is available at `docs/FRDR-template_README.txt`.

Required content:

- Contact information
- Methodology (acquisition and processing)
- Variable definitions with units
- Null-value coding
- Software/equipment versions
- File/folder inventory

Sources: [FRDR — Describing your data](https://www.frdr-dfdr.ca/docs/en/describing_your_data/), [FRDR — Preparing your data](https://www.frdr-dfdr.ca/docs/en/preparing_your_data/)

## 5. FAIR Principles in Context

The project workflow maps directly to FAIR:

- **Findable** — Structured metadata, DOIs, keyword search, FRDR catalog + Lunaris discovery.
- **Accessible** — Open access by default; controlled access/embargo when needed.
- **Interoperable** — Open formats, controlled vocabulary, standards (CAAML for snow profiles, OGRS for avalanche observations).
- **Reusable** — Creative Commons licensing, detailed README, variable dictionaries, citation.

## 6. GRIMP FRDR Collection

**Status:** Not yet created. A GRIMP collection on FRDR is planned but does not exist yet.

**Existing published dataset (reference):**

- Title: "Snow profile observation datasets, Glacier National Park, British Columbia, Canada"
- DOI: [10.20383/103.01523](https://doi.org/10.20383/103.01523)
- Part of collection: "Glacier National Park Weather, Snow, and Avalanche Collection"
- Format: CAAML files (XML standard for avalanche-related data)
- Authors: Imbach, Madore, Jones, Brown
- License: CC BY-NC 4.0 (Parks Canada Open Licence)
- This dataset is used as the reference template in `datasets/example/`.

## 7. Controlled Vocabulary

Maintained in `docs/controlled_vocabulary.md`. Current terms:

**Research axes:** Avalanche, Arctic

**Common keywords:** avalanche hazard assessment, snow profile, stability test, mountain hazard, winter hazard

**From meeting notes (to be integrated):**

- Themes: Avalanche, Arctic, Permafrost, MOACC, Snow Water Equivalent (SWE)
- Acquisition: Snowpit, Weather station, Radar dual-Ku, SNOWPACK modeling, OSSA derived maps, Drone imagery, Remote sensing, IRIS
- MOACC themes: TH1 (Snow remote sensing & ecological applications), TH2 (Snow modeling & hydrology)
- Sites: Fidelity, Cambridge Bay
- Partners: Parks Canada

## 8. Data Quality and Standardization

From meeting notes, snowpit data exists in multiple formats:

0. Raw — unprocessed, researcher-formatted
1. Multi-sheet Excel — shared pre-acquisition format
2. CSV tree — processed by Nicolas
3. CAAML markup — XML standard

The project should document which format level is being deposited and any processing steps applied.

## 9. Workflow Summary

```
Scope dataset → Prepare data (format, clean) → Write metadata (form + README)
  → Upload to FRDR (web/Globus) → Curation review → Publish (DOI) → Discover
```

Sources: meeting notes, FRDR docs, presentation plan
