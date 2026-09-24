# Research — RogersPass_2025-2026

Sources consulted: `papers/madore_jean-benoit_PhD_2023.pdf`, `papers/Madore_Jean_Benoit_MSc_2016.pdf`, `papers/snowSCOPE.pdf`, `docs/project_context.md`, `docs/controlled_vocabulary.md`, `datasets/example/README.txt`, `datasets/example/metadata.yaml`, and web search (instrument design papers, standards, site background). Both theses were read in full by sub-agents (PhD: 139 pp., MSc: 75 pp.); the SnowScope paper was read in full directly.

---

## Dataset overall description

**Scope.** Field measurement campaign at Rogers Pass, Glacier National Park (GNP), British Columbia, Canada, conducted 2026-03-03 to 2026-03-10 (within the 2025-2026 winter season). Five sites visited: Round Hill, Fidelity, Jim Bay, Gopher Butte, Hermit Meadows. The campaign collected manual snow profiles together with several complementary instrumented measurements of near-surface snow microstructure and stratigraphy: specific surface area (SSA) via the IRIS infrared-reflectance instrument, two hardness/penetration-resistance penetrometers (SMP and SnowScope/SCOPE), dual-frequency FMCW radar (Ku-band and Ka-band, folder-labeled `dku`/`ka`), and GPS positioning. Field logistics records (risk assessment PDFs, fieldbook photos) are out of FRDR deposit scope per researcher decision and are not researched here.

**Research objective — now well supported by the theses.** This is a direct continuation of a long-running GRIMP research program at the Fidelity station, Glacier National Park, whose goal is to validate remote-sensing/radar-based snow retrievals (SWE, stratigraphy, density, SSA) against in-situ snow-pit and penetrometer measurements, and to support Parks Canada's avalanche-forecasting operations at Rogers Pass. Specifically:

- GRIMP "has collected snow data since 2014" in GNP (PhD thesis, p.75), with an instrumented station established at Fidelity from 2016–2018 onward (visibility sensor 2016, 24 GHz FMCW radar 2017, snow-temperature/permittivity mast 2018).
- The PhD thesis (Madore, 2023) explicitly documents that, as of thesis writing, a **dual-frequency Ku-band FMCW radar (13.5/17.5 GHz) matching the planned satellite Terrestrial Snow Mass Mission (TSMM; Derksen et al., 2019) was planned for installation at Fidelity** (PhD thesis, p.117–118) — this strongly indicates the 2026 campaign's dual-frequency Ku-band radar (`dku` folder) is the field realization of that plan, i.e. calibration/validation data for a TSMM-analog instrument. This is a high-value fact for the README's context/methodology section.
- The `ka`-labeled radar data most likely corresponds to GRIMP's existing, separately-published 24 GHz FMCW radar (IMST Sentire™ sR1200, Pomerleau et al. 2020 hardware), which the group's own papers (Laliberté et al., 2018/2021/2022) call "Ka-band" despite technically sitting at the K/Ka-band boundary (24 GHz) — see Radar glossary entry for the reasoning and its confidence level.
- IRIS and SMP are the group's standard "heavy" (full-pit) and "light" (portable/spatially-distributed) snow-microstructure measurement pairing, used since at least the 2013–2016 campaigns (MSc thesis) specifically to validate the SNOWPACK model and, more recently, radar stratigraphy retrievals (PhD thesis Ch. 6, SMP-vs-radar peak comparison).
- SnowScope/SCOPE is a newer, lightweight, hand-push alternative/complement to SMP (not mentioned in either thesis — see gap note below); it is documented by an independent ISSW evaluation paper, not a GRIMP paper.

**Organizational context.** GRIMP (Groupe de Recherche Interdisciplinaire sur les Milieux Polaires), Universite de Sherbrooke, Departement de geomatique appliquee, founded 2014 by Alexandre Langlois (PI of this campaign, and supervisor of both source theses). Research axis: Avalanche (collaboration with Parks Canada, Glacier National Park, Rogers Pass) — see `docs/project_context.md` §1. Collaboration partners confirmed across both theses: Parks Canada's Glacier National Park avalanche-safety group, Avalanche Quebec, Centre d'etudes nordiques (CEN), and (PhD thesis) WSL Institute for Snow and Avalanche Research (SLF, Davos, Switzerland — co-supervisor Charles Fierz). No direct evidence that this specific campaign draws on MOACC (GRIMP's Arctic infrastructure project); MOACC is Cambridge-Bay/Arctic-focused and distinct from the GNP avalanche axis. `to-be-confirmed`

**Existing related FRDR dataset.** `datasets/example/` — "Snow profile observation datasets, Glacier National Park, British Columbia, Canada" (DOI 10.20383/103.01523), authors Imbach, Madore, Jones, Brown, CAAML format, CC BY-NC 4.0 (Parks Canada Open Licence). This is the Glacier National Park avalanche-forecasting team's own long-running snowpit archive (2015–2024), not this campaign's data — but the relationship is now independently corroborated: two of its Parks Canada co-authors, **Andrew Jones and Catherine Brown**, are named by their full names in the PhD thesis acknowledgments as members of "the Glacier National Park avalanche safety group" that supported this exact research line (PhD thesis, pp.4-5). Recommend `IsRelatedTo` reference to this DOI. Exact relation type (`IsPartOf` vs `IsRelatedTo` vs `Cites`) — **to confirm with researcher.**

---

## Scope dimensions

### Spatial

- Region: Rogers Pass, Glacier National Park, British Columbia, Canada — interior Columbia Mountains, specifically the **Selkirk Mountains** (PhD thesis, p.62). Transitional climate zone between wet/maritime (west, Illecillewaet valley) and dry/continental (east, Beaver valley); Fidelity sits near this boundary. Mean annual snowfall ~15 m at 1905 m; max accumulation regularly >3.5–4 m; generally low temperature gradients favoring equilibrium (rounding) metamorphism, with storm-loading onto weak layers as the primary avalanche trigger mechanism (PhD thesis, p.35, p.62, p.94). `literature-derived`
- Avalanche-control context: GNP has conducted artillery avalanche control on this Trans-Canada Highway corridor since 1962; ~200 potential avalanche paths affect 134 locations on the highway (Schleiss, 1990, cited in PhD thesis p.35). This is "the largest Canadian avalanche control operation" (PhD thesis, p.62). `literature-derived`
- Site elevations/coordinates, from Madore's GRIMP weather-station table (PhD thesis, Table 3.1, p.36) — these are the **same station names used in the 2025-2026 campaign** for three of five sites:

  | Site | Elevation (Madore Table 3.1) |
  |---|---|
  | Fidelity | 1905 m |
  | Round Hill | 2100 m ("500 m uphill on mount Fidelity") |
  | Hermit | 1950 m |
  | Rogers Pass (valley-bottom station) | 1315 m |
  | Asulkan | 2025 m |
  | Abbott | 2085 m |
  | MacDonald | 1930 m |
  | Rockfall | 2240 m |
  | Heather Hill | 915 m |

  `literature-derived`, elevation only — no lat/lon given in either thesis for any station (Figure 1 in the MSc thesis shows only a qualitative red-point map, no coordinate table).
- Jim Bay and Gopher Butte: **zero mentions in either thesis.** Gopher Butte has one independent web-literature match: a treeline knoll near Mount Fidelity at 51°14'17" N, 117°42'10" W, 1,940 m, used in an unrelated 2005–2006 snow-warming study (not GRIMP) — treat as a plausible but unconfirmed anchor point, not this campaign's actual coordinates. "Jim Bay" has no snow-science literature match at all; the only web hit is an informal place name for a highway switchback at Rogers Pass, likely unrelated. `to-be-confirmed-from-files`
- Precise per-profile coordinates for all five sites as actually visited in 2026: `to-be-confirmed-from-files` (Explore Data should extract from GPS files/instrument headers).
- Bounding box / CRS: not yet established; recommend WGS84 decimal degrees once Explore Data derives point coordinates. `to-be-confirmed-from-files`

### Temporal

- Campaign dates: 2026-03-03 to 2026-03-10 (2025-2026 winter field season). `literature-derived` (scope definition)
- This is a single one-week campaign; GRIMP's GNP/Fidelity research program itself is multi-year and ongoing since 2014 (radar station since 2017, SNOWPACK/IRIS/SMP campaigns since 2013). `literature-derived`
- Exact per-site, per-instrument acquisition dates/times within the campaign window: `to-be-confirmed-from-files`

### Measurement domain

- **SSA (IRIS):** infrared reflectance via a 10-cm diameter, 3-port Labsphere integrating sphere; illumination laser at 1310–1315 nm (both theses report slightly different wavelengths — 1315 nm in the PhD, "1.33 µm" [≈1330 nm] with a note that the related DUFISSS comparator instrument uses 1.31 µm, in the MSc — this is an instrument/unit-specific value, not resolved further here); dark-current correction via a diaphragm measurement subtracted from the sample signal; sample held in a 10-cm-diameter, 6-cm-high aluminum cylinder. Output is SSA in m²/kg per layer/depth. Design/validation reference: Montpetit et al. (2012), building on Gallet et al. (2009). `literature-derived` (instrument design); as-operated resolution/protocol for this campaign `to-be-confirmed-from-files`
- **Hardness/stratigraphy (SMP, SnowScope):** SMP — motorized, constant ~20 mm/s penetration, vertical resolution "263 measurements per mm" (≈0.004 mm) per the MSc thesis, force output in N, developed at SLF Davos (Schneebeli & Johnson, 1998; Schneebeli et al., 1999); density/correlation-length retrievable via Proksch et al. (2015). SnowScope/SCOPE — hand-push, optical/reflectance depth sensing, nominal 0.2–1.6 m depth range, 1 mm depth / 1.5 mm layer resolution, 3–550 kPa force range (Hagenmuller et al., 2024, ISSW evaluation). `literature-derived`
- **Radar:** dual-frequency FMCW, folders `dku` (very likely the dual-Ku 13.5/17.5 GHz TSMM-matching system — see Dataset overall description) and `ka` (very likely the existing 24 GHz Pomerleau/Laliberté system, "Ka-band" in GRIMP's own naming convention despite the frequency technically sitting at the K/Ka boundary). Exact center frequencies/bandwidth/deployment geometry **as actually operated in this specific campaign**: `to-be-confirmed-from-files` (file headers) — the `dku`/`ka` interpretation above is a well-supported inference, not a confirmed fact.
- **GPS:** positioning of profile/measurement locations. Neither thesis mentions a GPS instrument, brand, or accuracy at all (zero hits in both full-text searches) — this appears to be new to the 2025-2026 campaign's instrument set. Unit type/accuracy: `to-be-confirmed-from-files`.
- Depth range: manual profiles typically to the ground or to a defined stop depth per OGRS convention (full pits in Madore's work evaluated the top ~2 m in detail even when total depth reached 3.5 m); instrumented profiles limited by each instrument's stroke length (SMP ≤ ~1.25–2.2 m nominal; SnowScope ≤ ~1.6–2.1 m nominal). `literature-derived`

---

## README input capture

- **Candidate title** (already drafted in README.txt): "Snow profile, SSA, and radar observations, Rogers Pass, Glacier National Park, British Columbia, Canada (2025-2026 winter season)" — consistent with the confirmed instrument set; no change recommended, though consider adding "SMP"/"penetrometer" if Data Preparation confirms SMP/SnowScope are retained in the final deposit package.
- **People/institutions/roles:**
  - **Alexandre Langlois** — PI, Universite de Sherbrooke (GRIMP). Confirmed as founder/PI of the whole research program and supervisor of both source theses. Role: Project Manager / Supervisor.
  - **Jean-Benoit Madore** — Universite de Sherbrooke (GRIMP). Author of both source theses; extensive prior first-hand work on IRIS/SSA, SMP, and the Fidelity radar station. Role: Data Collector / methodology lead.
  - **Benjamin Imbach** — Universite du Quebec a Rimouski (UQAR). Co-author of the related published FRDR dataset (`datasets/example/`). Role: Data Collector / Research Associate.
  - **Nicolas Allet, Marie-Clara Delage, Violaine Paquette, Megan Cramb, Nicolas Marchand** — no independent literature confirmation of role/affiliation found for this specific campaign. Note: a **Nicolas Marchand** is separately named among GRIMP "research group colleagues" thanked in the PhD thesis acknowledgments (p.4-5) — plausibly the same person, supporting GRIMP affiliation, but not confirmed as the same individual. `to-be-confirmed`
  - Contact email addresses for all above: none published/confirmed. `to-be-confirmed` (researcher must supply)
  - **Cross-validation of the related FRDR dataset's authorship:** Andrew Jones and Catherine Brown (Parks Canada, co-authors of `datasets/example/`) are independently named in the PhD thesis acknowledgments as part of "the Glacier National Park avalanche safety group" that has supported GRIMP's Rogers Pass research for years — this confirms the two datasets share a real, ongoing institutional collaboration, not just topical overlap.
  - **Flag for researcher, not adopted as fact:** a GitHub pull request in a fork of this same tool's repository (`vincent-beauregard-ielab/grimp-frdr-helper`, PR #2, "Revision chercheur — artefacts Rogers Pass") — an earlier/parallel exercise of this exact workflow (current branch here is `demo-vincent`), reviewed by a "jbmadore" account — describes a *different* Rogers Pass campaign (dated 2025-03-01 to 2025-03-06, one year earlier, framed with Jean-Benoit Madore as PI rather than Alexandre Langlois) and lists additional collaborators: Francis Gauthier (UQAR), Francis Meloche (UQAR/ETH Zurich), Kate Hale (UBC), Hans-Peter Marshall and Joachim Meyer (Boise State). **This is now partially corroborated by independent sources**, which raises its credibility without making it authoritative for the 2026 campaign:
    - Francis Gauthier is a confirmed real co-author on the Laliberte et al. (2018, 2021/2022) GRIMP radar papers.
    - A "Francis Meloche" (and separately a "Julien Meloche") are named among GRIMP field companions/colleagues in the PhD thesis acknowledgments.
    - The PR's named funding sources (see Funding below) are independently corroborated by the MSc thesis's real acknowledgments.
    - Despite this corroboration, the PR describes a differently-dated, differently-framed campaign and is itself AI-agent-authored, unreviewed-by-us content — 🚩 **ask the researcher directly** whether there is a related 2025 Rogers Pass campaign/dataset and whether Gauthier, Meloche, Hale, Marshall, or Meyer were involved in the 2026 campaign being documented here.
- **Collection dates:** 2026-03-03 to 2026-03-10 (confirmed at Scope Definition).
- **Geographic coverage:** Rogers Pass, Glacier National Park, BC — see Scope dimensions/Site table.
- **Instruments** (README Methodological Information section should cover each): IRIS (SSA), SMP (hardness/microstructure), SnowScope/SCOPE (hardness), dual-frequency FMCW radar (Ku/Ka), GPS (positioning), manual snow profile/pit observation (stratigraphy, per OGRS/ICSSG).
- **Standards:** OGRS (Observation Guidelines and Recording Standards for Weather, Snowpack and Avalanches, Canadian Avalanche Association — cited as the CAA 2007, 2016, and current 2024 editions across sources, confirming this is GRIMP's standard governing reference for manual snow-profile methodology) and ICSSG (International Classification for Seasonal Snow on the Ground; Fierz et al., 2009) for grain-type/hardness classification. **CAAML was not mentioned in either thesis at all** — the theses use OGRS/ICSSG exclusively, unlike the CAAML-formatted `datasets/example/` archive. **To confirm with researcher/Data Preparation** which format level (raw / Excel / CSV / CAAML) is actually being deposited for this campaign's profiles, since the literature suggests OGRS/ICSSG-only recording (not necessarily CAAML export) is GRIMP's own practice, per `docs/project_context.md` §8 data-format ladder.
- **Processing stages:** SMP `.pnt` binary files are read via the `snowmicropyn` Python package (already installed in this repo's `.venv`) — likely SMP processing/software reference for the README's Software/Standards section. SNOWPACK model outputs are referenced throughout both theses as the modeling target these field measurements validate — relevant only if SNOWPACK-modeled data (not just raw field measurements) are part of this deposit; **to confirm with Data Preparation.**
- **Related publications/datasets/software:**
  - `datasets/example/` (DOI 10.20383/103.01523) — related GNP snowpit archive, see above.
  - `snowmicropyn` (SLF) — SMP file reader/processor, https://github.com/slf-dot-ch/snowmicropyn
  - Niviz (https://niviz.org/) and the GRIMP `Caaml_Reader` script (https://github.com/grimp-lab/Caaml_Reader) — relevant only if this campaign's profiles are deposited as CAAML.
- **File-relationship notes:** IRIS, SMP, SnowScope, and radar files are organized per site/day, each expected to reference a manual snow-pit/profile as the ground-truth anchor (GRIMP's standard validation methodology, confirmed across both theses). Exact folder/file relationships: `to-be-confirmed-from-files` (Explore Data).
- **Unresolved README fields:** licenses/restrictions (§Sharing/Access 1), links to publications citing/using the data (§Sharing/Access 2), citation (§Sharing/Access 6), full DATA & FILE OVERVIEW and DATA-SPECIFIC INFORMATION sections (depend on Explore Data + Data Preparation). Field of Research (CRDC 2020) candidate: RDF20802 "Geomatics engineering" — **to confirm, this is a Step 6 decision.**

---

## Citable references

**Instrument design / methodology:**

- Montpetit, B., Royer, A., Langlois, A., Cliche, P., Roy, A., Champollion, N., Picard, G., Domine, F., and Obbard, R. (2012). "New shortwave infrared albedo measurements for snow specific surface area retrieval." *Journal of Glaciology*, 58(211), 941–952. doi:10.3189/2012JoG11J248 — **the IRIS instrument design/validation paper**, transcribed directly from the MSc thesis's own bibliography (both theses cite this as the IRIS reference; DOI confirmed from primary-source transcription).
- Gallet, J.-C., Domine, F., Zender, C. S., and Picard, G. (2009). "Measurement of the specific surface area of snow using infrared reflectance in an integrating sphere at 1310 and 1550 nm." *The Cryosphere*, 3, 167–182. doi:10.5194/tc-3-167-2009 — foundational integrating-sphere method that IRIS follows/extends.
- Schneebeli, M., and Johnson, J. B. (1998). "A constant-speed penetrometer for high-resolution snow stratigraphy." *Annals of Glaciology*, 26, 107–111. — original SMP instrument design paper.
- Schneebeli, M., Pielmeier, C., and Johnson, J. B. (1999). "Measuring snow microstructure and hardness using a high resolution penetrometer." *Cold Regions Science and Technology*, 30, 101–114. doi:10.1016/S0165-232X(99)00030-0 — SMP microstructure/hardness reference, transcribed from MSc thesis bibliography.
- Proksch, M., Löwe, H., and Schneebeli, M. (2015). "Density, specific surface area, and correlation length of snow measured by high-resolution penetrometry." *Journal of Geophysical Research: Earth Surface*, 120(2), 346–362. doi:10.1002/2014JF003266 — SMP density/microstructure retrieval reference.
- Hagenmuller, P., Reuter, B., van Herwijnen, A., Ramseyer, V., and Caillol, J. (2024). "Evaluation of the Snow Penetrometer SCOPE." *Proceedings, International Snow Science Workshop (ISSW)*, Tromso, Norway, pp. 1196–1201. — independent third-party evaluation of the SnowScope/SCOPE instrument (manufacturer: PropagationLabs). Not a GRIMP paper; not mentioned in either Madore thesis. Key source for SnowScope's measurement principle and accuracy/repeatability vs. SMP.
- Elder, K., Keskinen, Z., McCaslin, C., Valentine, A., and Marshall, H.-P. (2023). "Comparisons of vertical snow hardness profiles using the SnowMicroPen, snow Scope, and manual methods." *International Snow Science Workshop*, Bend, OR, pp. 1445–1446. — companion/precursor SnowScope vs. SMP vs. manual comparison paper.

**Radar (GRIMP instrument lineage):**

- Pomerleau, P., Royer, A., Langlois, A., Cliche, P., Courtemanche, B., Madore, J.-B., Picard, G., and Lefebvre, E. (2020). "Low Cost and Compact FMCW 24 GHz Radar Applications for Snowpack and Ice Thickness Measurements." *Sensors*, 20(14), 3909. doi:10.3390/s20143909 — the commercial IMST Sentire™ sR1200-based 24 GHz FMCW radar hardware GRIMP has deployed at Fidelity since fall 2017; total field of view 65° azimuth / 24° longitudinal, 2.5 GHz bandwidth, 6 cm range resolution in air (2 cm achievable). This is very likely the physical unit behind the `ka` folder in this campaign.
- Laliberte, J., Langlois, A., Royer, A., Madore, J.-B., and Gauthier, F. (2022). "Retrieving dry snow stratigraphy using a versatile low-cost frequency modulated continuous wave (FMCW) K-band radar." *Physical Geography*, 43(3), 308–332. doi:10.1080/02723646.2021.2008104 — companion retrieval-methodology paper for the 24 GHz system, confirmed by independent web search. Note: one sub-agent's transcription of the PhD thesis bibliography also listed an apparently separate 2021 entry ("Retrieving high contrasted interfaces in dry snow using a FMCW Ka-band radar...") under the same DOI — **likely the same article under an earlier/working title**, not verified as a second distinct paper; treat as one publication unless confirmed otherwise.
- Laliberte, J., Langlois, A., Royer, A., Madore, J.-B., and Gauthier, F. (2018). "Retrieving snow stratigraphic information using a Frequency Modulated Continuous Wave (FMCW) Ka-band radar." *International Snow Science Workshop*, Innsbruck, Austria, October 2018. — earlier conference-paper version of the Ka-band retrieval work; GRIMP's own papers use "Ka-band" for this 24 GHz system.
- Kramer, D., Langlois, A., Royer, A., Madore, J.-B., King, J., and McLennan, D. (2023). "Assessment of Arctic snow stratigraphy and water equivalent using a portable Frequency Modulated Continuous Wave (FMCW) RADAR." *Cold Regions Science and Technology*, 205, 103683. doi:10.1016/j.coldregions.2022.103683 — Arctic deployment of the same portable-FMCW-radar hardware lineage; useful supporting reference if the `dku` system shares hardware ancestry.
- Derksen, C. et al. (2019). Terrestrial Snow Mass Mission (TSMM) concept — cited in-text only in the PhD thesis as "(Derksen et al., 2019)"; full bibliographic entry not captured by the sub-agent's excerpt. **To confirm** exact citation if the README wants to reference the satellite-mission context for the dual-Ku radar directly.

**Standards:**

- Canadian Avalanche Association (2016). *Observation Guidelines and Recording Standards for Weather, Snowpack and Avalanches (OGRS)*, 8th ed. — cited verbatim in the PhD thesis bibliography (an earlier MSc-thesis citation references a 2007 edition; the current public edition as of 2026 is 2024 — https://cdn.ymaws.com/www.avalancheassociation.ca/resource/resmgr/docs/ogrs/ogrs2024web.pdf). Recommend citing the 2024 edition as current best practice, while noting the standard's continuity across editions.
- Fierz, C., et al. (2009). *The International Classification for Seasonal Snow on the Ground (ICSSG)*. IHP-VII Technical Documents in Hydrology N°83, IACS Contribution N°1, UNESCO-IHP, Paris. — grain-type/hardness classification standard used alongside OGRS in GRIMP's own snow-pit protocol (PhD thesis, p.38).
- CAAML (Canadian Avalanche Association Markup Language) / "Snow Profile IACS" schema, derived from CAAML v5.0. http://caaml.org/ — candidate exchange-format standard **only if** Data Preparation confirms CAAML deposit (as in `datasets/example/`); note neither Madore thesis uses or mentions CAAML, so this may not reflect GRIMP's actual practice for raw field data.

**Hardness instrumentation (patch, added at QC reconciliation):**

- Borstad, C. P., and McClung, D. M. (2011). "Thin-blade penetration resistance and snow strength." *Journal of Glaciology*, 57(202), 325–336. doi:10.3189/002214311796405924 — design/validation reference for the Blade Hardness Gauge (BHG), a third hardness instrument present in this campaign's stratigraphy workbooks (`BHG` sheet) alongside SMP and SnowScope. Not mentioned in either Madore thesis; resolves a documentation-coverage gap flagged by Explore Data.

**Software:**

- `snowmicropyn` — SLF (WSL Institute for Snow and Avalanche Research). Python package to read/export/post-process `.pnt` files recorded by SnowMicroPen. https://github.com/slf-dot-ch/snowmicropyn (GPL license).

**GRIMP methodology/context papers (author-network continuity, useful for README background):**

- Madore, J.-B., Fierz, C., and Langlois, A. (2022). "Investigation into percolation and liquid water content in a multi-layered snow model for wet snow instabilities in Glacier National Park, Canada." *Frontiers in Earth Science*, 10, 1–19.
- Madore, J.-B., Langlois, A., and Cote, K. (2018). "Evaluation of the SNOWPACK model's metamorphism and microstructure in Canada: a case study." *Physical Geography*, 39(5), 406–427.
- Madore, J.-B., Cote, K., and Langlois, A. (2016, submitted). "Evaluation of the SNOWPACK model metamorphism and microstructure in a Canadian context: A case study for snow stability assessment." *Cold Regions Science and Technology* (MSc thesis core chapter).
- Bellaire, S., Jamieson, B., Thumlert, S., Goodrich, J., and Statham, G. (2016). "Analysis of long-term weather, snow and avalanche data at Glacier National Park, B.C., Canada." *Cold Regions Science and Technology*, 121, 118–125. — co-author Jeff Goodrich is the same Parks Canada contact thanked in the PhD thesis acknowledgments.
- Schleiss, V. (1990). "Rogers Pass Snow Avalanche Control – A Summary, Glacier National Park, British Columbia, Canada." — source for the "~200 avalanche paths / 134 highway locations" figure.

**Source theses themselves:**

- Madore, J.-B. (2023). *Etude Integree de la Percolation de l'Eau dans le Manteau Neigeux du Parc National des Glaciers, Colombie-Britannique, Canada* [Integrated Study of Water Percolation in the Snowpack of Glacier National Park, British Columbia, Canada]. PhD thesis, Universite de Sherbrooke. Supervisors: Alexandre Langlois and Charles Fierz (SLF, Davos).
- Madore, J.-B. (2016). *Evaluation de la modelisation de la taille de grain de neige du modele multi-couches thermodynamique SNOWPACK: implication dans l'evaluation des risques d'avalanches.* MSc thesis, Universite de Sherbrooke. Supervisor: Alexandre Langlois.

---

## Glossary

| Term | Tag | Detail |
|---|---|---|
| IRIS | instrument | InfraRed Integrating Sphere. GRIMP-built instrument (Montpetit et al., 2012, following Gallet et al., 2009). Measures snow SSA (m²/kg) via infrared reflectance: 10-cm Labsphere integrating sphere, 3 ports (illumination laser ~1310–1315 nm; sample port; InGaAs photodiode detector), dark-current-corrected. Sample held in a 10-cm-diameter, 6-cm-high aluminum cylinder. Operated in "heavy" (full pit) and "light" (portable, spatial-variability survey) field modes. GRIMP-operated resolution/protocol as used in this specific campaign: `to-be-confirmed-from-files`. |
| SMP (SnowMicroPen) | instrument | Motorized, constant-speed (~20 mm/s) high-resolution snow penetrometer, developed at SLF Davos (Schneebeli & Johnson, 1998; Schneebeli et al., 1999). Vertical resolution ≈0.004 mm ("263 measurements per mm"), force output in N. Used to derive density, SSA, and correlation length via Proksch et al. (2015); also cross-validated against radar-detected stratigraphic interfaces in GRIMP's own work (PhD thesis Ch. 6). Raw output: `.pnt` binary files, read via `snowmicropyn` (Python, SLF, GPL license). |
| SnowScope / SCOPE | instrument | Lightweight (0.28 kg), hand-push digital penetrometer (manufacturer: PropagationLabs). Optical/reflectance depth sensing (analogous to a computer-mouse sensor) paired with a force sensor; Bluetooth link to a smartphone recorder. Nominal range 0.2–1.6 m depth, 3–550 kPa force, 1 mm depth resolution, 1.5 mm layer resolution. Independent ISSW evaluation (Hagenmuller et al., 2024) found repeatability comparable to SMP but a device-dependent positive hardness bias (~30–100%) and a small depth bias (~−4 to −6 cm); correctly reproduces profile shape and weak-layer position. Measures hardness/stratigraphy only, not density/SSA/temperature directly. Not used or mentioned in either Madore thesis — likely a recent addition to GRIMP's field kit. |
| Dual-frequency FMCW radar (Ku/Ka) | instrument | Portable frequency-modulated continuous-wave radar, operated here at two bands (folders `dku`, `ka`). Well-supported inference (not yet file-confirmed): `ka` = GRIMP's existing 24 GHz system (IMST Sentire™ sR1200; Pomerleau et al., 2020; called "Ka-band" in GRIMP's own papers, e.g. Laliberte et al. 2018/2021/2022, despite sitting at the K/Ka boundary), installed at Fidelity since fall 2017. `dku` = a newer dual-Ku-band (13.5/17.5 GHz) system, explicitly described in the 2023 PhD thesis as "planned for installation at Fidelity" to match the satellite Terrestrial Snow Mass Mission (TSMM; Derksen et al., 2019) — the 2026 campaign is very likely the field realization of that plan. Measures snow depth and internal stratigraphic interfaces (ice crusts, layer boundaries) toward SWE retrieval. Exact frequencies/bandwidth/deployment geometry as operated in 2026: `to-be-confirmed-from-files`. |
| GPS | instrument | Positioning of profile/measurement locations. Not mentioned in either source thesis (zero hits) — appears new to this campaign's instrument set. Unit type, accuracy, datum: `to-be-confirmed-from-files`. |
| SSA (specific surface area) | variable | Surface area of the snow ice–air interface per unit mass (m²/kg); a key microstructural property controlling metamorphism rate, albedo, and microwave/optical scattering. |
| OGRS | standard | Observation Guidelines and Recording Standards for Weather, Snowpack and Avalanches. Canadian Avalanche Association manual (cited as 2007/2016 editions in the two theses; current edition 2024) defining standard field techniques for snow, weather, and avalanche observation; governs GRIMP's manual snow-pit/profile protocol. |
| ICSSG | standard | International Classification for Seasonal Snow on the Ground (Fierz et al., 2009). Used alongside OGRS in GRIMP's own snow-pit protocol for grain type/size/hardness classification. |
| CAAML | standard | Canadian Avalanche Association Markup Language — XML grammar (modeled on OGC's GML) for exchanging avalanche-safety observations, incl. a "Snow Profile IACS" schema derived from CAAML v5.0. Used by the related `datasets/example/` dataset; **not used or mentioned in either Madore thesis** — confirm before assuming it applies to this campaign's deposit format. |
| BHG (Blade Hardness Gauge) | instrument | Thin-blade penetrometer for quantitative snow hardness measurement, designed by Fraser Instruments Ltd. based on the thin-blade tool introduced by Borstad & McClung (2011). Reduces the known operator bias of the manual hand-hardness test; typically inserted perpendicular to the slope angle, multiple insertions per layer (matches the triplet-value rows — e.g. `2.03-1.83-2.42` — seen in the `BHG` sheet of this campaign's stratigraphy workbooks, §2 of `data_exploration.md`). Resolves the QC documentation-coverage gap flagged by Explore Data (instrument present in files, undocumented in the original research pass). `literature-derived` (patch, added at QC reconciliation) |
| GRIMP | organization | Groupe de Recherche Interdisciplinaire sur les Milieux Polaires, Universite de Sherbrooke (Departement de geomatique appliquee), founded 2014 by Alexandre Langlois. Research axes include Avalanche (this campaign, active in GNP since 2014) and Arctic/MOACC. |
| snowmicropyn | processing | Python package (SLF, GPL license) to read, export, and post-process SMP `.pnt` binary files. https://github.com/slf-dot-ch/snowmicropyn |
| SNOWPACK | technique | Multi-layer thermodynamic snowpack model (SLF); the modeling target that GRIMP's field measurements (IRIS, SMP, radar) are repeatedly used to validate/calibrate across both Madore theses. Relevant only if SNOWPACK outputs are part of this deposit — `to-be-confirmed`. |
| Manual snow profile / snowpit | technique | Standard field method: dig a snow pit, record stratigraphy (grain type/size, hardness, temperature, density at ~5 cm intervals) and stability test results (e.g. compression test) layer-by-layer, per OGRS/ICSSG protocol. |

---

## Source notes (claim → source mapping)

| Claim | Source |
|---|---|
| PI Alexandre Langlois founded GRIMP 2014, Universite de Sherbrooke, Avalanche research axis w/ Parks Canada collaboration | `docs/project_context.md` §1 |
| Related published FRDR dataset (DOI 10.20383/103.01523), CAAML format, OGRS-governed, CC BY-NC 4.0 Parks Canada Open Licence | `datasets/example/README.txt`, `docs/project_context.md` §6 |
| Andrew Jones and Catherine Brown (Parks Canada, co-authors of the related dataset) independently confirmed as GNP avalanche-safety-group collaborators | `papers/madore_jean-benoit_PhD_2023.pdf`, acknowledgments pp.4-5 (via sub-agent) |
| Snowpit data format ladder (raw / Excel / CSV / CAAML) | `docs/project_context.md` §8 |
| Controlled-vocabulary keywords | `docs/controlled_vocabulary.md`, `docs/project_context.md` §7 |
| IRIS full design description, wavelength, sphere/cylinder dimensions, dark-current protocol, exact citation (Montpetit et al. 2012, DOI 10.3189/2012JoG11J248) and foundational Gallet et al. (2009) reference | `papers/Madore_Jean_Benoit_MSc_2016.pdf`, §3.2.1 (via sub-agent) |
| IRIS "heavy"/"light" field modes, 1315 nm laser variant | `papers/madore_jean-benoit_PhD_2023.pdf`, p.38 (via sub-agent) |
| SMP resolution (263 measurements/mm), force units, exact citations (Schneebeli & Johnson 1998; Schneebeli et al. 1999; Proksch et al. 2015) | `papers/Madore_Jean_Benoit_MSc_2016.pdf`, §3.2.2 (via sub-agent) |
| SMP-vs-radar cross-validation in GRIMP's own work | `papers/madore_jean-benoit_PhD_2023.pdf`, Ch. 6 / Figs 6.6, 6.9 (via sub-agent) |
| snowmicropyn package purpose/license | Web search → https://github.com/slf-dot-ch/snowmicropyn |
| 24 GHz FMCW radar (IMST Sentire sR1200) full specs, install date/location, Pomerleau et al. (2020) citation | `papers/madore_jean-benoit_PhD_2023.pdf`, pp.41, 96 (via sub-agent) |
| Dual-Ku (13.5/17.5 GHz) radar "planned for installation at Fidelity" matching TSMM | `papers/madore_jean-benoit_PhD_2023.pdf`, pp.117-118 (via sub-agent) |
| Laliberte et al. (2018/2021/2022) Ka-band radar papers, Kramer et al. (2023) Arctic portable FMCW radar paper | `papers/madore_jean-benoit_PhD_2023.pdf`, publication list pp.135-137 (via sub-agent); cross-checked by direct web search for the 2022 Physical Geography entry |
| OGRS (CAA 2007/2016 editions), ICSSG (Fierz et al. 2009), full snow-pit protocol (temperature/10cm, density/5cm wedge cutter, compression test) | Both theses (via sub-agents); current 2024 edition confirmed by direct web search |
| CAAML absent from both theses | Both sub-agents' full-text searches (zero hits) |
| SnowScope/SCOPE full technical description, specs, accuracy/repeatability, comparison to SMP, related citations; absent from both theses | `papers/snowSCOPE.pdf` (read in full directly) — Hagenmuller et al. 2024 ISSW paper |
| Round Hill (2100 m, 500 m uphill of Fidelity) and Hermit (1950 m) elevations; Rogers Pass regional climate/terrain/avalanche-control description | `papers/madore_jean-benoit_PhD_2023.pdf`, Table 3.1 p.36, pp.35, 62, 94 (via sub-agent) |
| Jim Bay and Gopher Butte absent from both theses | Both sub-agents' full-text searches (zero hits) |
| Gopher Butte approximate coordinates (unrelated 2005-2006 study, not GRIMP) | Web search (ResearchGate figure caption) |
| MSc-thesis campaign funding: SAR-NIF, NSERC, CFI, CEN | `papers/Madore_Jean_Benoit_MSc_2016.pdf`, acknowledgments p.45 (via sub-agent) |
| PhD-thesis acknowledgments name no specific grant/funder, only people and partner organizations (Avalanche Quebec, Parks Canada, SLF) | `papers/madore_jean-benoit_PhD_2023.pdf`, acknowledgments pp.4-5 (via sub-agent) |
| Parks Canada research/collection permit requirement for GNP fieldwork | Web search (parks.canada.ca research-permit pages) |
| CRDC 2020 candidate Field of Research code (RDF20802, Geomatics engineering) | Web search (StatCan CRDC 2020 v2.0 classification browser) |
| Unverified sibling-dataset lead (PR #2, fork repo, different campaign dates/PI, additional collaborator names); partially corroborated (Gauthier, Meloche, SAR-NIF funding name) by thesis content | WebFetch of `github.com/vincent-beauregard-ielab/grimp-frdr-helper/pull/2` and its `.diff`, cross-checked against both theses — still flagged as unverified for this specific 2026 campaign |

---

## Site table

| Site name | Coordinates | Elevation | Description | Source |
|---|---|---|---|---|
| Rogers Pass (general area / valley-bottom station) | Not precisely pinned in literature | 1,315 m (valley-bottom weather station) | Parks Canada highway-corridor avalanche-forecasting area, Selkirk Mountains; artillery avalanche control since 1962; ~200 avalanche paths affecting 134 highway locations; long-running snow study plots since the early 1960s | `papers/madore_jean-benoit_PhD_2023.pdf` (Table 3.1, p.36; p.35) |
| Fidelity (Mount Fidelity) | Not precisely pinned; web search places it near 51°14'N, 117°42'W | 1,905 m | GRIMP's primary GNP instrumented station: flat site on the east flank of Mount Fidelity at treeline, restricted-access research area; site of the group's 24 GHz radar (since 2017), visibility sensor (2016), and snow-temperature/permittivity mast (2018); also where Parks Canada performs its own avalanche-forecasting measurements. One of the snowiest places in Canada (>15 m cumulative seasonal snowfall, >4 m max depth) | `papers/madore_jean-benoit_PhD_2023.pdf` (pp.36, 62, 94); `papers/Madore_Jean_Benoit_MSc_2016.pdf` (§3.1, p.33-34) |
| Round Hill | Not given (no coordinate table in either thesis) | 2,100 m | Located ~500 m uphill from Mount Fidelity; used historically as a supplementary wind-data station when Fidelity's own wind sensor was unavailable (early season) | `papers/madore_jean-benoit_PhD_2023.pdf` (Table 3.1 p.36; p.64) |
| Jim Bay | Not found in either thesis or general snow-science literature | Unknown | No literature match under this name as a GNP snow-study site; the only web hit is an unrelated informal highway-switchback place name at Rogers Pass | `to-be-confirmed-from-files` |
| Gopher Butte | 51°14'17" N, 117°42'10" W (unrelated 2005-2006 study, not GRIMP) | 1,940 m | Treeline knoll near Mount Fidelity; not mentioned in either Madore thesis | Web search only; `to-be-confirmed-from-files` |
| Hermit Meadows | Not given (thesis calls the station only "Hermit," no coordinate) | 1,950 m (as "Hermit" weather station) | Appears only in Madore's weather-station instrument table with no narrative description; general web sources place "Hermit Meadows" in the Connaught Creek drainage, alpine terrain above treeline, near Mount Tupper/Hermit Mountain/Mount Rogers/Swiss Peak | `papers/madore_jean-benoit_PhD_2023.pdf` (Table 3.1, p.36); web search for descriptive context |

Elevations for Fidelity, Round Hill, Hermit, and Rogers Pass are now literature-confirmed from GRIMP's own instrument table (same station names used by this campaign) — a substantially stronger baseline than the earlier general-web approximations. Precise coordinates for all sites, and any confirmation of Jim Bay/Gopher Butte as actual 2026 site names, remain `to-be-confirmed-from-files`; Explore Data should extract per-site, per-profile coordinates from the GPS files and instrument headers.

---

## Proposed README.txt updates

*(For the human-in-the-loop orchestrator to apply — do not edit README.txt directly, per task instructions.)*

### Section: `2. Author Information`

```
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

	⚠️ Note: institutions, emails, and precise roles for the full team are still unconfirmed. Research also surfaced a partially-corroborated lead (see artifacts/research.md) suggesting possible additional collaborators (F. Gauthier, F. Meloche, K. Hale, H.-P. Marshall, J. Meyer) from what may be a related prior-season Rogers Pass campaign — 🚩 ask the researcher directly whether any of these people were involved in the 2025-2026 campaign being deposited here.
```

### Section: `4. Geographic location of data collection`

Append after the existing sentence:

```
⚠️ Site elevations below are confirmed from GRIMP's own weather-station records (same station names used by this campaign); precise coordinates for this campaign's actual measurement locations are still pending confirmation from GPS/instrument files (Explore Data step):
- Fidelity (Mount Fidelity): GRIMP's primary GNP research station, 1,905 m, treeline elevation on the east flank of Mount Fidelity.
- Round Hill: 2,100 m, ~500 m uphill from Fidelity.
- Hermit Meadows: 1,950 m (recorded as "Hermit" in GRIMP's station records), alpine terrain in the Connaught Creek drainage.
- Jim Bay, Gopher Butte: 🚩 no match found in GRIMP's own published site records for these names; confirm site identity/location with the field team before finalizing.
```

### Section: `5. Information about funding sources`

```
5. Information about funding sources that supported the collection of the data:
⚠️ GRIMP's Glacier National Park/Fidelity research program has previously been funded by the National Search and Rescue Secretariat New Initiatives Fund (SAR-NIF), the Natural Sciences and Engineering Research Council of Canada (NSERC), the Canada Foundation for Innovation (CFI), and the Centre d'etudes nordiques (CEN) (per Madore's 2016 MSc thesis acknowledgments). 🚩 These are candidate/plausible funders for the 2025-2026 campaign given program continuity, but the specific grant(s)/award number(s) active for THIS campaign must be confirmed directly with the PI before finalizing this section.
```

### Section: `METHODOLOGICAL INFORMATION` (currently a placeholder)

```
---------------------------
METHODOLOGICAL INFORMATION
---------------------------

Manual snow profiles were recorded following the Observation Guidelines and Recording Standards for Weather, Snowpack and Avalanches (OGRS, Canadian Avalanche Association, 2024 ed., https://www.avalancheassociation.ca/) and the International Classification for Seasonal Snow on the Ground (ICSSG; Fierz et al., 2009), recording layering, grain type/size, hardness, and temperature (typically every 10 cm) and density (typically every 5 cm).

Specific surface area (SSA) was measured using IRIS (InfraRed Integrating Sphere), a GRIMP-built infrared-reflectance instrument (10-cm integrating sphere, ~1310-1315 nm laser; Montpetit et al., 2012, following Gallet et al., 2009).

Snow hardness/stratigraphy profiles were measured with two complementary penetrometers: the SnowMicroPen (SMP; motorized, ~20 mm/s, ~0.004 mm vertical resolution; Schneebeli & Johnson, 1998; Schneebeli et al., 1999), whose raw `.pnt` files are processed with the `snowmicropyn` Python package (SLF); and SnowScope/SCOPE (hand-push, optical depth-sensing, 1 mm depth resolution; Hagenmuller et al., 2024).

Snow depth and internal stratigraphy were also measured with a dual-frequency FMCW radar operated at two bands (folders `dku` and `ka` in the raw data). ⚠️ The `ka` data are likely GRIMP's existing 24 GHz radar (IMST Sentire sR1200; Pomerleau et al., 2020; Laliberte et al., 2018/2022), operated at Fidelity since 2017; the `dku` data are likely a newer dual-Ku-band (13.5/17.5 GHz) system matching the planned satellite Terrestrial Snow Mass Mission (TSMM, Derksen et al., 2019), described as planned infrastructure in Madore's 2023 PhD thesis. 🚩 Exact center frequencies and deployment protocol as operated in this campaign are pending confirmation from file headers/field notes.

Measurement locations were recorded with GPS. ⚠️ Unit type and accuracy pending confirmation — not documented in prior GRIMP publications for this site.

🚩 This section will be finalized once acquisition-protocol details are confirmed from file-level metadata (Explore Data / Quality Control steps).
```

---

## Proposed metadata.yaml updates

```yaml
keywords:
  - avalanche hazard assessment
  - snow profile
  - stability test
  - specific surface area (SSA)
  - radar
  - FMCW radar
  - snow micropenetrometry
  - SnowMicroPen
  - snow stratigraphy
  - Rogers Pass
  - Glacier National Park

field_of_research: ""   # Candidate: RDF20802 "Geomatics engineering" (CRDC 2020 v2.0) — NOT confirmed, Step 6 decision.

authors:
  # Order/roles/ORCID unconfirmed — do not treat as final. No ORCID iDs found for any team member.
  - last_name: "Langlois"
    first_name: "Alexandre"
    affiliations: ["Universite de Sherbrooke (GRIMP)"]
    orcid: ""
  - last_name: "Madore"
    first_name: "Jean-Benoit"
    affiliations: ["Universite de Sherbrooke (GRIMP)"]
    orcid: ""
  - last_name: "Imbach"
    first_name: "Benjamin"
    affiliations: ["Universite du Quebec a Rimouski"]
    orcid: ""
  - last_name: "Allet"
    first_name: "Nicolas"
    affiliations: ["Universite de Sherbrooke (GRIMP)"]  # to confirm
    orcid: ""
  - last_name: "Delage"
    first_name: "Marie-Clara"
    affiliations: []  # to confirm
    orcid: ""
  - last_name: "Paquette"
    first_name: "Violaine"
    affiliations: []  # to confirm
    orcid: ""
  - last_name: "Cramb"
    first_name: "Megan"
    affiliations: []  # to confirm
    orcid: ""
  - last_name: "Marchand"
    first_name: "Nicolas"
    affiliations: []  # to confirm — possibly the same "Nicolas Marchand" thanked as a GRIMP research-group colleague in the PhD thesis acknowledgments
    orcid: ""

related_identifiers:
  - identifier: "https://doi.org/10.20383/103.01523"
    relation_type: "IsRelatedTo"   # candidate; confirm exact DataCite relation with researcher — related GNP snowpit archive; shared Parks Canada collaborators (Jones, Brown) independently confirmed via thesis acknowledgments

funding:
  # Candidate program-level funders for GRIMP's GNP/Fidelity research (confirmed via Madore 2016 MSc thesis acknowledgments) — NOT confirmed as the specific funder(s) for THIS 2026 campaign. Researcher must confirm before finalizing.
  - funder: "National Search and Rescue Secretariat New Initiatives Fund (SAR-NIF)"
    award_number: ""
    award_title: ""
  - funder: "Natural Sciences and Engineering Research Council of Canada (NSERC)"
    award_number: ""
    award_title: ""
  - funder: "Canada Foundation for Innovation (CFI)"
    award_number: ""
    award_title: ""

geographic_coverage:
  place_name: "Rogers Pass, Glacier National Park"
  country: "Canada"
  province: "British Columbia"
  # point/bounding_box: leave blank pending Explore Data's file-derived coordinates. Elevations for Fidelity (1905 m), Round Hill (2100 m), and Hermit Meadows (1950 m) are now literature-confirmed (GRIMP's own station records) but lack lat/lon — do not populate point/bounding_box from this document's approximate values.
```

---

## Open items for Quality Control / researcher confirmation

1. Exact IRIS wavelength/protocol as operated in this campaign (theses give 1310-1330 nm range across different instrument generations).
2. Confirm the `dku`/`ka` radar-folder-to-physical-unit mapping proposed above (dual-Ku 13.5/17.5 GHz = TSMM-matching system; Ka = existing 24 GHz Pomerleau/Laliberte system) against file headers/field notes.
3. GPS unit type and accuracy (undocumented in prior GRIMP literature).
4. Precise coordinates for all five sites as actually visited in 2026 (literature supplies elevations for Fidelity/Round Hill/Hermit only, no coordinates for any site, and no match at all for Jim Bay/Gopher Butte).
5. Confirm whether SAR-NIF/NSERC/CFI/CEN funding (2016-era) is still the active funding for this 2026 campaign, or whether a newer grant applies.
6. Team member institutional affiliations, emails, and roles for Allet, Delage, Paquette, Cramb, Marchand.
7. Whether the unverified fork-repo PR (#2) describes a genuinely related prior-season dataset, and whether any of its named collaborators (Gauthier, Meloche, Hale, Marshall, Meyer) participated in the 2025-2026 campaign.
8. Which snow-profile data format level (raw / Excel / CSV / CAAML) is being deposited — neither Madore thesis uses CAAML, unlike the related `datasets/example/` dataset.
9. CRDC 2020 Field of Research code — confirm RDF20802 or identify a better-fitting code.
10. Full Derksen et al. (2019) TSMM citation, if the README should reference the satellite-mission context directly.
