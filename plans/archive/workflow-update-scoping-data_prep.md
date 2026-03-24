I want to change the workflow and related tasks in README.md and  AGENTS.md.

**Scope definition**
Required step is now Scope definition - It should capture the time/spatial/measurements/variables/data of what will be archived by FRDR and described by the metadata. Elicitation task was an attempt at it, but just a  badly formed idea - should should be reworded and reworked. Recommend place in  workflow in relation to other steps.


**Data preparation**
Also add a new Data preparation step before deposit. Basically permform data manipulation actions identified in quality control. Also copy and rename files from raw_data to frdr_data. Important. Data preparation should Any relevant action from QC should be moved to there.

All data preparation steps should be captured in a Jupyter notebook for reproducibility.

IMPORTANT: This step should be non-destructive to the original data.

**Human-in-the-loop**
Human in the loop is hard. Recommend 4 different levels of integration that could be planned and make recommendations.