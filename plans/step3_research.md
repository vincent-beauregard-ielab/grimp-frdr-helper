# Step 3 — Research: Rogers Pass Snow Profiles

## Goal

Write `datasets/rogers_pass_snow_profiles/artifacts/research.md` so it does two jobs:

1. satisfy the AGENTS.md research artifact requirements; and
2. capture the non-tabular information needed later to complete the FRDR README template.

This artifact feeds steps 4–6.

## Why this plan changed

Reviewing `docs/FRDR-template_README.txt` showed that the original step 3 / step 4 split did not explicitly guarantee enough information for all README sections.

The template requires more than a high-level description and glossary. Between research and exploration, we need to capture:

- title candidates and dataset scope
- people, institutions, and roles
- collection dates and geography
- funding / project / organizational context
- related publications, ancillary datasets, and derived-data relationships
- collection methods, processing methods, instruments, software, and standards
- file inventory, file relationships, naming conventions, and excluded material
- missing-value conventions, variable definitions, units, row counts, and QA notes

Step 3 should cover the contextual and methodological items that do not require full file parsing. Step 4 should cover the empirical file-level facts.

## Deliverables

### Step 3 output: `artifacts/research.md`

Required sections:

- **Dataset overall description**
  - dataset scope and campaign boundaries
  - research objective and reuse context
  - organizational and project context (GRIMP, MOACC, collaborators)
  - date range and geographic coverage known from source documents
- **README input capture**
  - candidate dataset title
  - people / institutions / likely contributor roles
  - likely funding and project linkage
  - related publications, standards, software, and external resources
  - instruments and acquisition protocols
  - processing stages mentioned in documents
  - file/folder relationship notes known before data exploration
  - open questions / unresolved fields for the README
- **Glossary**
  - key terms tagged as `instrument`, `variable`, `technique`, `acquisition`, `processing`, `initiative`, `organization`, or `standard`
- **Source notes**
  - concise claim-to-source mapping for later README drafting

### Step 4 outputs

- `notebooks/rogers_pass_snow_profiles_data_exploration.ipynb`
- `datasets/rogers_pass_snow_profiles/artifacts/data_exploration.md`

These must provide the README-ready file facts that step 3 cannot:

- file inventory by folder and data type
- naming conventions and relationships between files
- row counts / record counts where applicable
- variable names, units, dtypes, enums, and numeric ranges
- missing-value encoding and text-case consistency
- file encoding / delimiters / workbook sheet structure
- software or package requirements needed to read each format
- QA observations and anomalies

## Current dataset assumptions

- Scope is the Rogers Pass March 2025 field campaign stored under `raw_data/Rogers Pass March 2024-2025/`.
- Core scientific data types present now:
  - `13` `.xlsx`
  - `322` `.csv`
  - `172` `.TXT`
  - `79` `.pnt`
- Context-only material also exists (`.pdf`, `.docx`, `.HEIC`, `.zip`) and must be classified as either included in deposit, excluded, or supporting documentation.
- Existing `datasets/rogers_pass_snow_profiles/artifacts/research.md` and `datasets/rogers_pass_snow_profiles/README.txt` are empty, so this plan must be executed from scratch.

## Strategy

### Research sources

Use these first:

- `papers/madore_jean-benoit_PhD_2023.pdf`
- `datasets/rogers_pass_snow_profiles/docs/scope.yaml`
- meeting notes in `datasets/rogers_pass_snow_profiles/docs/meeting notes/`
- `docs/project_context.md`
- `docs/controlled_vocabulary.md`
- `datasets/example/README.txt`

Supplement with web research for:

- SnowScope instrument details
- SnowMicroPen / SMP instrument details
- IRIS snow-profile instrument details if present in scope
- FMCW K-band radar details
- CAAML and OGRS standards

### README coverage split

#### Step 3 should answer

- What is this dataset?
- Why was it collected?
- Who collected it, under which organizational/project context?
- Which instruments, protocols, and standards define the variables?
- What related papers, standards, and software should be cited?
- Which README fields still require file inspection?

#### Step 4 should answer

- What files and folders are actually present?
- Which files are scientific data vs administrative/supporting material?
- What are the real columns, variables, ranges, units, and missing codes?
- How do files map to days, sites, instruments, and processing stages?
- What quality or consistency issues need to be documented?

## Tasks

### Step 3

1. Read local source materials and capture README-relevant claims.
2. Read targeted thesis sections for snow, radar, and field-method context.
3. Search the web for instrument specs and standards not fully described locally.
4. Draft `artifacts/research.md` with the required sections above.
5. Explicitly list unresolved README fields that must be answered in step 4 or later elicitation.

### Step 4

1. Start JupyterLab with `uv run scripts/jupyter_mcp.py` before creating the notebook.
2. Create `notebooks/rogers_pass_snow_profiles_data_exploration.ipynb`.
3. Inspect each core data type:
   - Excel stratigraphy and survey workbooks
   - CSV profile / point tables
   - TXT radar and IRIS text exports
   - PNT SMP binary files
4. Summarize findings in `artifacts/data_exploration.md`.
5. Ensure the notebook + markdown summary together provide all remaining FRDR README inputs listed above.

## Sequencing

Do step 3 before step 4.

Reason: the research artifact defines terminology, instrument context, and expected processing stages, which are needed to interpret the raw files correctly and to write accurate file descriptions in step 4.

## Exit criteria

The plan is complete when:

- `research.md` contains enough context to draft the README's general, sharing/access, and methodological sections except for file-derived facts.
- `data_exploration.md` plus the notebook contain enough verified file-derived facts to draft the README's data/file overview and data-specific sections.
- any remaining README gaps are explicit and narrow, not hidden.
