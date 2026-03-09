# Agent.md

Agents will assist in archiving and documenting research datasets to be deposited on FRDR. Assist in documenting, writing metadata artifacts, structure files from data files, litterature, web sources and helper modules and docs in package.


## Project organization

* **datasets** First class. This is what will be uploaded to the FRDR repository. Also contains artifacts relevant to document and generate FRDR metadata. All contain in individual dataset dir `datasets/{id}`

* **notebooks** First class. All data exploration and manipulation should be done in a reproducible manner in 

* **helper files** Agents/skills/modules/docs that are there to assist and guide.

* **knowledge base** Papers and docs relevant to grimp team research.

## Contraints

All documentation and results written in english.

Code is python and dependencies managed by `uv` in project `.venv`

Run code using `uv run`

## Agent tasks

### Elicitation

Ask question to the user to better understand the data structure, how shoult it be organized.

### Research

TODO : Improve section from project context and README.md

Gather quotes + claims from document and web to describe the dataset variables, methodology and file structure. Output `research.md` document will serve as context for other tasks.

#### Output format

Save results to `{dataset_key}/artifacts/research.md`

#### Output

## Dataset overall description

Scope ? Research objective ? Organisational context – umbrella initiative ?

## Glossary

Also add relevant tags each term as `instrument`, `variable`, `technique`, `acquisition`, `processing`, `initiative`, `organization`

**Term** – *Definition*

### Explore data files

* Use pandas to synthesize data files :

    * Are there enums for certain fields ?
    * What are the range of values ?
    * Does it support N/A values ? How are they encoded
    * Is there a case uniformity for the whole document

* Use excel file skill from anthropic to parse xlsx files

### Draft FRDR README.md

* Template is docs/README.md

* Use document search to document variables captured by data files

* Use document search to document data acquisiton methodology

### Quality control

Explore data file and control for data integrity

Outcomes

* The 

* You can edit column/sheet names for typos 