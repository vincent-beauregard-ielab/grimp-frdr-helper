⚠️ REVIEW INSTRUCTIONS
This document is part of the FRDR deposit preparation package for **[DATASET TITLE]**.
🚩 marks items requiring your decision — please comment directly on these lines.
⚠️ marks critical context for your understanding — no action required.
Your companion review document is README.txt.
Notebooks and artifacts/ are reference material — you do not need to review them.
----------------------------------------------------------------

# Data Preparation Report

**Dataset:** [DATASET TITLE]
**Dataset ID:** [ID]
**Last updated:** [YYYY-MM-DD]

> **How to read this document.** It is a living document: it is updated at every workflow step, and each period section below carries a status.
> - **Projected** — the plan for Step 5 (Data Preparation). No files have been prepared yet. Your answers to the 🚩 items shape what will be prepared.
> - **Prepared** — Step 5 is done: the section records what was actually done.
> - **Final** — reviewed, all 🚩 resolved, ready for deposit.
> - **Published** — already on FRDR; carried over unchanged.
>
> The document has one section per campaign period (field season), newest first. You only need to read the section for the period under review.

---

<!--
One section per period, newest first. Copy the block below for each period.
Single-period datasets have exactly one section.
Created at the end of Step 4 (status Projected); completed at Step 5 (Prepared); finalized at Step 7 (Final).
-->

## Period [PERIOD, e.g. 2025-2026] — [Projected | Prepared | Final | Published (vN, DOI)]

<!-- AGENT: remove this comment and the banner below at the end of Step 5, and set the period status to Prepared. -->
> ⚠️ **PROJECTED PLAN.** This section describes what Step 5 *will* do, based on the Quality Control findings. No files have been prepared yet. Tables marked "projected" contain expected values and will be replaced by actual results.

### Scope

| Dimension | Value |
|-----------|-------|
| Spatial coverage | [site names; bounding box or region description] |
| Temporal extent | [YYYY-MM-DD to YYYY-MM-DD] |
| Measurement domain | [key variables, instruments, or domain-specific bounds] |

Source: `artifacts/[period/]data_exploration.md` (file-derived) and `artifacts/[period/]research.md` (literature-derived).

### Proposed Deposit Scope

Each row describes one file category or instrument class. Review the Decision column.
🚩 marks any item where a decision is required before deposit can proceed.

| Category | Files | Decision | Rationale |
|----------|-------|----------|-----------|
| [File/instrument type] | [count] | Include | [reason] |
| [File/instrument type] | [count] | Exclude | [reason] |
| 🚩 [Contested item] | [count] | **Pending your decision** — Include or Exclude? | [why this is contested; what each option means for the deposit] |

### frdr_data/ File Tree [(projected)]

```
frdr_data/[period/]
[paste the full tree here; when projected, show the planned structure with expected counts]
```

**Total:** [N] files, [approximate size] [(projected)]

### Change Summary [(projected)]

| Operation | Count |
|-----------|-------|
| Files copied (no content change) | [N] |
| Files renamed | [N] |
| Files with content modifications | [N] |
| Files excluded from deposit | [N] |

### Transformation Log [(planned)]

Each row is one content-level change applied (or, when projected, planned) during data preparation. Packaging-only copies are not listed here.

| File | Transform | Before | After | QC Issue addressed |
|------|-----------|--------|-------|--------------------|
| [filename] | [transform name] | [old value / state] | [new value / state] | [reference to QC issue] |

### Excluded Files [(projected)]

Files present in raw_data/ that are not included in the deposit.

| File | Reason |
|------|--------|
| [filename or pattern] | [rationale — out of scope, duplicate, ancillary, etc.] |

### Unresolved Issues

Items that are not yet resolved. 🚩 marks items requiring your input.

| Issue | Status | Notes |
|-------|--------|-------|
| 🚩 [Issue description] | Pending researcher decision | [context; what you need to decide; what happens for each answer] |
| ⚠️ [Issue description] | Acknowledged — not blocking deposit | [what was done; what the limitation means for reuse] |

---
