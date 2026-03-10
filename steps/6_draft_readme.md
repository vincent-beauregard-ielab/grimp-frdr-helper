# Draft FRDR README

Generate the dataset README from `docs/FRDR-template_README.txt`, filling in all applicable sections.

**Autonomy:** Level 2 — Public-facing artifact, needs careful review.

**Requires:** Data Preparation complete.

## Sections to fill

- General information (title, authors, dates, geographic location, funding)
- Sharing/access (license, citation, related datasets)
- Data & file overview (file list with descriptions, naming conventions)
- Methodological information (acquisition methods, processing steps, instruments, software)
- Data-specific sections (variable lists, missing data codes, units)

## Additional coverage

Make sure the draft also accounts for:

- Relationship between files and folders
- Ancillary or excluded files
- Standards and calibration notes
- Quality-assurance notes
- Any format-specific software requirements
- Detailed attribution for any external data sources (title, authors, institution, DOI, access link, date accessed)
- Software/instrument names and versions

## Sources

Use the scope document (`artifacts/scope.md`), research artifact (`artifacts/research.md`), data exploration outputs (`artifacts/data_exploration.md` + notebook), and data preparation notebook as sources. The README should describe the deposit-ready files in `frdr_data/`, not the raw originals. Use `datasets/example/README.txt` as a reference for tone and level of detail.

## Validation

After drafting, compare the README against `docs/FRDR-template_README.txt` section by section. Flag any template sections that are empty or missing. The draft should have no leftover template help text (lines starting with `##`).

## Outputs

- `datasets/{id}/README.txt`
