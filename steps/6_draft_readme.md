# Draft FRDR README

Generate the dataset README from `docs/FRDR-template_README.txt`, filling in all applicable sections.

**Autonomy:** Level 2 — Public-facing artifact, needs careful review.

**Requires:** Data Preparation complete.

## Sections to fill

- General information (title, authors, dates, geographic location, funding)
- Sharing/access (license, citation, related datasets)
- Data & file overview (file list with descriptions, naming conventions)
- Methodological information (acquisition methods, processing steps, instruments, software) — see methodology transfer checklist below
- Data-specific sections (variable lists, missing data codes, units)

## Methodology transfer checklist

The methods section is where most README quality issues occur. For each instrument, technique, and standard listed in `research.md` (glossary entries tagged `instrument`, `technique`, or `standard`), the README must include:

1. **A concrete description** of how it was used — not just the instrument name but the acquisition protocol (altitude, resolution, sampling parameters, transect design, etc.)
2. **Model name and version** (firmware, software edition) when known
3. **An inline citation** to the design paper, standard document, or methodology reference, formatted as: Author (Year), Title, DOI/URL. Use the citable-references section from `research.md` as the source for these citations.
4. **Processing chain** — what software or workflow transforms raw output into the deposited files

This follows FRDR's requirement for "data collection methods employed" and "equipment/instrument names" and is standard practice in published FRDR READMEs (e.g., citing OGRS for observation standards, citing instrument design papers for custom hardware).

### Citation format in README

Cite sources inline in the relevant section, for example:

```
Manual observations follow OGRS (Canadian Avalanche Association, 2024;
https://www.avalancheassociation.ca/resource/resmgr/docs/ogrs/ogrs2024web.pdf).

The 24 GHz FMCW radar follows the design described in Pomerleau et al. (2020),
Sensors, https://doi.org/10.3390/s20143909.
```

Also list key references in the "Links to publications that cite or use the data" section.

## Naming conventions

The README must document file and folder naming patterns. If the dataset uses consistent naming (date prefixes, site codes, instrument identifiers, serial numbers), describe the convention explicitly, e.g.:

```
Naming convention: <YYYYMMDD>_<site>_<instrument>
Example: 20230724_alder25_m3m
```

Inspect file names from the data exploration artifact and the deposit-ready file list. If multiple conventions coexist (e.g., one for day folders, one for SnowScope CSVs, one for radar exports), document each.

## File list granularity

The file list must be detailed enough that a reader can understand what each file contains without opening folders. Two acceptable approaches:

1. **File-type-first** (preferred for multi-instrument datasets): group by data type (e.g., "Stratigraphy workbooks", "SnowScope profiles", "Radar exports"), then list representative file names with descriptions.
2. **Folder-first**: list each folder, then describe the file types found within it with counts and representative names.

Avoid folder-only summaries that hide the actual file types. For example, "Day 1 folder containing field data" is insufficient — the reader needs to know it contains an `.xlsx` workbook, 23 SnowScope CSVs, 8 SMP `.pnt` files, etc.

## Reading and reusing data

Include a section (after methodological information or as a subsection) that tells a new user how to open and work with the deposited files. For each file format in the deposit:

- Name the format and any non-obvious structure (e.g., "SnowScope CSVs contain metadata header rows followed by the profile table — do not read as flat CSV without preprocessing")
- Recommend software or libraries for reading (with URLs), e.g., `snowmicropyn` for `.pnt`, `pandas` for CSV, Niviz for CAAML
- If the depositors provide reader scripts or conversion tools, link them here

This follows the pattern in the published GNP example dataset, which has a dedicated "READING AND USING DATA" section.

## Additional coverage

Make sure the draft also accounts for:

- Relationship between files and folders
- Ancillary or excluded files
- Standards and calibration notes (with URLs for standard documents)
- Quality-assurance notes
- Environmental/experimental conditions — summarize concrete values from the data (snow depth range, temperature range, elevation range) rather than generic descriptions
- Detailed attribution for any external data sources (title, authors, institution, DOI, access link, date accessed)
- Software/instrument names and versions
- All URLs for referenced software, standards, and tools (OGRS, CAAML, snowmicropyn, etc.)

## Sources

Use the scope document (`artifacts/scope.md`), research artifact (`artifacts/research.md`), data exploration outputs (`artifacts/data_exploration.md` + notebook), and data preparation notebook as sources. The README should describe the deposit-ready files in `frdr_data/`, not the raw originals. Use `datasets/example/README.txt` as a reference for tone and level of detail.

## Validation

After drafting, run these checks:

1. **Template coverage**: Compare the README against `docs/FRDR-template_README.txt` section by section. Flag any template sections that are empty or missing. The draft should have no leftover template help text (lines starting with `##`).
2. **Methodology completeness**: For every glossary entry in `research.md` tagged `instrument`, `technique`, or `standard`, verify that the README methods section contains a concrete description, not just a name. Flag any missing entries.
3. **Citation completeness**: For every entry in the `research.md` citable-references section, verify it appears as an inline citation in the README or in the related-publications section. Flag any missing citations.
4. **Naming conventions**: Verify that every distinct file-naming pattern in the deposit is documented. If files follow an obvious convention that isn't described, flag it.
5. **File list granularity**: For each folder entry in the file list, verify that the file types within are described with counts and representative names — not just a folder-level summary.
6. **Reading/reuse section**: Verify that every deposited file format has a corresponding entry explaining how to open it, with software/library recommendations and URLs.
7. **URLs present**: Every referenced standard, software package, or external tool must include a URL or DOI. Flag bare names without links (e.g., "snowmicropyn" without a URL).

## Outputs

- `datasets/{id}/README.txt`
