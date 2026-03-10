# Research

Gather quotes and claims from documents (papers, web sources, knowledge base) to describe the dataset's variables, methodology, and file structure. The output serves as context for README drafting and quality control, so it must capture the non-tabular information required by the FRDR README template.

**Autonomy:** Level 3 — Low risk (gathering quotes). Human spot-checks.

**Parallel with:** Explore Data. These two steps are independent and should run concurrently when possible.

## Sources to use

- Papers in `papers/`
- Web searches for instrument specs, standards (CAAML, OGRS), and related publications
- `docs/project_context.md` for organizational context
- `datasets/example/` as a reference for format and content
- For datasets that reference or extend existing FRDR datasets, run `uv run python utils/frdr_metadata.py datasets/{id}/metadata.yaml` to fetch structured metadata (authors, keywords, geographic coverage, related identifiers) and use it to bootstrap `research.md` and `metadata.yaml`

## Output format

Save results to `datasets/{id}/artifacts/research.md` with sections:

- **Dataset overall description** — Scope, research objective, organizational context, umbrella initiative
- **README input capture** — Candidate title, people/institutions/roles, collection dates, geographic coverage, instruments, standards, processing stages, related publications/datasets/software, file-relationship notes, and unresolved README fields
- **Citable references** — Citation-ready entries for every instrument design, observation standard, processing method, and software package that should appear in the README. Each entry must include: author(s), year, title, DOI or URL. These will be cited inline in the README methods and software sections. For example: `Pomerleau, P. et al. (2020). "A low-cost…" Sensors. https://doi.org/10.3390/s20143909`
- **Glossary** — Key terms tagged as `instrument`, `variable`, `technique`, `acquisition`, `processing`, `initiative`, `organization`, or `standard`. For entries tagged `instrument`, `technique`, or `standard`, include the model/version, key measurement parameters (e.g., frequency, resolution, sampling rate), and a reference to the citable-references entry if one exists
- **Source notes** — Brief claim-to-source mapping for later README drafting

The research artifact should answer as many FRDR README sections as possible before file parsing begins, especially:

- General information
- Sharing/access context
- Methodological context (acquisition protocol per instrument type, not just instrument category names)
- Standards and software context
- Related identifiers and ancillary-resource context

### Instrument and method detail level

For each instrument or technique, capture enough detail to write a concrete README paragraph — not just the category name. Include:

- Instrument model name and version/firmware if available
- Key measurement parameters (frequency, resolution, sampling rate, GSD, overlap, altitude, etc.)
- Acquisition protocol: how is the instrument used in the field (e.g., flight plan, transect spacing, pit wall measurement sequence)
- The design or reference paper that describes the instrument or method, formatted as a citable reference
- Processing chain: what software or workflow transforms the raw output into the deposited product

## Delegation

Research is highly parallelizable. Consider splitting across source types, for example:

- Papers in `papers/` (extract claims from PDFs)
- Web sources (instrument specs, standards, related publications)
- Local context (`docs/project_context.md`, `docs/controlled_vocabulary.md`, `datasets/example/`)

The agent decides the split based on the actual source volume. The main agent merges outputs into the final `research.md`.

## Outputs

- `datasets/{id}/artifacts/research.md`
- Updates to `datasets/{id}/metadata.yaml` (authors, keywords, related identifiers, funding)
