# Agent Flow Review

Is the workflow and agents well configured to accomplish our goals? Think in first principles.

What is well implemented and well captured? What is missing? What opportunity are we moving past? Are we taking full advantage of agents? Are we introducing some noise? Have we overengineered stuff?

---

## Implementation check (2026-03-24)

This review has now been partly implemented in the repo.

### Implemented

- Dataset initialization is now documented in `steps/1_scope_definition.md`.
- Deposit assistance is now documented in `steps/8_deposit.md`, including FRDR field mapping.
- Workflow dependencies now explicitly show `Research` and `Explore Data` running in parallel in `AGENTS.md`.
- The scope-update protocol is documented in `AGENTS.md` and `steps/1_scope_definition.md`.
- Preflight validation now exists as `steps/7_preflight_validation.md`.
- `metadata.yaml` is now used as a richer workflow and metadata record, including workflow state.
- `steps/2_research.md` now tells the agent to use `utils/frdr_metadata.py` when applicable.
- `steps/6_draft_readme.md` now includes explicit validation against `docs/FRDR-template_README.txt`.
- The autonomy note keeps Level 4 out of the main workflow table and treats it as future work.

### Still not implemented

- Cross-dataset and collection-level guidance is still minimal. The repo has controlled vocabulary notes, but not a clear collection-level workflow or consistency checks across datasets.
- There is still no dedicated automation for cross-dataset validation, collection metadata management, or related-identifier consistency across multiple datasets.

### Notes

- Several recommendations were implemented as workflow documentation rather than standalone code. That closes the process gap, but not every item has dedicated tooling yet.
- The sections below preserve the original review framing; use the implementation check above as the current-status summary.

## What's well implemented

**Workflow design is solid.** The pipeline (Scope → Research → Explore → QC → Data Prep → README → Preflight → Deposit) is a natural progression from "understand the dataset" to "publish it." Each step has a clear deliverable artifact with a defined path, which makes the workflow inspectable and resumable.

**Human-in-the-loop is thoughtful.** The four autonomy levels with per-step targets are well-calibrated. Research/Explore at Level 3 (low risk, inspectable output), Data Prep/README at Level 2 (modifies files or is public-facing), Deposit at Level 1 (irreversible). The "start at Level 2, promote selectively" rule is prudent for a small team.

**Data preparation is well-structured.** The raw_data → frdr_data non-destructive pattern, mandatory Jupyter notebook, and the verification report as a review gate are all excellent. The verification report's required sections (change summary, file inventory, structural changes, transformation log, excluded data, unresolved issues) give the researcher exactly what they need to approve.

**README-centric design.** Every preceding step explicitly feeds into README sections. Research targets "General information, Sharing/access, Methodological context." Explore targets "Data & file overview, Variable/codebook sections." This alignment reduces wasted work.

**Scope as a living artifact.** Explicitly stating that scope gets refined after Research and Explore prevents the common trap of treating scoping as one-and-done.

**QC as read-only with structured recommendations.** The What/Impact/Recommended action format per issue is clear and actionable. Separating "find problems" from "fix problems" is the right call for Level 2 autonomy.

---

## What's missing

### 1. No dataset initialization step

There's no documented process for bootstrapping a new dataset: creating `datasets/{id}/`, `metadata.yaml`, `raw_data/`, `artifacts/`, etc. This is the very first thing an agent or researcher does, but it's implicit. Should be a trivial step (maybe part of Scope Definition) but worth codifying so the directory structure is always consistent.

### 2. Deposit step has no task description

Every other step has detailed sub-activities, outputs, and delegation guidance. Deposit just says "Researcher drives, agent assists. Irreversible action." Even at Level 1, the agent should know what it assists *with*: preparing the FRDR metadata form fields, generating the submission checklist, validating that all required files are present, etc.

### 3. No dependency graph or parallelism guidance at the workflow level

Individual steps document internal parallelism (Research spawns 3 subagents, Explore spawns per-format subagents), but the step-to-step dependencies aren't explicit. Key insight: **Research and Explore can run in parallel** — Research gathers literature/context while Explore inspects files. Both feed into QC and README independently. This is a significant time-saving opportunity that isn't captured.

Suggested dependency graph:
```
Scope Definition
    ├── Research (parallel)
    └── Explore Data (parallel)
            ├── Quality Control (needs both)
            │       └── Data Preparation
            └── Draft README (needs Research + Explore + Data Prep)
                        └── Deposit
```

### 4. No feedback loop mechanism

Scope says "update when Research or Explore reveals new info" but there's no trigger or protocol. When does the agent decide to update scope? Does it pause and ask? Does it update and flag? This matters for Level 3 steps — if Research is running autonomously and discovers the dataset has a broader date range than scoped, what happens?

Suggestion: define a simple protocol — if a step discovers information that contradicts or extends the scope document, it adds a `## Scope updates` section to its own artifact and flags it in its output. The main agent consolidates these into scope.md before proceeding to QC.

### 5. No preflight/validation before Deposit

There should be a checklist step between README draft and Deposit that validates:
- All FRDR required metadata fields are populated
- README covers all template sections
- `frdr_data/` file list matches README file inventory
- `metadata.yaml` has required fields
- License is specified
- Geographic coordinates are present

This is cheap to implement and catches errors before the irreversible step.

### 6. No cross-dataset concerns

The workflow is per-dataset, but there are collection-level concerns:
- Controlled vocabulary consistency across datasets
- GRIMP collection metadata on FRDR (noted as "not yet created" in project_context.md)
- Cross-dataset references (Related Identifiers in the README)

These don't need a full step but deserve a note in AGENTS.md.

---

## Missed opportunities

### 1. Research and Explore should run in parallel

As noted above. These two steps are independent — Research reads papers/web/context while Explore reads data files. Running them sequentially wastes time. The delegation sections already describe *internal* parallelism but miss the *cross-step* opportunity.

### 2. `metadata.yaml` is underused

Currently holds DOI and FRDR URL. Could also track:
- Workflow state (which steps are complete)
- Dataset-level metadata that feeds into both the FRDR form and README (title, authors, license, dates)
- Links to raw_data source (e.g., OneDrive path, shared drive)

This would make datasets self-describing and enable an agent to pick up work mid-workflow.

### 3. `utils/frdr_metadata.py` could bootstrap Research

For datasets that reference or extend existing FRDR datasets, the metadata fetcher could auto-populate parts of `research.md` — related identifiers, author lists, geographic coverage, etc.

### 4. No README validation against template

An agent could programmatically compare the draft README against `docs/FRDR-template_README.txt` to ensure no sections were missed. This is distinct from the preflight check — it's a README-specific quality pass.

### 5. QC could cross-reference Research findings

If Research documents that a certain instrument has a known measurement range, QC could use that to validate value ranges. Currently QC and Research don't talk to each other — QC only looks at files. Connecting them would catch more issues (e.g., "temperature values of 999°C are sentinel values, not real measurements — the manual says this instrument uses 999 as missing").

---

## Noise and overengineering risks

### 1. Subagent delegation is over-prescribed

The Research and Explore sections specify exact subagent splits (Papers/Web/Context for Research; per-format for Explore). This is useful guidance but risks being noise — the agent should decide how to parallelize based on the actual dataset, not a fixed formula. A dataset with 2 PDFs and 50 CSVs needs different parallelism than one with 20 PDFs and 3 Excel files.

**Recommendation:** Keep the delegation sections as *examples* of how to parallelize, not prescriptions. Reword from "Spawn subagents concurrently for:" to "Consider parallelizing across:" — let the agent decide.

### 2. The "prefer xlsx/pdf skills" instruction adds decision complexity

Explore says to prefer available skills for Excel/PDF, then fall back to Python. This creates a decision point that doesn't add much value — pandas + openpyxl handles Excel fine, and pdfplumber handles PDFs. The skills are useful for *creating* documents but for *inspection*, Python libraries are simpler and more reproducible in a notebook.

**Recommendation:** Use Python libraries consistently for data exploration (they're captured in the notebook). Reserve skills for document *creation* (README, reports).

### 3. Autonomy levels table is defined but Level 4 is explicitly unused

Four levels are defined, but Level 4 is deferred. This is fine conceptually but adds cognitive load. Consider removing Level 4 from the table until the workflow is mature enough to use it, or move it to a footnote.

---

## Summary of recommendations

| # | Category | Action | Effort | Status |
|---|----------|--------|--------|--------|
| 1 | Missing | Add dataset initialization step (fold into Scope) | Low | Done |
| 2 | Missing | Write Deposit task description with FRDR field mapping | Low | Done |
| 3 | Opportunity | Document step-level dependency graph, enable Research ∥ Explore | Low | Done |
| 4 | Missing | Define scope-update protocol for feedback loops | Medium | Done |
| 5 | Missing | Add preflight validation step before Deposit | Medium | Done |
| 6 | Missing | Note cross-dataset concerns (collection, vocabulary) | Low | Deferred |
| 7 | Opportunity | Expand `metadata.yaml` to track workflow state + FRDR metadata | Medium | Done |
| 8 | Opportunity | Use `frdr_metadata.py` in Research for related datasets | Low | Done |
| 9 | Opportunity | Add README validation against template | Low | Done |
| 10 | Noise | Soften subagent delegation from prescriptive to suggestive | Low | Done |
| 11 | Noise | Standardize on Python for data exploration, skills for doc creation | Low | Done |
| 12 | Noise | Defer Level 4 definition to a footnote | Low | Done |
