# AGENTS.md

Agents assist GRIMP researchers in archiving and documenting research datasets for deposit on FRDR. They generate metadata artifacts, inspect data files, and retrieve relevant information from literature, web sources, and helper modules.

## Project organization

* **`datasets/{id}/`** — First class. Each directory is one dataset to be uploaded to FRDR. Contains:
  - `README.txt` — public-facing dataset description (review surface #1)
  - `DATA_PREPARATION.md` — deposit package scope, file inventory, and transformation record (review surface #2)
  - `METADATA.yaml` — dataset metadata and workflow state
  - `raw_data/` — original unmodified data files
  - `frdr_data/` — deposit-ready files
  - `notebooks/` — Jupyter notebooks for this dataset
  - `scripts/` — dataset-specific helper scripts (optional)
  - `artifacts/` — agent workpaper; not reviewed by researcher

  **All dataset-specific code lives inside `datasets/{id}/`.** Never place a dataset's
  notebooks or scripts in the repository-level `notebooks/` or `scripts/` directories —
  the latter is reserved for project-wide tooling that is not tied to any single dataset.

  `datasets/example/` is a reference template based on the published Glacier National Park (Rogers Pass area) CAAML snow profile dataset (DOI: 10.20383/103.01523). It is a different FRDR record from `datasets/rogers_pass_snow_profiles/` (DOI: 10.20383/103.01634).

  `METADATA.yaml` mirrors FRDR required and recommended fields (title, authors, license, dates, geographic coverage, funding, related identifiers, etc.) plus workflow state. It is populated incrementally: Scope fills identity and extents, Research fills people and context, later steps update as needed. The Deposit step reads it to fill the FRDR submission form. See `datasets/example/METADATA.yaml` for the full schema.

```
datasets/{id}/
├── README.txt                        ← Review surface #1
├── DATA_PREPARATION.md               ← Review surface #2
├── METADATA.yaml
├── raw_data/
├── frdr_data/
├── notebooks/
│   ├── data_exploration.ipynb
│   └── data_preparation.ipynb
├── scripts/                          ← Dataset-specific helpers (optional)
└── artifacts/                        ← Agent workpaper — not reviewed by researcher
    ├── research.md
    ├── data_exploration.md
    ├── qc_report.md
    └── preflight.md
```

* **`docs/`** — Project-level documentation: `project_context.md` (GRIMP/MOACC/FRDR context), `FRDR-template_README.txt` (README template), `FRDR-template_DATA_PREPARATION.md` (hardened report template), `controlled_vocabulary.md` (keywords).

* **`papers/`** — Domain literature (PDFs) relevant to GRIMP research.

* **`utils/`** — Python helper modules (e.g. `frdr_metadata.py` for fetching metadata from published FRDR datasets).

* **`scripts/`** — Project-wide utility scripts only. `jupyter_mcp.py` starts JupyterLab with the token expected by the MCP server. Dataset-specific scripts belong in `datasets/{id}/scripts/`.

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
| 4 | Quality Control | 2 | [`steps/4_quality_control.md`](steps/4_quality_control.md) | `artifacts/qc_report.md`, `DATA_PREPARATION.md` (projected plan) |
| 5 | Data Preparation | 2 | [`steps/5_data_preparation.md`](steps/5_data_preparation.md) | `frdr_data/`, `DATA_PREPARATION.md`, notebook |
| 6 | Documentation Preparation | 2 | [`steps/6_documentation_preparation.md`](steps/6_documentation_preparation.md) | `README.txt` (complete), `METADATA.yaml` (final), `artifacts/preflight.md` (first run) |
| 7 | Review | 2 | [`steps/7_review.md`](steps/7_review.md) | Resolved `README.txt` and `DATA_PREPARATION.md`, final preflight PASS |
| 8 | Deposit | 1 | [`steps/8_deposit.md`](steps/8_deposit.md) | Published dataset with DOI |

When adding a new period (e.g. a new field season) to a dataset already published on FRDR, also follow [`steps/extension.md`](steps/extension.md): it adds a Baseline step (Step 0) and lists what changes in each step above.

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

## Extending a published dataset

When the user wants to add new data (typically a new field season) to a dataset already published on FRDR, this is an extension, not a new dataset. The result is a new FRDR version of the same record, with a new DOI. Work in the existing `datasets/{id}/` folder and follow [`steps/extension.md`](steps/extension.md).

The first response should briefly explain that the agent will first download the published version as a read-only baseline, then run Steps 1–8 on the new period only, keeping previously published files unchanged. Ask for:

- the DOI of the latest published version (or find it in `METADATA.yaml` and confirm it),
- the period name (e.g. `2025-2026`) and where its raw files are located,
- what changed since the last version (new sites, instruments, people, protocol).

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

## DATA_PREPARATION.md is a living document

`DATA_PREPARATION.md` is shared by the agent, the people developing the workflow, and the dataset reviewers. It is updated at several steps, not written once:

| Step | Update | Period status |
|------|--------|---------------|
| 4 Quality Control | Create the period section as a **projected** plan for Step 5: scope, planned transformations, projected tree and counts, 🚩 decisions | Projected |
| 5 Data Preparation | Replace the projection with what was actually done; note deviations | Prepared |
| 7 Review | Resolve 🚩 items; strip projected markers | Final |

Rules:
- One section per campaign period (field season), newest first. Earlier periods are not rewritten; a published period is marked `Published (vN, DOI)`.
- A projected section carries a visible **PROJECTED** banner and nothing in it may read as already done. The reviewer must be able to tell, at a glance, what is planned and what is real.
- The layout and banner text come from `docs/FRDR-template_DATA_PREPARATION.md`.
- A review PR must contain `DATA_PREPARATION.md` in its diff. If it does not, draft it first.

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

### PR description — review round

Used as the PR description whenever a PR asks the researcher to review (Step 4 for the projected plan, Step 7 for the final documents). The reviewer does this work only occasionally: write for someone who has never opened a PR, keep sections short, and fill every placeholder.

**Review files and questions must match the current step.** Use the table below to decide which files the reviewer must act on and what they confirm at this step. Ask only questions the reviewer can answer now: never ask them to complete or confirm content that belongs to a later step (for example authors and participants, which are confirmed at Step 6). If a fact is needed later, say so in "What comes next" instead of asking it now. Before opening the PR, check every question against this table.

| File | Step 4 review (projected plan) | Step 7 review (final documents) | Confirmed at |
|------|------------------|------------------|--------------|
| `DATA_PREPARATION.md` | **Critical.** Status Projected. Reviewer answers deposit-scope and QC questions | **Critical.** Status Prepared, then Final | Step 4 (scope and QC decisions), Step 7 (final) |
| `README.txt` | Not under review. Status Draft | **Critical.** Status Final | Step 7 (content and people prepared at Step 6) |
| `METADATA.yaml` | Not under review. Status Draft | **Critical.** Status Final | Step 7 (authors and fields prepared at Step 6) |
| `artifacts/`, notebooks | Optional evidence | Optional evidence | not reviewed |

```
## Dataset review — [dataset title] ([period / version])

### 1. Where we stand

Curation pipeline (✅ done, 👉 this review, ⬜ upcoming):

✅ 1 Scope · ✅ 2 Research · ✅ 3 Explore data · ✅ 4 Quality control · 👉 **Review of the projected data preparation** · ⬜ 5 Data preparation · ⬜ 6 Documentation · ⬜ 7 Final review · ⬜ 8 Deposit

[Two or three sentences: what has been done so far, and the status of each review file (e.g. "DATA_PREPARATION.md is *projected*: it describes what we plan to do, no deposit files have been prepared yet").]

### 2. What comes next

[What the agent operator does once your answers are in (the next step, in plain words), what the following review round will contain, and what remains before deposit.]

### 3. Review these files (in this order)

[Fill from the step table above. Only list as Critical the files the reviewer must act on at this step. For every file give its status and the step at which it is confirmed.]

| Priority | File | What to check now | Status | Confirmed at |
|---|---|---|---|---|
| Critical | `datasets/{id}/DATA_PREPARATION.md`, section [period] | [Step 4: proposed deposit scope, planned transformations, 🚩 decisions] | [Projected / Prepared / Final] | [Step 4 / Step 7] |
| Not yet | `datasets/{id}/README.txt` | Nothing at this step [or, at Step 7: public description, people, sites, instruments, methods] | [Draft / Final] | [Step 7] |
| Not yet | `datasets/{id}/METADATA.yaml` | Nothing at this step [or, at Step 7: authors, dates, coverage, keywords] | [Draft / Final] | [Step 7] |
| Optional | `datasets/{id}/artifacts/`, notebooks | Agent workpapers, only if you want the evidence behind a question | n/a | n/a |

Everything else in the diff (code, utilities, instructions) is tooling: you can skip it.

### 4. Open questions for you

Numbered, answerable in one line each. Name the file and section, and say what we will do for each answer. Every question must be answerable at the current step (see the step table above).

1. **[Topic]** — [question]. (`file`, section) If A: [consequence]. If B: [consequence].

### 5. How to review

- Open the **Files changed** tab and use the file list on the left to jump to the critical files above.
- Click the **+** next to a line to comment on it, or answer in the PR conversation by question number. Short answers are fine ("1: B").
- 🚩 marks items needing your decision. ⚠️ marks context to read, no action required.
- You do not need to approve code or understand the notebooks.
```
