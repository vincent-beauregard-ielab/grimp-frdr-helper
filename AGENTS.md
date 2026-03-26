# AGENTS.md

Agents assist GRIMP researchers in archiving and documenting research datasets for deposit on FRDR. They generate metadata artifacts, inspect data files, and retrieve relevant information from literature, web sources, and helper modules.

## Project organization

* **`datasets/{id}/`** — First class. Each directory is one dataset to be uploaded to FRDR. Contains data files, the FRDR README, `metadata.yaml` (dataset metadata + workflow state), and `artifacts/` (research notes, extracted metadata, QC reports). `datasets/example/` is a reference template based on the published Rogers Pass snow profile dataset (DOI: 10.20383/103.01523).

  `metadata.yaml` mirrors FRDR required and recommended fields (title, authors, license, dates, geographic coverage, funding, related identifiers, etc.) plus workflow state. It is populated incrementally: Scope fills identity and extents, Research fills people and context, later steps update as needed. The Deposit step reads it to fill the FRDR submission form. See `datasets/example/metadata.yaml` for the full schema.

* **`notebooks/`** — First class. All data exploration and manipulation must be done reproducibly in Jupyter notebooks.

* **`docs/`** — Project-level documentation: `project_context.md` (GRIMP/MOACC/FRDR context), `FRDR-template_README.txt` (README template), `controlled_vocabulary.md` (keywords).

* **`papers/`** — Domain literature (PDFs) relevant to GRIMP research.

* **`utils/`** — Python helper modules (e.g. `frdr_metadata.py` for fetching metadata from published FRDR datasets).

* **`scripts/`** — Utility scripts. `jupyter_mcp.py` starts JupyterLab with the token expected by the MCP server.

* **`steps/`** — Detailed instructions for each workflow step. The agent reads the relevant step file when executing that step.

## Constraints

All documentation and results written in English.

Code is Python. Dependencies managed by `uv` in project `.venv`. Run code using `uv run`.

If local tooling expects a project `.env`, create it from `.env.example` before running `uv run`.

Before running or creating Jupyter notebooks, ensure JupyterLab is running:

```bash
uv run scripts/jupyter_mcp.py
```

## Human-in-the-loop

Default autonomy level is **Level 2** (agent proposes, human reviews). Autonomy scales inversely with reversibility.

| Level | Label | Pattern |
|-------|-------|---------|
| 1 | Agent assists | Agent drafts, human does everything |
| 2 | Agent proposes | Agent produces artifact, human reviews & approves before it is used |
| 3 | Agent executes with gates | Agent runs autonomously, pauses at checkpoints for human approval |

> **Note:** A future Level 4 (Agent autonomous — agent runs end-to-end, human spot-checks) may be introduced once the workflow is well established. Not planned for now.

Start all steps at Level 2 and selectively promote to Level 3 as the team gains confidence.

## Workflow

Each dataset follows this pipeline. Detailed instructions for each step are in `steps/`.

| # | Step | Level | Instructions | Key outputs |
|---|------|-------|-------------|-------------|
| 1 | Scope Definition | 2 | [`steps/1_scope_definition.md`](steps/1_scope_definition.md) | `metadata.yaml`, `artifacts/scope.md` |
| 2 | Research | 3 | [`steps/2_research.md`](steps/2_research.md) | `artifacts/research.md` |
| 3 | Explore Data | 3 | [`steps/3_explore_data.md`](steps/3_explore_data.md) | `artifacts/data_exploration.md`, notebook |
| 4 | Quality Control | 2 | [`steps/4_quality_control.md`](steps/4_quality_control.md) | `artifacts/qc_report.md` |
| 4b | Scope Revision | 2 | [`steps/4b_scope_revision.md`](steps/4b_scope_revision.md) | revised `artifacts/scope.md` |
| 5 | Data Preparation | 2 | [`steps/5_data_preparation.md`](steps/5_data_preparation.md) | `frdr_data/`, `artifacts/data_preparation_report.md`, notebook |
| 6 | Draft README | 2 | [`steps/6_draft_readme.md`](steps/6_draft_readme.md) | `README.txt` |
| 7 | Preflight Validation | 3 | [`steps/7_preflight_validation.md`](steps/7_preflight_validation.md) | `artifacts/preflight.md` |
| 8 | Deposit | 1 | [`steps/8_deposit.md`](steps/8_deposit.md) | Published dataset with DOI |

## Step dependencies

Research and Explore Data are independent and should run in parallel when possible. All other dependencies are sequential.

```
Scope Definition
    ├── Research ──────────┐
    └── Explore Data ──────┤
                           ├── Quality Control
                           │       └── Scope Revision (human reviews)
                           │               └── Data Preparation
                           │                       └── Draft README
                           │                               └── Preflight Validation
                           │                                       └── Deposit
```

## Scope-update protocol

When Research or Explore Data discovers information that contradicts or extends the current scope (e.g., broader date range, additional file types, out-of-scope records), the step adds a `## Scope updates` section to its own artifact describing the finding. The main agent consolidates these into `scope.md` before proceeding to Quality Control.

## Documentation-coverage reconciliation

Because Research draws from literature and Explore Data draws from files, neither artifact alone guarantees full coverage. Before Quality Control begins data-quality checks, it must reconcile the two artifacts:

1. Every instrument or file type in `data_exploration.md` must have a methodology entry and citable reference in `research.md`.
2. Every instrument in `research.md` must have corresponding files in `data_exploration.md` (catches phantom instruments).
3. Every variable found in file headers must have a definition or unit in one of the two artifacts.

When a gap is found, QC sends a targeted research request back to the Research step (covering only the missing instruments or variables) before proceeding. This is a lightweight patch, not a full re-run of Research.
