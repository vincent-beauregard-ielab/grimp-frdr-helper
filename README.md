# GRIMP FRDR Helper

Agent-assisted toolkit for preparing and documenting GRIMP research datasets for deposit on the [Federated Research Data Repository (FRDR)](https://www.frdr-dfdr.ca/docs/en/).

LLM agents automate metadata generation, data file inspection, and information retrieval from external sources and knowledge bases — ensuring datasets comply with FAIR principles (Findable, Accessible, Interoperable, Reusable) and FRDR requirements.

## Project structure

```
datasets/           # Dataset folders to be deposited on FRDR
  {id}/             #   One directory per dataset
    README.txt      #   FRDR README (from template)
    about.yaml      #   Dataset identity (DOI, FRDR URL)
    artifacts/      #   Research notes, extracted metadata, QC reports
  example/          #   Reference: published Rogers Pass snow profiles dataset (DOI: 10.20383/103.01523)

notebooks/          # Reproducible data exploration and manipulation (Jupyter)

docs/               # Project-level documentation and templates
  project_context.md      # Research context (GRIMP, MOACC, FRDR, FAIR)
  FRDR-template_README.txt  # FRDR README template
  controlled_vocabulary.md  # GRIMP controlled vocabulary for keywords

papers/             # Domain literature (PDFs)
utils/              # Python helper modules
plans/              # Project planning documents
```

## Workflow

Each dataset follows this pipeline:

1. **Research** — Gather context from literature, web sources, and knowledge base to describe the dataset.
2. **Explore** — Inspect data files (structure, variables, ranges, missing values) in a notebook.
3. **Draft README** — Generate the FRDR README from the template using research and exploration outputs.
4. **Quality control** — Validate data integrity and flag issues.
5. **Deposit** — Upload to FRDR with metadata form + README + data files.

## Dependencies

Python dependencies are defined in `pyproject.toml` and managed by `uv`.

- **pandas** — Data exploration and manipulation
- **openpyxl** — Read/write Excel files (required by xlsx skill)
- **pypdf** — PDF reading and manipulation (required by pdf skill)
- **pdfplumber** — PDF text and table extraction (required by pdf skill)
- **jupyter** — Notebook environment for reproducible analysis
- **datalayer/jupyter-mcp-server** — MCP server for Jupyter integration with Claude Code

Claude Code skills (`~/.claude/plugins/`):

- **[document-skills/xlsx](file:///C:/Users/beav3503/.claude/plugins/cache/anthropic-agent-skills/document-skills/69c0b1a06741/skills/xlsx/)** — Excel file parsing and formula recalculation
- **[document-skills/pdf](file:///C:/Users/beav3503/.claude/plugins/cache/anthropic-agent-skills/document-skills/69c0b1a06741/skills/pdf/)** — PDF reading, text extraction, and form handling

## Setup

```bash
uv sync
```

## Usage

### Fetch metadata from an existing FRDR dataset

```bash
uv run python utils/frdr_metadata.py datasets/example/about.yaml
```

### Agent-assisted workflow

Agent instructions are defined in `AGENTS.md`. Agents can:

- Research dataset context and generate `artifacts/research.md`
- Explore data files and summarize structure in notebooks
- Draft FRDR README files from the template
- Run quality control checks on data files

## Resources

- [GRIMP Website](https://grimp.ca/)
- [FRDR Documentation](https://www.frdr-dfdr.ca/docs/en/)
- [FRDR — Describing your data](https://www.frdr-dfdr.ca/docs/en/describing_your_data/)
- [FRDR — Preparing your data](https://www.frdr-dfdr.ca/docs/en/preparing_your_data/)
- [FRDR README template](https://www.frdr-dfdr.ca/docs/txt/README.txt)

### Local references

- [MOACC Data Synthesis](file:///C:/Users/beav3503/OneDrive%20-%20USherbrooke/work/MOACC_synthese_des_donnees_20250923)
- [MOACC Data Management Plan](file:///C:/Users/beav3503/OneDrive%20-%20USherbrooke/work/MOACC_data_management_plan_20250129)
