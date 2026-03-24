Let's start and document the project.

Push back on project structure / file organization / file naming to make sure we follow good patterns.

## Context

* First brain dump of project organization and file content. Many files are generated, but empty to reflect what I have in mind.

* Search the web and use ressources in README.md

* Search previous works related to this project linked in README.md

## Tasks

0. Research

Research sources and files and gather relevant information to provide problem statement this project is trying to achieve (with sources). Document key concepts. Add any relevant findings.



Output to single md in `docs/`

1. Write AGENTS.md and README.md

From project research.

Agent skills and tasks do not need to be refined at this point, just clarified.

2. Initialize project environment

* Setup python environment (`pyproject.toml`) with relevant packages (pandas, jupyter, etc.)

* Setup MCP servers and skills (datalayer/jupyter-mcp-server). Make sure all skills and mcp are well setup and configured to be used in repo codex settings, github copilot settings and claude settings.

* Add relevant gitignores.

* Create a launcher script (`uv run jupyter-mcp`) that starts both the Jupyter server and the related MCP server

3. Test research

Refine plan and discuss strategy :

    Large pdf constraint – Can we brute force and just send large pdf ? How can the anthropic skill can be used ?

Write datasets\rogers_pass_snow_profiles\artifacts\research.md.

Refine relevant AGENTS task/skill instructions

4. Test data exploration

Refine plan and discuss strategy

Create execute debug iterate /notebooks/rogers_pass_snow_profiles_data_exploration.ipynb

Document in datasets artifacts as md.

Refine relevant AGENTS task/skill instructions

5. Test metadata writing

Refine plan and discuss strategy

Document in datasets README.txt following FRDR template.

Refine relevant AGENTS task/skill instructions

6. Test QC

Refine plan and discuss strategy

Document in datasets artifacts as md.

Refine relevant AGENTS task/skill instructions