# AGENTS.md

Agents assist GRIMP researchers in archiving and documenting research datasets for deposit on FRDR. They generate metadata artifacts, inspect data files, and retrieve relevant information from literature, web sources, and helper modules.

## Project organization

* **`datasets/{id}/`** — First class. Each directory is one dataset to be uploaded to FRDR. Contains:
  - `README.txt` — public-facing dataset description (review surface #1)
  - `DATA_PREPARATION.md` — deposit package scope, file inventory, and transformation record (review surface #2)
  - `METADATA.yaml` — dataset metadata and workflow state
  - `raw_data/` — original unmodified data files
  - `frdr_data/` — deposit-ready files
  - `notebooks/` — Jupyter notebooks
  - `artifacts/` — agent workpaper; not reviewed by researcher

  `datasets/example/` is a reference template based on the published Rogers Pass snow profile dataset (DOI: 10.20383/103.01523).

  `METADATA.yaml` mirrors FRDR required and recommended fields (title, authors, license, dates, geographic coverage, funding, related identifiers, etc.) plus workflow state. It is populated incrementally: Scope fills identity and extents, Research fills people and context, later steps update as needed. The Deposit step reads it to fill the FRDR submission form. See `datasets/example/METADATA.yaml` for the full schema.

```
datasets/{id}/
├── README.txt                        ← Review surface #1
├── DATA_PREPARATION.md               ← Review surface #2
├── METADATA.yaml
├── raw_data/
├── frdr_data/
├── notebooks/
│   └── data_preparation.ipynb
└── artifacts/                        ← Agent workpaper — not reviewed by researcher
    ├── research.md
    ├── data_exploration.md
    ├── qc_report.md
    └── preflight.md
```

* **`docs/`** — Project-level documentation: `project_context.md` (GRIMP/MOACC/FRDR context), `FRDR-template_README.txt` (README template), `FRDR-template_DATA_PREPARATION.md` (hardened report template), `controlled_vocabulary.md` (keywords).

* **`papers/`** — Domain literature (PDFs) relevant to GRIMP research.

* **`utils/`** — Python helper modules (e.g. `frdr_metadata.py` for fetching metadata from published FRDR datasets).

* **`scripts/`** — Utility scripts. `jupyter_mcp.py` starts JupyterLab with the token expected by the MCP server.

* **`steps/`** — Detailed instructions for each workflow step. The agent reads the relevant step file when executing that step.

## Emoji convention

Applies to `README.txt` and `DATA_PREPARATION.md` only.

| Marker | Meaning | Who acts |
|--------|---------|---------|
| 🚩 | Required decision — researcher must choose | Researcher |
| ⚠️ | Critical context — researcher must understand | Read only |

Not used in `artifacts/qc_report.md`, `artifacts/research.md`, `artifacts/data_exploration.md`, or `artifacts/preflight.md`.

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
| 1 | Scope Definition | 2 | [`steps/1_scope_definition.md`](steps/1_scope_definition.md) | `README.txt` (identity sections), `METADATA.yaml` |
| 2 | Research | 3 | [`steps/2_research.md`](steps/2_research.md) | `artifacts/research.md` |
| 3 | Explore Data | 3 | [`steps/3_explore_data.md`](steps/3_explore_data.md) | `artifacts/data_exploration.md`, notebook |
| 4 | Quality Control | 2 | [`steps/4_quality_control.md`](steps/4_quality_control.md) | `artifacts/qc_report.md` |
| 5 | Data Preparation | 2 | [`steps/5_data_preparation.md`](steps/5_data_preparation.md) | `frdr_data/`, `DATA_PREPARATION.md`, notebook |
| 6 | Documentation Preparation | 2 | [`steps/6_documentation_preparation.md`](steps/6_documentation_preparation.md) | `README.txt` (complete), `METADATA.yaml` (final), `artifacts/preflight.md` (first run) |
| 7 | Review | 2 | [`steps/7_review.md`](steps/7_review.md) | Resolved `README.txt` and `DATA_PREPARATION.md`, final preflight PASS |
| 8 | Deposit | 1 | [`steps/8_deposit.md`](steps/8_deposit.md) | Published dataset with DOI |

## New dataset intake

When the user says they want to archive a new dataset, guide them quickly toward Scope Definition. Do not assume they already know this repository structure or the FRDR workflow, but do not linger in explanation either: give just enough orientation to help them provide the dataset or the missing scope facts.

The first response should:

1. Briefly explain the path in plain language: first define the scope, then inspect/research the data, prepare deposit-ready files, draft the FRDR documentation, and run review/preflight before deposit.
2. Say that the immediate next milestone is **Scope Definition**, where the agent creates the dataset folder and drafts the initial `METADATA.yaml` plus the identity/scope sections of `README.txt`.
3. Explain quickly what the main files are for:
   - `METADATA.yaml` gathers the structured fields needed for the FRDR dataset submission form.
   - `README.txt` becomes the public-facing dataset description that users will see with the deposit.
   - `DATA_PREPARATION.md` records what files are included, excluded, renamed, converted, or otherwise prepared for deposit.
4. Name the two researcher-facing review documents early: `README.txt` and `DATA_PREPARATION.md`. Explain that notebooks and `artifacts/` are internal workpapers unless the user wants to inspect them.
5. Elicit the quickest path to Scope Definition by asking for either a dataset location or the missing facts:
   - a short dataset name or identifier,
   - where the raw files are located,
   - what the dataset is about,
   - any known people, dates, location, or related publication/DOI.
6. If the user provides a raw data path, DOI, existing folder, or enough context to infer a dataset ID, proceed into `steps/1_scope_definition.md` instead of asking for every field upfront. Missing details can be marked as draft/unknown and resolved during review.
7. Keep the tone practical and companionable. Avoid a terse checklist-only answer when the user is starting a workflow.

Do not create or move files until the user provides enough information to identify the dataset and raw data location.

## Step dependencies

Research and Explore Data are independent and should run in parallel when possible. All other dependencies are sequential.

```
Scope Definition
    ├── Research ──────────┐
    └── Explore Data ──────┤
                           ├── Quality Control
                           │       └── Data Preparation
                           │               └── Documentation Preparation
                           │                       └── Review
                           │                               └── Deposit
```

## Scope-update protocol

When Research or Explore Data discovers information that contradicts or extends the current scope (e.g., broader date range, additional file types, out-of-scope records), the agent updates the relevant `README.txt` section directly and notes the change in the step's artifact (`research.md` or `data_exploration.md`). There is no separate scope document. The README is the living scope document throughout the workflow.

**README.txt is not sent to the researcher until Step 6.** Before Step 6 it is a draft — no review preamble, no 🚩 markers.

## Documentation-coverage reconciliation

Because Research draws from literature and Explore Data draws from files, neither artifact alone guarantees full coverage. Before Quality Control begins data-quality checks, it must reconcile the two artifacts:

1. Every instrument or file type in `data_exploration.md` must have a methodology entry and citable reference in `research.md`.
2. Every instrument in `research.md` must have corresponding files in `data_exploration.md` (catches phantom instruments).
3. Every variable found in file headers must have a definition or unit in one of the two artifacts.

When a gap is found, QC sends a targeted research request back to the Research step (covering only the missing instruments or variables) before proceeding. This is a lightweight patch, not a full re-run of Research.

## Templates

### README.txt review preamble

Added by Documentation Preparation (Step 6) at the very top of `README.txt`, stripped at final preflight before deposit.

```
⚠️ REVIEW INSTRUCTIONS — REMOVE BEFORE DEPOSIT
This document is under review for FRDR deposit.
🚩 marks items requiring your decision.
⚠️ marks critical context you must understand.
Your companion review document is DATA_PREPARATION.md.
Notebooks and artifacts/ are reference material — you do not need to review them.
----------------------------------------------------------------
```

### PR description — revision instructions

Used as the PR description when opening a review round in Step 7.

```
## Dataset review — [dataset title]

Please review the two documents below and leave comments on any 🚩 items.

**Your review documents:**
- `README.txt` — public-facing dataset description for FRDR deposit
- `DATA_PREPARATION.md` — deposit package scope, file inventory, and transformation record

**How to review:**
- 🚩 marks items requiring your decision — please comment directly on these lines
- ⚠️ marks critical context for your understanding — no action required
- Notebooks and `artifacts/` are reference material — you do not need to review them

**What happens next:**
After your comments, the agent operator will apply fixes, run a preflight check, and either
send another round or proceed to deposit.
```
