# Dataset Flow Plan

## Purpose

This plan replaces the earlier high-level initialization flow with the next concrete execution steps for the Rogers Pass dataset and the repo workflow around it.

## Status snapshot (2026-03-24)

This plan is now partly implemented and partly superseded by work in the repo.

### Implemented from this plan

- `datasets/rogers_pass_snow_profiles/README.txt`
- `datasets/rogers_pass_snow_profiles/artifacts/qc_report.md`
- `datasets/rogers_pass_snow_profiles/metadata.yaml`
- `notebooks/rogers_pass_snow_profiles_data_preparation.ipynb`
- `scripts/prepare_rogers_pass_dataset.py`
- Repo docs and workflow updates around scope, README drafting, QC, data preparation, and deposit assistance

### Still not implemented

- `datasets/rogers_pass_snow_profiles/artifacts/preflight.md`
- FRDR deposit execution, DOI assignment, and FRDR URL capture
- Final researcher decisions on still-open scope questions in the QC report

### Notes

- This file is now best read as historical planning plus remaining follow-up items, not as the current source of truth for dataset status.

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
- `datasets/rogers_pass_snow_profiles/README.txt`
- `datasets/rogers_pass_snow_profiles/artifacts/qc_report.md`
- `datasets/rogers_pass_snow_profiles/metadata.yaml`
- `notebooks/rogers_pass_snow_profiles_data_preparation.ipynb`
- `scripts/prepare_rogers_pass_dataset.py`

### Completed workflow refinements

- `plans/step3_research.md` now maps research and exploration outputs to the FRDR README template
- `AGENTS.md` now requires README-ready research capture, subtype-based exploration, and stronger QC expectations

### Still missing for this dataset

- `datasets/rogers_pass_snow_profiles/artifacts/preflight.md`
- FRDR deposit execution and publication metadata (`doi`, `doi_url`, `frdr_url`)
- researcher confirmation on still-open QC decisions such as hazard-assessment PDFs and HEIC field notebook photos
- funding metadata, which remains unset in `metadata.yaml`

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

**Status (2026-03-24):** Implemented.

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

**Status (2026-03-24):** Implemented, with some scope decisions still open for researcher review.

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

**Status (2026-03-24):** Partly implemented. `metadata.yaml` now exists and includes title, authors, contact, license, dates, geography, contributors, and workflow state. Funding, publication identifiers, and some deposit-scope decisions still need researcher confirmation.

### Questions to resolve

- funding source and grant wording
- whether hazard assessment PDFs should be included
- whether HEIC field notebook photos should be included
- whether the Day 6 Fidelity stratigraphy workbook is correctly interpreted as a revisit
- final publication identifiers after FRDR deposit (`doi`, `doi_url`, `frdr_url`)

### Output

- update `README.txt`
- optionally update dataset `metadata.yaml` if a richer local metadata record is needed

## Step 8 — Repo workflow cleanup

### Goal

Bring repo-level planning and docs into line with what now works in practice.

**Status (2026-03-24):** Mostly implemented. `AGENTS.md`, `README.md`, the step files, and dataset metadata now reflect the updated workflow. The main remaining repo-level work is preflight execution and any cleanup after the actual deposit.

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

- the Rogers Pass dataset has a usable `README.txt` and a reviewed `qc_report.md`
- preflight validation has been run and captured in `artifacts/preflight.md`
- deposit scope decisions are finalized by the researcher
- remaining metadata gaps are limited to publication identifiers assigned during deposit
- the dataset has been deposited and `metadata.yaml` has been updated with the final DOI and FRDR URL
