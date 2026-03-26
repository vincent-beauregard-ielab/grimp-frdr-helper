# Scope Revision

Consolidate all scope-changing findings from Research, Explore Data, and Quality Control into a revised `scope.md` for human approval before Data Preparation begins.

**Autonomy:** Level 2 — Agent consolidates, human reviews and approves. Data Preparation must not start until scope is approved.

**Depends on:** Quality Control (step 4), which itself depends on Research and Explore Data.

## Trigger

This step runs after QC completes, including the documentation-coverage reconciliation gate. If QC sent targeted research requests back to step 2, those must be resolved before Scope Revision begins.

## Inputs

- `artifacts/scope.md` (original from step 1)
- `artifacts/research.md` § Scope updates
- `artifacts/data_exploration.md` § Scope updates
- `artifacts/qc_report.md` (quality flags, inclusion/exclusion recommendations, reconciliation results)

## Process

1. Collect every `## Scope updates` section from research.md and data_exploration.md.
2. Collect every inclusion/exclusion recommendation and unresolved question from qc_report.md.
3. For each finding, classify as:
   - **Confirmed extension** — new instrument, wider date range, additional site (update scope.md directly)
   - **Confirmed exclusion** — administrative files, out-of-scope records (document in scope.md)
   - **Pending researcher decision** — ambiguous files, quality flags, band designations (mark with 🔔 in scope.md)
4. Write a `## Revision changelog` section at the bottom of scope.md listing every change with its source step.
5. Present the revised scope.md to the human for review.

## Approval criteria

The human confirms:
- Every instrument in the file inventory is either included with documentation or explicitly excluded with rationale.
- Every 🔔 pending item has a decision or is acknowledged as deferred to the researcher.
- The bounding box, date range, and site list match the file evidence.

## Output

- Revised `artifacts/scope.md` with `## Revision changelog` appended.
- `metadata.yaml` updated if scope changes affect metadata fields (dates, bounding box, instruments, keywords).

## Gate

Data Preparation (step 5) must not proceed until the human has approved the revised scope.md. If the human requests changes, iterate on scope.md until approved.
