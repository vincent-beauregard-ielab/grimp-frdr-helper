# Scope Definition

Define the boundaries of what will be archived on FRDR and described by the metadata. This step is iterative — it runs first but gets refined after Research and Explore Data as new information emerges.

**Autonomy:** Level 2 — Agent proposes scope from files + context, researcher validates.

## The scope must capture

- **Temporal extent** — Date range of observations or data collection periods
- **Spatial extent** — Geographic area, sites, coordinate systems
- **Measurements and variables** — What was measured, with what instruments, at what resolution
- **Data boundaries** — Which files are in scope for deposit vs. ancillary/excluded
- **Processing level** — Raw, cleaned, derived, or a mix

## Sub-activities

1. **Initialize dataset** — Create the dataset directory structure if it doesn't exist: `datasets/{id}/`, `datasets/{id}/raw_data/`, `datasets/{id}/frdr_data/`, `datasets/{id}/artifacts/`, and `datasets/{id}/metadata.yaml`. Copy or link raw data files into `raw_data/`.

2. **Elicitation** — Ask questions to understand the dataset: what data was collected, how it is structured, what instruments were used, what processing was applied, and how files should be organized for deposit. Use `docs/project_context.md` for GRIMP/MOACC context and `docs/controlled_vocabulary.md` for standard terminology.

3. **Scope document** — Produce a concise scope statement summarizing the above dimensions. Save to `datasets/{id}/artifacts/scope.md`.

The scope document is a living artifact — see **Scope-update protocol** below.

## Scope-update protocol

When Research or Explore Data discovers information that contradicts or extends the current scope (e.g., broader date range, additional file types, out-of-scope records), the step adds a `## Scope updates` section to its own artifact describing the finding. The main agent consolidates these into `scope.md` before proceeding to Quality Control.

## Outputs

- `datasets/{id}/` directory structure initialized
- `datasets/{id}/metadata.yaml` with identity fields populated
- `datasets/{id}/artifacts/scope.md`
