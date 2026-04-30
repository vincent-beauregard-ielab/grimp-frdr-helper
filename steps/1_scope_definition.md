# Scope Definition

Initialize the dataset and define the boundaries of what will be archived on FRDR. The README.txt is the living scope document — it starts here and is refined by Research and Explore Data as new information emerges.

**Autonomy:** Level 2 — Agent proposes scope from files + context, researcher validates.

## The scope must capture

- **Temporal extent** — Date range of observations or data collection periods
- **Spatial extent** — Geographic area, sites, coordinate systems
- **Measurements and variables** — What was measured, with what instruments, at what resolution
- **Data boundaries** — Which files are in scope for deposit vs. ancillary/excluded
- **Processing level** — Raw, cleaned, derived, or a mix

## Sub-activities

1. **Initialize dataset** — Create the dataset directory structure if it doesn't exist: `datasets/{id}/`, `datasets/{id}/raw_data/`, `datasets/{id}/frdr_data/`, `datasets/{id}/artifacts/`, `datasets/{id}/notebooks/`, and `datasets/{id}/METADATA.yaml`. Copy or link raw data files into `raw_data/`.

2. **Elicitation** — Ask questions to understand the dataset: what data was collected, how it is structured, what instruments were used, what processing was applied, and how files should be organized for deposit. Use `docs/project_context.md` for GRIMP/MOACC context and `docs/controlled_vocabulary.md` for standard terminology. Always ask about relevant documents/sources/PDFs in `papers/` or elsewhere that should inform the Research step.

3. **Initialize README.txt** — Create `datasets/{id}/README.txt` from `docs/FRDR-template_README.txt`. Fill the identity sections (title, authors, dates, geographic location, funding) using information from elicitation and `METADATA.yaml`. Leave all structural sections (file overview, methods, variable lists) as:

   ```
   ⚠️ [placeholder — to be filled at Step 6]
   ```

   Do not add the review preamble. Do not add 🚩 markers. The README at this stage is a draft working document — it is not sent to the researcher until Step 6.

## Scope-update protocol

When Research (Step 2) or Explore Data (Step 3) discovers information that contradicts or extends the current scope (e.g., broader date range, additional file types, out-of-scope records), the agent updates the relevant `README.txt` section directly and notes the change in the step's artifact. There is no separate scope document. The README is the living scope document throughout the workflow.

## Outputs

- `datasets/{id}/` directory structure initialized
- `datasets/{id}/METADATA.yaml` with identity fields populated
- `datasets/{id}/README.txt` — identity sections filled; structural sections stubbed with `⚠️ [placeholder — to be filled at Step 6]`
