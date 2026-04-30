# Plan: Refactor Researcher Collaboration Workflow

**Date:** 2026-04-30
**Status:** Approved for implementation

## Objective

Harden and simplify the researcher review process. Two documents, one review surface. The researcher touches exactly two files: `README.txt` and `data_preparation_report.md`, both at `datasets/{id}/`. Everything else is agent workpaper.

---

## Emoji convention

Applies to `README.txt` and `data_preparation_report.md` only.

| Marker | Meaning | Who acts |
|--------|---------|---------|
| 🚩 | Required decision — researcher must choose | Researcher |
| ⚠️ | Critical context — researcher must understand | Read only |

Not used in `qc_report.md`, `research.md`, `data_exploration.md`, or `preflight.md`.

---

## Step sequence

| # | Step | Autonomy | Key outputs |
|---|------|----------|-------------|
| 1 | **Scope Definition** | 2 | `README.txt` (identity sections only, stub placeholders for the rest), `metadata.yaml` |
| 2 | **Research** | 3 | `artifacts/research.md` — fills README methods + attribution stubs |
| 3 | **Explore Data** | 3 | `artifacts/data_exploration.md` — fills README file overview stubs, notebook |
| 4 | **Quality Control** | 2 | `artifacts/qc_report.md` (frozen after this step), README updated |
| 5 | **Data Preparation** | 2 | `frdr_data/`, `data_preparation_report.md`, `notebooks/data_preparation.ipynb` |
| 6 | **Documentation Preparation** | 2 | README completed, `metadata.yaml` finalized, `artifacts/preflight.md` (first run) |
| 7 | **Review** | 2 | Resolved `README.txt` and `data_preparation_report.md`, final `artifacts/preflight.md` PASS |
| 8 | **Deposit** | 1 | Published dataset with DOI |

Steps 2 and 3 are parallel. Step 4b (Scope Revision) is eliminated — scope decisions are confirmed in `data_preparation_report.md`'s proposed scope table. Preflight lives inside Step 7. Former Step 7 (Preflight Validation) is eliminated as a standalone step.

---

## Step 1 — Scope Definition

Step 1 is still called **Scope Definition**. The scope document is no longer `artifacts/scope.md` — it is `README.txt` itself.

**Initialization creates:**
- `datasets/{id}/` directory structure
- `datasets/{id}/metadata.yaml` with identity fields
- `datasets/{id}/README.txt` — identity sections filled (title, authors, dates, location, funding); all structural sections (file overview, methods, variable lists) left as `⚠️ [placeholder — to be filled at Step 6]`

**Scope-update protocol:**
When Research (Step 2) or Explore Data (Step 3) discovers information that conflicts with or extends the current scope (broader date range, additional file types, out-of-scope records), the agent updates the relevant README.txt section directly and notes the change. There is no separate scope.md. The README is the living scope document throughout the workflow.

**README.txt is not sent to the researcher until Step 6.** Before Step 6 it is a draft — no review preamble, no 🚩 markers.

---

## Document responsibility matrix

| Document | Location | Who generates | Researcher reviews? | Frozen when? |
|---|---|---|---|---|
| `README.txt` | `datasets/{id}/` | Agent (Step 1 init; Step 6 complete) | **Yes — primary** | After final preflight PASS |
| `data_preparation_report.md` | `datasets/{id}/` | Agent (Step 5) | **Yes — primary** | After final preflight PASS |
| `metadata.yaml` | `datasets/{id}/` | Agent (Step 1 init; Step 6 finalize) | No | After final preflight PASS |
| `artifacts/qc_report.md` | `artifacts/` | Agent (Step 4) | No — reference only | After Step 4 — never edited again |
| `artifacts/research.md` | `artifacts/` | Agent (Step 2) | No | After Step 2 |
| `artifacts/data_exploration.md` | `artifacts/` | Agent (Step 3) | No | After Step 3 |
| `artifacts/preflight.md` | `artifacts/` | Agent (Steps 6–7) | No — operator only | After deposit |
| `notebooks/data_preparation.ipynb` | `notebooks/` | Agent (Step 5) | Optional | — |

---

## Dataset folder layout

```
datasets/{id}/
├── README.txt                        ← Review surface #1
├── data_preparation_report.md        ← Review surface #2
├── metadata.yaml
├── raw_data/
├── frdr_data/
├── notebooks/
│   └── data_preparation.ipynb
└── artifacts/                        ← Agent workpaper — not reviewed
    ├── research.md
    ├── data_exploration.md
    ├── qc_report.md
    └── preflight.md
```

---

## README.txt lifecycle

| Stage | State |
|---|---|
| Step 1 | Identity sections filled; structural sections are `⚠️ [placeholder]`; no review preamble; no 🚩 |
| Steps 2–4 | Agent fills stubs as information becomes available; no researcher involvement |
| Step 6 | All sections completed; `metadata.yaml` finalized; ⚠️ review preamble added (see template in AGENTS.md); 🚩 on any items needing researcher decision |
| Review loop | 🚩 items resolved one by one |
| Final preflight | Preamble stripped, no remaining 🚩 → deposit-ready |

**Review preamble** (added at Step 6, stripped at final preflight):

```
⚠️ REVIEW INSTRUCTIONS — REMOVE BEFORE DEPOSIT
This document is under review for FRDR deposit.
🚩 marks items requiring your decision.
⚠️ marks critical context you must understand.
Your companion review document is data_preparation_report.md.
Notebooks and artifacts/ are reference material — you do not need to review them.
----------------------------------------------------------------
```

---

## data_preparation_report.md lifecycle

- Generated at Step 5 from the hardened template (`docs/FRDR-template_data_preparation_report.md`)
- Opens with the ⚠️ review instructions block (legend, companion README reference, what to ignore)
- Contains: proposed deposit scope table (🚩 on any contested items), full `frdr_data/` file tree, change summary, transformation log, excluded files, unresolved issues
- Review loop: 🚩 items resolved; scope decisions confirmed
- Not stripped — archived as deposit record

---

## qc_report.md behavior

- Generated once at Step 4 as an exhaustive forensic log — free-form, no template
- Describes every issue found with file/row/column specificity
- **Never edited after Step 4.** Resolution tracking belongs entirely to `data_preparation_report.md`
- Researcher may consult it as reference but does not act on it directly

---

## preflight.md behavior

- First run at Step 6 after README is completed
- Each subsequent run in the review loop appends a timestamped section with what changed
- Checks include: README completeness, no leftover template markers, all 🚩 resolved, `frdr_data/` file counts match report, `metadata.yaml` fields complete, ⚠️ review preamble present (pre-final) or absent (final)
- Final PASS is the gate before Deposit

---

## Step 7 — Review

Researcher reviews the two collaboration documents. The agent operator drives the revision loop and runs preflight after each fix round. The step ends when all 🚩 items are resolved and preflight returns PASS.

```
Step 6 complete (README + first preflight)
    │
    ▼
Operator opens PR (optional) or sends documents directly
    │   PR includes: README.txt + data_preparation_report.md
    │   PR description uses the revision instructions boilerplate (see below)
    ▼
Researcher comments on 🚩 items (inline PR comments or direct feedback)
    │
    ▼
Agent operator + agent apply fixes
    │
    ├── Fix touches frdr_data/ ──► Re-run Step 5 (Data Preparation), then Step 6 (Documentation Preparation)
    └── Fix touches README, metadata.yaml, or report only ──► Apply directly
    │
    ▼
Operator runs preflight → preflight.md updated with timestamped run
    │
    ├── All 🚩 resolved + PASS ──► Proceed to Step 8 (Deposit)
    └── Unresolved items ──────► Another review round (return to researcher)
```

**Modifications during Step 7 are confined to:** `README.txt`, `metadata.yaml`, `data_preparation_report.md`, and `notebooks/`. Fixes that require changes to `frdr_data/` loop back through Steps 5–6 before returning to Step 7.

### PR boilerplate — revision instructions

Used as the PR description when opening a review round. Stored as a template in AGENTS.md.

```
## Dataset review — [dataset title]

Please review the two documents below and leave comments on any 🚩 items.

**Your review documents:**
- `README.txt` — public-facing dataset description for FRDR deposit
- `data_preparation_report.md` — deposit package scope, file inventory, and transformation record

**How to review:**
- 🚩 marks items requiring your decision — please comment directly on these lines
- ⚠️ marks critical context for your understanding — no action required
- Notebooks and `artifacts/` are reference material — you do not need to review them

**What happens next:**
After your comments, the agent operator will apply fixes, run a preflight check, and either
send another round or proceed to deposit.
```

---

## Notebook synthesis section

`data_preparation.ipynb` ends with a `## Synthesis for Report` section containing:
- Markdown cells explaining key decisions and unresolved issues
- Code cells printing structured summaries: file counts per category, transform counts, any items flagged for researcher decision

The agent reads this section before writing `data_preparation_report.md`. No intermediate file. The notebook is the source; the report is the formatted output.

---

## docs/ additions

```
docs/
├── FRDR-template_README.txt                          ← existing
├── FRDR-template_data_preparation_report.md          ← NEW (hardened template)
├── controlled_vocabulary.md
└── project_context.md
```

---

## What is eliminated

| Eliminated | Replaced by |
|---|---|
| `artifacts/scope.md` | `README.txt` (initialized at Step 1) |
| `steps/4b_scope_revision.md` | 🚩 scope table in `data_preparation_report.md` |
| `steps/7_preflight_validation.md` | Preflight moves inside new `steps/7_review.md` |
| 🔔 emoji | 🚩 and ⚠️ |

---

## Implementation order

1. `AGENTS.md` — update overall structure: file layout, step table, emoji convention, scope-update protocol pointing to README, review loop removed as phase (now Step 7)
2. `steps/1_scope_definition.md` — README.txt initialization, no scope.md output
3. `steps/2_research.md` — update outputs to reference README stub-filling
4. `steps/3_explore_data.md` — update outputs to reference README stub-filling
5. `steps/4_quality_control.md` — remove 4b reference, clarify qc_report is frozen after this step
6. `steps/5_data_preparation.md` — move report to `datasets/{id}/`, add filetree requirement, notebook synthesis section, template reference
7. `steps/6_draft_readme.md` — rename to Documentation Preparation; scope covers README.txt completion + metadata.yaml finalization + first preflight run; add review preamble insertion
8. `steps/7_review.md` — new step; revision loop, preflight-on-loop, frdr_data/ re-run gate, modification constraints
9. Delete `steps/4b_scope_revision.md` and `steps/7_preflight_validation.md`; renumber `steps/8_deposit.md` to `steps/8_deposit.md` (unchanged)
10. `docs/FRDR-template_data_preparation_report.md` — new hardened template
11. Update `datasets/example/` to reflect new layout (no scope.md, data_preparation_report.md at top level)
