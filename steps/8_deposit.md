# Deposit

Upload the dataset to FRDR. This step is irreversible once published.

**Autonomy:** Level 1 — The researcher drives, the agent assists.

**Requires:** Review (Step 7) complete — all 🚩 resolved, final preflight PASS.

## Agent assists with

- Filling in the FRDR metadata submission form fields from the README and `METADATA.yaml`
- Preparing the file list and descriptions for upload
- Generating the recommended citation
- Reviewing the FRDR curator's feedback after submission

## FRDR form field mapping

| FRDR field | Source |
|------------|--------|
| Title, Description, Keywords | README §General Information + `METADATA.yaml` |
| Field of Research | `docs/controlled_vocabulary.md` + researcher input |
| Authors, Affiliations, ORCID | `METADATA.yaml` authors + researcher input |
| Contact | Researcher provides |
| License | `METADATA.yaml` license / README §Sharing/Access |
| Time Period / Collection Period | `METADATA.yaml` time_period/collection_period |
| Geographic coverage | `METADATA.yaml` geographic_coverage |
| Funding | `METADATA.yaml` funding / README §General Information |
| Contributors | `METADATA.yaml` contributors / README §Methodological Information §7 |
| Related Identifiers | `METADATA.yaml` related_identifiers / README §Sharing/Access §2, §3 |
| Notes | README §Data & File Overview |

## Researcher responsibilities

The researcher is responsible for: initiating the FRDR submission, uploading files via Globus, reviewing the final metadata form, and clicking submit.

## Outputs

- Dataset published on FRDR with DOI
- Update `METADATA.yaml` with assigned DOI and FRDR URL
- Update `METADATA.yaml` workflow state: `deposit: "done"`
