# Documentation Preparation

Complete the README.txt, finalize METADATA.yaml, insert the review preamble, and run the first preflight check. This step transforms the draft README built up through Steps 1–5 into a review-ready document.

**Autonomy:** Level 2 — Public-facing artifact, needs careful review.

**Requires:** Data Preparation complete.

## Sections to complete

At this point, identity sections are already filled (Step 1) and structural stubs have been partially updated by Research (Step 2) and Explore Data (Step 3). Remaining work:

- **Data & file overview** — Finalize from `data_exploration.md` and the `frdr_data/` file tree in `DATA_PREPARATION.md`
- **Methodological information** — Complete from `research.md` (see methodology transfer checklist below)
- **Data-specific sections** — Variable lists, missing data codes, units
- **Sharing/access** — License, citation, related datasets
- **General information** — Verify title, authors, dates, geographic location, funding are final

Remove all `⚠️ [placeholder — to be filled at Step 6]` stubs. Every section must contain real content. Flag any section where information is genuinely missing or requires a researcher decision with 🚩.

## Methodology transfer checklist

The methods section is where most README quality issues occur. For each instrument, technique, and standard listed in `research.md` (glossary entries tagged `instrument`, `technique`, or `standard`), the README must include:

1. **A concrete description** of how it was used — not just the instrument name but the acquisition protocol (altitude, resolution, sampling parameters, transect design, etc.)
2. **Model name and version** (firmware, software edition) when known
3. **An inline citation** to the design paper, standard document, or methodology reference, formatted as: Author (Year), Title, DOI/URL. Use the citable-references section from `research.md` as the source for these citations.
4. **Processing chain** — what software or workflow transforms raw output into the deposited files

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

Inspect file names from the data exploration artifact and the deposit-ready file list. If multiple conventions coexist, document each.

## File list granularity

The file list must be detailed enough that a reader can understand what each file contains without opening folders. Two acceptable approaches:

1. **File-type-first** (preferred for multi-instrument datasets): group by data type (e.g., "Stratigraphy workbooks", "SnowScope profiles", "Radar exports"), then list representative file names with descriptions.
2. **Folder-first**: list each folder, then describe the file types found within it with counts and representative names.

Avoid folder-only summaries that hide the actual file types.

## Reading and reusing data

Include a section (after methodological information or as a subsection) that tells a new user how to open and work with the deposited files. For each file format in the deposit:

- Name the format and any non-obvious structure
- Recommend software or libraries for reading (with URLs)
- If the depositors provide reader scripts or conversion tools, link them here

## Additional coverage

Make sure the README also accounts for:

- Relationship between files and folders
- Ancillary or excluded files
- Standards and calibration notes (with URLs for standard documents)
- Quality-assurance notes
- Environmental/experimental conditions — concrete values from the data (snow depth range, temperature range, elevation range)
- Detailed attribution for any external data sources (title, authors, institution, DOI, access link, date accessed)
- Software/instrument names and versions
- All URLs for referenced software, standards, and tools

## Sources

Use the README.txt draft (accumulated through Steps 1–5), `artifacts/research.md`, `artifacts/data_exploration.md` + notebook, and `DATA_PREPARATION.md`. The README describes the deposit-ready files in `frdr_data/`, not the raw originals. Use `datasets/example/README.txt` as a reference for tone and level of detail.

## 🚩 marker placement

After completing all sections, place 🚩 on any item requiring a researcher decision:
- Facts the agent cannot confirm from available sources
- Scope decisions that were flagged in `DATA_PREPARATION.md` but not yet resolved
- Author details, contact information, or funding specifics that need researcher confirmation
- Any sentence where the agent is uncertain

Place ⚠️ on critical context the researcher must understand but does not need to act on (e.g., a known limitation, a non-obvious file structure choice).

## Insert review preamble

Add the following block at the very top of `README.txt` (before the dataset title):

```
⚠️ REVIEW INSTRUCTIONS — REMOVE BEFORE DEPOSIT
This document is under review for FRDR deposit.
🚩 marks items requiring your decision.
⚠️ marks critical context you must understand.
Your companion review document is DATA_PREPARATION.md.
Notebooks and artifacts/ are reference material — you do not need to review them.
----------------------------------------------------------------
```

(The full template is in AGENTS.md.)

## METADATA.yaml finalization

Update `METADATA.yaml` with any remaining fields that are now confirmed:
- Final bounding box coordinates
- Final date range
- Any keywords refined during documentation
- Related identifiers if applicable

## Validation before first preflight

1. **Template coverage**: Compare README against `docs/FRDR-template_README.txt` section by section. No section should be empty or contain leftover help text.
2. **Methodology completeness**: Every glossary entry in `research.md` tagged `instrument`, `technique`, or `standard` must have a concrete description in the README methods section.
3. **Citation completeness**: Every entry in the `research.md` citable-references section must appear as an inline citation or in the related-publications section.
4. **Naming conventions**: Every distinct file-naming pattern in the deposit is documented.
5. **File list granularity**: Every folder entry describes file types with counts and representative names.
6. **Reading/reuse section**: Every deposited file format has a corresponding entry with software recommendations and URLs.
7. **URLs present**: Every referenced standard, software package, or external tool includes a URL or DOI.
8. **No leftover stubs**: `grep -c "placeholder" README.txt` must be 0.
9. **Review preamble present**: `grep -c "REVIEW INSTRUCTIONS" README.txt` must be 1.

## Run first preflight

After validation, run the preflight checks and save results to `datasets/{id}/artifacts/preflight.md`. Preflight checks at this stage:

- README completeness (no empty sections, no leftover template text, no stubs)
- Review preamble present
- `frdr_data/` file counts match `DATA_PREPARATION.md`
- `METADATA.yaml` fields complete (title at minimum; flag any missing recommended fields)
- All 🚩 items are present and documented (they are expected — not a failure)
- No 🚩 items are already resolved (that happens in Review)

A first-run preflight may show unresolved 🚩 items — that is correct. The purpose of this run is to confirm the documents are structurally complete and ready for researcher review, not that all decisions are made.

## Outputs

- `datasets/{id}/README.txt` — all sections complete, review preamble inserted, 🚩 and ⚠️ markers placed
- `datasets/{id}/METADATA.yaml` — finalized
- `datasets/{id}/artifacts/preflight.md` — first preflight run recorded
