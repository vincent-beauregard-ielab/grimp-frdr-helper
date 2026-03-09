# Step 3 — Research: Rogers Pass Snow Profiles

## Goal

Write `datasets/rogers_pass_snow_profiles/artifacts/research.md` following the AGENTS.md research output format (dataset description + glossary). This artifact feeds steps 4–6.

## Strategy

### PDF handling

The PhD thesis (`papers/madore_jean-benoit_PhD_2023.pdf`) is ~130 pages / 16 MB. The Read tool supports 20 pages per request.

**Approach: TOC-guided targeted reads, not brute force.**

The table of contents tells us exactly which pages matter. Three Read calls cover the useful content:

| Pages | Content | Why |
|-------|---------|-----|
| 7–20 | Ch. 2 — Snow properties, metamorphism, SNOWPACK model, FMCW radar theory | Variable definitions, instrument background |
| 21–28 | Ch. 3 — Methodology, study sites, validation data, radar config | Site descriptions, field protocols, data formats |
| 81–100 | Ch. 6 — FMCW radar for snow stratigraphy and melt-freeze crusts | Directly describes radar_k data in this dataset |

Remaining pages (simulation optimization ch. 4–5, appendices) are less relevant to this dataset's instruments and can be read on demand.

**The `document-skills:pdf` skill is not useful here** — it handles PDF creation/editing/merging, not smarter reading.

### Web searches

Supplement the thesis with instrument specs and standards:

- **SnowScope** — SLF/Davos NIR optical profiler (produces the `.csv` SS files)
- **SMP / SnowMicroPen** — SLF snow micro-penetrometer (produces `.pnt` binary files)
- **IRIS** — infrared snow profiler (mentioned in scope, separate data folder)
- **FMCW K-band radar** — 24 GHz radar (produces the `.txt` IQ data files)
- **OGRS** — Observation Guidelines and Recording Standards (CAA field protocol)

### Other sources

- `docs/project_context.md` — organizational context (already read, summarized)
- `datasets/example/README.txt` — reference tone and level of detail
- Meeting notes in `datasets/rogers_pass_snow_profiles/docs/meeting notes/`
- `datasets/rogers_pass_snow_profiles/docs/scope.yaml` — dataset scope definition

## Tasks

1. **Read thesis targeted sections** (3 Read calls: pp. 7–20, 21–28, 81–100)
2. **Web search** instrument specs (SnowScope, SMP, IRIS, FMCW radar K-band)
3. **Web search** standards (CAAML, OGRS latest edition)
4. **Draft `artifacts/research.md`** with:
   - Dataset overall description (scope, objective, organizational context, umbrella initiative)
   - Glossary (terms tagged: instrument, variable, technique, acquisition, processing, initiative, organization)
5. **Refine AGENTS.md** research task instructions based on what worked / what didn't

## Decisions (resolved)

- **Scope:** Rogers Pass 2024-2025 campaign only. No CAAML / historical Parks Canada dataset.
- **IRIS:** Yes, include in scope.

---

# Step 4 — Data Exploration: Rogers Pass Snow Profiles

## Goal

Create and run `notebooks/rogers_pass_snow_profiles_data_exploration.ipynb`. Document findings to `datasets/rogers_pass_snow_profiles/artifacts/data_exploration.md`.

## Dataset inventory

| Type | Count | Format | Description |
|------|-------|--------|-------------|
| `.xlsx` | 13 | Multi-sheet Excel | Stratigraphy templates — one per day/site |
| `.csv` | 322 | Header + tabular | SnowScope (SS) and SMP profiles — depth vs hardness/reflectance |
| `.txt` | 166 | Header + IQ data | FMCW K-band radar — I/Q channels |
| `.pnt` | 79 | Binary | SMP SnowMicroPen — needs `snowmicropyn` |
| `.HEIC` | 22 | Image | Field notebook photos — visual reference, not data |
| `.pdf` | 17 | Document | AWP permits, hazard assessments — admin only |
| `.docx` | 11 | Document | Field notes, planning — context only |

## Strategy

### Dependency check

Before running the notebook, ensure these are in `pyproject.toml`:

- `openpyxl` — read xlsx
- `snowmicropyn` — read .pnt SMP files
- `matplotlib` — plots

### Notebook structure

Explore the **3 core data types** in order of complexity:

1. **Excel stratigraphy files** (`.xlsx`) — enumerate sheets, column names, data types, value ranges. Start with `StratiTemplate.xlsx` (blank template) then one filled file per day.
2. **SnowScope / SMP CSV files** (`.csv`) — parse header block + data block. Check consistency across files (same columns? same serial numbers? same units?).
3. **Radar FMCW files** (`.txt`) — parse header metadata + IQ data matrix. Check frequency config consistency, sample counts.
4. **SMP binary files** (`.pnt`) — use `snowmicropyn` to load and plot a sample profile.
5. **IRIS data** — inspect format, fields, and structure.

For each file type, document per AGENTS.md spec:
- Column names and data types
- Enum/categorical fields and their values
- Value ranges for numeric fields
- Missing value encoding
- Case uniformity across text fields
- File encoding and delimiter

### Folder structure observations

Data is organized by field day:

```
Rogers Pass March 2024-2025/
├── Jour 1 - Fidelity/          (2025-03-01)
├── Jour 2 - Jim Bay/           (2025-03-02)
├── Jour 3 - Hermit/            (2025-03-03)
├── Jour 4 - Fidelity/          (2025-03-04)
├── Jour 5 - Round Hill/        (2025-03-05)
├── Jour 6 - RoundHill and .../  (2025-03-06)
├── AWP/                         (permits)
└── Bouffe et infos/             (logistics)
```

Sites: Fidelity, Jim Bay Corner, Hermit, Round Hill, Christiana Ridge.

## Tasks

1. **Add dependencies** (`snowmicropyn`, `openpyxl` if missing)
2. **Start JupyterLab** (`uv run scripts/jupyter_mcp.py`)
3. **Create notebook** — sections per data type above
4. **Run, debug, iterate** until all file types are parsed and characterized
5. **Write `artifacts/data_exploration.md`** — summary of findings
6. **Refine AGENTS.md** data exploration task instructions

## Sequencing

**Step 3 first, then step 4.** The research glossary from step 3 is needed to interpret what the variables in the data files mean (e.g., what "optical Reflectance Avg" maps to physically, what the radar IQ channels represent).
