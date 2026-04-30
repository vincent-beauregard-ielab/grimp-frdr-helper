# Review

Researcher reviews the two collaboration documents (`README.txt` and `DATA_PREPARATION.md`). The agent operator drives the revision loop and runs preflight after each fix round. The step ends when all 🚩 items are resolved and preflight returns PASS.

**Autonomy:** Level 2 — Human decisions required on all 🚩 items.

**Requires:** Documentation Preparation complete (README.txt with review preamble, first preflight run).

## Revision loop

```
Step 6 complete (README + first preflight)
    │
    ▼
Operator opens PR (optional) or sends documents directly
    │   PR includes: README.txt + DATA_PREPARATION.md
    │   PR description uses the revision instructions boilerplate (see AGENTS.md)
    ▼
Researcher comments on 🚩 items (inline PR comments or direct feedback)
    │
    ▼
Agent operator + agent apply fixes
    │
    ├── Fix touches frdr_data/ ──► Re-run Step 5 (Data Preparation), then Step 6 (Documentation Preparation)
    └── Fix touches README, METADATA.yaml, or report only ──► Apply directly
    │
    ▼
Operator runs preflight → preflight.md updated with timestamped run
    │
    ├── All 🚩 resolved + PASS ──► Proceed to Step 8 (Deposit)
    └── Unresolved items ──────► Another review round (return to researcher)
```

## Modification constraints

During this step, changes are confined to:
- `README.txt`
- `METADATA.yaml`
- `DATA_PREPARATION.md`
- `datasets/{id}/notebooks/`

Fixes that require changes to `frdr_data/` loop back through Steps 5–6 before returning to Review.

## Applying fixes

For each 🚩 item:
1. Confirm the researcher has addressed the underlying question (value confirmed, fact settled, or item explicitly ruled out).
2. Replace the 🚩 and any placeholder text with the confirmed content, or remove the sentence if the item is out of scope.
3. Do not leave any 🚩 without a resolution — "not available" or "not applicable" are valid resolutions.

## Running preflight

After each fix round, append a timestamped section to `artifacts/preflight.md` with:
- What changed since the last run
- Results of each check
- Remaining unresolved 🚩 items (if any)

Preflight checks each run:
- README completeness (no empty sections, no leftover template text)
- No leftover `⚠️ [placeholder]` stubs
- All 🚩 resolved (required for final PASS)
- `frdr_data/` file counts match `DATA_PREPARATION.md`
- `METADATA.yaml` fields complete
- Review preamble **present** (pre-final runs) or **absent** (final run only)

## Final preflight — deposit gate

The step is complete when:
1. All 🚩 items are resolved in both `README.txt` and `DATA_PREPARATION.md`
2. No 🚩 remain
3. Preflight returns PASS

Before the final PASS, strip the review preamble from `README.txt`:

```
⚠️ REVIEW INSTRUCTIONS — REMOVE BEFORE DEPOSIT
...
----------------------------------------------------------------
```

Then verify:

```bash
grep -c "🚩" README.txt                  # must be 0
grep -c "REVIEW INSTRUCTIONS" README.txt  # must be 0
```

Also strip all references to internal project workflow from README.txt:
- File paths pointing inside the repository (`artifacts/`, `datasets/`, `notebooks/`)
- PR or review-round numbers ("PR #2", "review applied 2026-04-28")
- Step names or workflow phrases ("pending researcher confirmation", "flagged for passthrough", "to be confirmed later")

Every sentence in the final README must be self-contained for an external reader with no access to this repository.

Run final preflight after stripping; it must return PASS before proceeding to Deposit.

## Outputs

- Resolved `datasets/{id}/README.txt` — no 🚩, no review preamble, self-contained
- Resolved `datasets/{id}/DATA_PREPARATION.md` — no 🚩
- `datasets/{id}/artifacts/preflight.md` — updated with each run; final entry is PASS
