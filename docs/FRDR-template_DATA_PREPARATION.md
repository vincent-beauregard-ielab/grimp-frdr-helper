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
**Prepared:** [YYYY-MM-DD]

---

## Dataset scope

Brief summary of what this deposit covers, for reviewer orientation.

| Dimension | Value |
|-----------|-------|
| Spatial coverage | [site names; bounding box or region description] |
| Temporal extent | [YYYY-MM-DD to YYYY-MM-DD] |
| Measurement domain | [key variables, instruments, or domain-specific bounds] |

Source: `artifacts/data_exploration.md` (file-derived) and `artifacts/research.md` (literature-derived).

---

## Proposed Deposit Scope

Each row below describes one file category or instrument class. Review the Decision column.
🚩 marks any item where a decision is required before deposit can proceed.

| Category | Files | Decision | Rationale |
|----------|-------|----------|-----------|
| [File/instrument type] | [count] | Include | [reason] |
| [File/instrument type] | [count] | Exclude | [reason] |
| 🚩 [Contested item] | [count] | **Pending your decision** — Include or Exclude? | [why this is contested; what each option means for the deposit] |

---

## frdr_data/ File Tree

Complete directory tree of the deposit package as prepared.

```
frdr_data/
[paste full tree here]
```

**Total:** [N] files, [approximate size]

---

## Change Summary

| Operation | Count |
|-----------|-------|
| Files copied (no content change) | [N] |
| Files renamed | [N] |
| Files with content modifications | [N] |
| Files excluded from deposit | [N] |

---

## Transformation Log

Each row is one content-level change applied during data preparation. Packaging-only copies are not listed here.

| File | Transform | Before | After | QC Issue addressed |
|------|-----------|--------|-------|--------------------|
| [filename] | [transform name] | [old value / state] | [new value / state] | [reference to QC issue] |

---

## Excluded Files

Files present in raw_data/ that are not included in the deposit.

| File | Reason |
|------|--------|
| [filename or pattern] | [rationale — out of scope, duplicate, ancillary, etc.] |

---

## Unresolved Issues

Items that could not be fully resolved during data preparation. 🚩 marks items requiring your input.

| Issue | Status | Notes |
|-------|--------|-------|
| 🚩 [Issue description] | Pending researcher decision | [context; what you need to decide] |
| ⚠️ [Issue description] | Acknowledged — not blocking deposit | [what was done; what the limitation means for reuse] |
