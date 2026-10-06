# Dataset Extension (new version of a published dataset)

Use this file when the work adds a new collection period (typically a new field season) to a dataset that is **already published on FRDR**. The result is a new FRDR version of the same record, with its own DOI.

This file does not replace Steps 1–8. It adds a Baseline step (Step 0) and lists, for each step, only what differs from the normal instructions. Read the normal step file first, then apply the delta below.

## Key concepts

- **Published record = source of truth for the previous version.** Local files in `datasets/{id}/` may be stale (e.g. a DOI or a review fix that never reached `main`). When local and published content disagree, the published content wins, and the discrepancy is noted in `artifacts/baseline.md`.
- **Period** — the unit of extension, named after the field season, e.g. `2024-2025`, `2025-2026`. Each period has its own subfolder in `raw_data/`, `frdr_data/` and `artifacts/`.
- **Previous files are not reprocessed.** Files already published are carried over unchanged. They are only modified to correct a confirmed error (erratum), which must be recorded in `DATA_PREPARATION.md` and in the public summary of changes.
- **How FRDR versions work** ([FRDR docs](https://www.frdr-dfdr.ca/docs/en/create_new_version)):
  - Only the depositor of the published dataset can start a new version ("New Version" in the dashboard or on the landing page).
  - FRDR copies all previous files into the new version; files can then be added, removed or overwritten. Globus uploads can sync only new/changed files or delete files absent from the local source.
  - A "Public Summary of Changes" (max 2,000 characters) is required and shown in the version history table.
  - The new version goes through curation again and receives a **new DOI**. The old DOI keeps resolving to the old version, and FRDR links the versions together.
  - Metadata-only changes and complete file removals go through FRDR support, not through a new version.

## Folder layout

One `datasets/{id}/` folder per FRDR record, for all versions. Do not create a new dataset folder for a new version; git history and tags hold the previous states.

```
datasets/{id}/
├── README.txt                    ← covers all periods + "Version history" section
├── DATA_PREPARATION.md           ← one section per version
├── METADATA.yaml                 ← extended extents + `versions:` list
├── published/v{N}/               ← git-ignored, read-only copy of the published version
├── raw_data/{period}/            ← raw files of the new period only
├── frdr_data/{period}/           ← one subfolder per period (+ shared top-level files)
├── notebooks/
│   ├── restructure_v{N}.ipynb    ← only for the first extension (flat → per-period layout)
│   └── data_preparation_{period}.ipynb
└── artifacts/
    ├── baseline.md
    ├── {period}/research.md, data_exploration.md, qc_report.md
    └── preflight.md
```

If the dataset was first published with a flat layout (no period subfolders), the first extension moves the published files into `frdr_data/{first period}/`. This changes public file paths, so it must be announced in the README version history and the public summary of changes.

Artifacts produced before the dataset was extended (flat `artifacts/research.md`, etc.) are moved into `artifacts/{first period}/` with `git mv`.

## Step 0 — Baseline

**Autonomy:** Level 2. **Output:** `artifacts/baseline.md`, `published/v{N}/`, updated `METADATA.yaml`.

1. **Fetch the published record.** Put the DOI of the latest published version in `METADATA.yaml` (`doi`, `doi_url`), then:

   ```bash
   uv run python -m utils.frdr_metadata datasets/{id}/METADATA.yaml --output datasets/{id}/artifacts/frdr_published_v{N}.json
   ```

   The JSON holds the published title, creators, keywords, license, file list, and under `source` the Globus endpoint ID and `submitted_data` path.

2. **Download the published files** into `published/v{N}/`. One-time prerequisites, done by the human:
   - `GLOBUS_CLIENT_ID` set in `.env`;
   - Globus Connect Personal installed and running, with the repository's `datasets/` folder added as an accessible and **writable** folder (GCP Options → Access). Otherwise the transfer fails with `PERMISSION_DENIED … 500 Path not allowed`;
   - one interactive login (any `utils.globus_transfer` command, e.g. `ls`), which asks for a code pasted from the browser. The agent cannot do this step.

   Then (see `utils/globus_transfer.py`):

   ```bash
   MSYS_NO_PATHCONV=1 uv run python -m utils.globus_transfer download \
       --source-endpoint <source.globus_endpoint_id> \
       --source-path <source.globus_submitted_data_path> \
       --dest-dir datasets/{id}/published/v{N}/ --wait
   ```

   The transfer creates a `submitted_data/` folder inside the destination; move its contents up one level so the files sit directly in `published/v{N}/`. The transfer runs for several minutes: run it in the background.

   Never edit files in `published/`. Verify the download against `frdr-dfdr-checksums.txt` before going further. FRDR generates this file at each publication; it is not part of the submitted dataset, so it is used only for verification and never carried into `frdr_data/`.

3. **Reconcile local documentation with the published record.** Compare `README.txt` and `METADATA.yaml` with the published `README.txt` and the fetched metadata. Replace the local `README.txt` with the published one (it is what users have seen). Update `METADATA.yaml` (DOI, authors, keywords, dates). List every difference found in `artifacts/baseline.md`.

4. **Record the version.** Add the published version to `METADATA.yaml`:

   ```yaml
   versions:
     - version: 1
       doi: "10.20383/103.xxxxx"
       published: "YYYY-MM-DD"
       periods: ["2024-2025"]
   ```

   Propose a git tag `{id}/v{N}` on the commit that matches the published state (or on the baseline commit if none matches). Tags are pushed only with approval.

5. **Reset workflow state** for the new version: set every `workflow:` entry back to `null`, and record the new period under `extension:` in `METADATA.yaml`:

   ```yaml
   extension:
     target_version: 2
     new_period: "2025-2026"
     raw_data_source: ""          # where the raw files of the new period live
   ```

`artifacts/baseline.md` contains: published DOI, date and landing page; published file tree (top level + counts); checksum verification result; local-vs-published differences; whether the layout is flat or per-period.

## Step deltas

### 1. Scope Definition

- Do not re-initialize the dataset. Create only `raw_data/{period}/` and `artifacts/{period}/`, and copy the new raw files there.
- Elicitation focuses on what changed: new sites, instruments, people, protocol changes, and whether new contributors should become authors (researcher decision).
- Extend the existing `README.txt` instead of creating it from the template: extend dates, sites and instrument lists; add stubs `⚠️ [placeholder — to be filled at Step 6]` only for new sections.
- Extend `METADATA.yaml` extents (`time_period`, `collection_period`, `geographic_coverage`) to cover all periods.

### 2. Research

- Start from the previous period's `research.md`. Do not repeat it: the new `artifacts/{period}/research.md` covers only new instruments, protocol or firmware changes, new people and new publications since the last version (including papers that cite the published dataset).
- End with a short "Carried over" list naming the previous entries that still apply unchanged.

### 3. Explore Data

- Explore the new period's raw files as usual, into `artifacts/{period}/data_exploration.md`.
- Add a **Cross-period comparison** section against the previous published version (`published/v{N}/`): instrument folders present/absent, file formats, naming conventions, column headers and units, template versions. Every difference is listed with its consequence for packaging (e.g. "new naming convention for SMP files — decide whether to harmonize").

### 4. Quality Control

- QC the new period as usual, into `artifacts/{period}/qc_report.md`. The documentation-coverage reconciliation uses the new research and exploration artifacts plus the carried-over research entries.
- Add a **Cross-period consistency** section: differences from Step 3 that would confuse a user combining periods (units, site names, column order, codes). For each, recommend harmonizing the new period, documenting the difference, or (rarely) an erratum to the previous period.
- An issue found in the previous published files is reported as an **erratum candidate**, never fixed silently.

### 5. Data Preparation

- **Previous version:** copy `published/v{N}/` into `frdr_data/` unchanged. If the layout is flat, a separate notebook `notebooks/restructure_v{N}.ipynb` moves the period files into `frdr_data/{previous period}/` and keeps shared files (`README.txt`, `LICENSE.txt`, `CITATION.txt`) at the top level. Skip FRDR's generated `frdr-dfdr-checksums.txt`; FRDR regenerates it for each version. The notebook asserts that every published file is present and byte-identical (checksum) after the move, except approved errata.
- **New period:** `notebooks/data_preparation_{period}.ipynb`, following the normal notebook structure, writing only into `frdr_data/{period}/`. Reuse the previous period's naming conventions unless the researcher decided otherwise.
- **`DATA_PREPARATION.md`:** add a section `## Version {N+1} — {period}` with the usual content (scope, tree, change summary, transformation log, exclusions, unresolved issues), plus:
  - a **path mapping table** (published path → new path) if the layout changed;
  - an **errata** list (empty if none).
  Earlier version sections are kept as they are.

### 6. Documentation Preparation

- The README describes the whole dataset (all periods). Add the new period's sites, instruments and methods; mark period-specific statements explicitly ("in 2025-2026 only…").
- Add a **Version history** section listing each version with its DOI, date, periods covered, and a short summary of changes (new period, restructured paths, errata).
- Add to `METADATA.yaml` `related_identifiers`: `{identifier: <previous DOI>, relation_type: "IsNewVersionOf"}`.
- Draft the FRDR **Public Summary of Changes** (≤ 2,000 characters) in `DATA_PREPARATION.md` under the version section, for researcher review.
- New authors, author order and title changes are 🚩 researcher decisions.

### 7. Review

Preflight adds these checks:

- Every published file of v{N} is present in `frdr_data/` at its mapped path, with an identical checksum, unless listed as an erratum or an approved removal.
- The README version history and `DATA_PREPARATION.md` path mapping agree.
- The public summary of changes is ≤ 2,000 characters and mentions every path change and erratum.
- `METADATA.yaml` has the `IsNewVersionOf` relation and extended extents.

### 8. Deposit

- The depositor of the published version uses **New Version** on FRDR (not a new submission).
- Paste the Public Summary of Changes; update metadata from `METADATA.yaml`.
- Upload only what changed: the data folder(s) and the new `README.txt`. In the usual case that is the new period folder `frdr_data/{period}/` plus `README.txt`; FRDR already holds the previous files. `frdr-dfdr-checksums.txt` is never uploaded.
- If the layout changed (first extension of a flat dataset), upload the whole `frdr_data/` and let the Globus transfer **delete files absent from the source**, otherwise FRDR keeps the old flat copies next to the new ones. Check the file list in the FRDR form before finishing.
- After publication: append the new version (DOI, date, periods) to `versions:` in `METADATA.yaml`, set `doi`/`doi_url`/`frdr_url` to the new version, clear `extension:`, and propose the tag `{id}/v{N+1}`.
