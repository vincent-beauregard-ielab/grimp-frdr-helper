# Preflight Validation

Final check before deposit. Validates that all deliverables are complete and consistent. This is a fast, automated pass — not a human review gate.

**Autonomy:** Level 3 — Automated checks, no judgment needed.

**Requires:** Draft README complete.

## Checks

- All FRDR required metadata fields are addressed in the README: title, authors, contact, description, keywords, license, date of collection, geographic location
- README has no leftover template help text or empty sections
- `frdr_data/` file list matches the README file inventory (no missing or extra files)
- `metadata.yaml` exists and has at minimum a dataset title
- Geographic coordinates are present (point or bounding box)
- License is explicitly specified
- Scope document, research artifact, QC report, and verification report all exist in `artifacts/`
- All files described in the README have variable definitions, units, and null-value coding
- No files contain protected or restricted information (flag for researcher if uncertain)
- Third-party data sources are credited with proper attribution

## Outputs

- `datasets/{id}/artifacts/preflight.md`

If any check fails, flag it — do not proceed to Deposit until all checks pass or the researcher explicitly waives them.
