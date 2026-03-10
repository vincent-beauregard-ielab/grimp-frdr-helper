# Dataset Flow Plan

## Purpose

This plan replaces the earlier high-level initialization flow with the next concrete execution steps for the Rogers Pass dataset and the repo workflow around it.

It assumes the following are now complete:

- project scaffolding and basic repo setup
- `AGENTS.md` and `README.md` refinement
- step 3 research artifact
- step 4 data exploration notebook and summary

The next work should focus on converting those inputs into a usable FRDR package, validating it, and feeding the lessons back into the repo workflow.

## Current state

### Completed dataset outputs

- `datasets/rogers_pass_snow_profiles/artifacts/research.md`
- `datasets/rogers_pass_snow_profiles/artifacts/data_exploration.md`
- `notebooks/rogers_pass_snow_profiles_data_exploration.ipynb`

### Completed workflow refinements

- `plans/step3_research.md` now maps research and exploration outputs to the FRDR README template
- `AGENTS.md` now requires README-ready research capture, subtype-based exploration, and stronger QC expectations

### Still missing for this dataset

- `datasets/rogers_pass_snow_profiles/README.txt`
- `datasets/rogers_pass_snow_profiles/artifacts/qc_report.md`
- a deposit decision on which files are scientific, ancillary, or excluded
- owner-confirmed metadata fields such as title, authors, contact, license, and funding

## Key learnings from the session

### Planning

- The FRDR README template is the real contract. Research and exploration steps should be designed backward from that template.
- A description-only research step is insufficient. It must also capture README inputs and unresolved fields.
- Data exploration should produce both a notebook and a markdown summary artifact.

### Data structure

- The dataset is organized by field day, not by instrument.
- Extension alone is not a good enough classification. The package contains multiple subtypes within `.csv`, `.txt`, and `.xlsx`.
- Mapping files that link radar, SMP, SnowScope, and GPS records are essential and should be treated as first-class scientific support files.

### Tooling

- `uv run` may depend on a project `.env`; the workflow should assume `.env` is created from `.env.example` early.
- `snowmicropyn` is required for `.pnt` parsing and should remain declared in `pyproject.toml`.
- Jupyter notebook execution is useful as the final verification step for data-exploration logic.

### Documentation and QC

- The raw package contains scientific data mixed with support/admin material.
- Naming inconsistencies and format quirks are not edge cases; they are part of the real dataset and must be documented.
- The QC step should explicitly distinguish:
  - fixable issues in prepared outputs
  - raw-source issues that should only be recorded

## Next steps in the flow

## Step 5 — Draft FRDR README

### Goal

Write `datasets/rogers_pass_snow_profiles/README.txt` from `docs/FRDR-template_README.txt` using the completed research and exploration outputs.

### Inputs

- `datasets/rogers_pass_snow_profiles/artifacts/research.md`
- `datasets/rogers_pass_snow_profiles/artifacts/data_exploration.md`
- `notebooks/rogers_pass_snow_profiles_data_exploration.ipynb`
- `datasets/example/README.txt`
- `docs/FRDR-template_README.txt`

### Tasks

1. Build a README field checklist from the FRDR template.
2. Fill all sections that are already supported by verified evidence.
3. Mark unresolved fields explicitly instead of guessing.
4. Separate:
   - deposited scientific data
   - ancillary scientific support files
   - excluded admin/logistics material
5. Add file-relationship explanations for:
   - snowpit workbooks
   - instrument exports
   - GNSS / mapping files
   - shapefile ZIPs
6. Add software requirements and standards:
   - `snowmicropyn`
   - spreadsheet readers
   - OGRS
   - CAAML context where relevant

### Deliverable

- `datasets/rogers_pass_snow_profiles/README.txt`

### Exit criteria

- Every section in `docs/FRDR-template_README.txt` is either filled or explicitly marked as pending owner confirmation.

## Step 6 — Quality control and packaging decisions

### Goal

Write `datasets/rogers_pass_snow_profiles/artifacts/qc_report.md` and define the proposed deposit scope.

### Tasks

1. Review the raw package against the README draft.
2. Classify each major folder/file class as:
   - include in deposit
   - include as ancillary/support
   - exclude from deposit
3. Record dataset issues found during exploration, including:
   - `Round Hill` vs `RoundHill`
   - `Christiana` vs `Christiania`
   - mixed `.txt` / `.TXT`
   - mixed `.HEIC` / `.heic`
   - likely date typo `202500306`
   - placeholder zeros in template-derived workbooks
   - truncated SMP file(s)
   - missing or invalid coordinates in `.pnt`
   - repeated radar data blocks within each text export
4. Decide which issues should be corrected in prepared deliverables and which should only be documented as raw-source conditions.
5. Verify the README statements against actual files.

### Deliverable

- `datasets/rogers_pass_snow_profiles/artifacts/qc_report.md`

### Exit criteria

- The report clearly states deposit scope, known issues, and whether any file renaming or normalization is required before FRDR submission.

## Step 7 — Metadata completion with owner input

### Goal

Resolve the metadata fields that cannot be inferred safely from local files.

### Questions to resolve

- final dataset title
- author list and order
- principal investigator and contact email
- license
- funding source and grant wording
- whether Parks Canada is co-author, contributor, or contextual partner
- whether field notes, HEIC photos, and shapefile ZIPs are included
- whether the package remains raw-format or is normalized before deposit

### Output

- update `README.txt`
- optionally update dataset `metadata.yaml` if a richer local metadata record is needed

## Step 8 — Repo workflow cleanup

### Goal

Bring repo-level planning and docs into line with what now works in practice.

### Tasks

1. Keep `initialize.md` as project history, but treat this file as the current execution plan.
2. Update `README.md` if needed so it references:
   - `artifacts/data_exploration.md`
   - the `.env` requirement before `uv run`
   - the stronger README-first flow
3. Consider adding lightweight helper scripts later for:
   - inventory summaries
   - SnowScope parsing
   - radar export parsing
   - QC checks

## Recommended execution order

1. Draft `datasets/rogers_pass_snow_profiles/README.txt`
2. Write `datasets/rogers_pass_snow_profiles/artifacts/qc_report.md`
3. Resolve owner-confirmation metadata gaps
4. Revise README and deposit scope
5. Update repo docs only if the workflow changed again during steps 5–6

## Success criteria

This plan is complete when:

- the Rogers Pass dataset has a usable `README.txt`
- the dataset has a clear `qc_report.md`
- deposit scope is explicit
- unresolved metadata fields are narrow and owner-facing
- the repo workflow reflects the actual sequence:
  `research -> data exploration -> README draft -> QC -> metadata completion -> deposit`
