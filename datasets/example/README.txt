--------------------
GENERAL INFORMATION
--------------------
Snow profile observation datasets, Glacier National Park, British Columbia, Canada.

2. Author’s information: 
	a. Principal Investigator Contact Information
		Name: Benjamin Imbach
		Institution: Université du Québec à Rimouski
		Email: benjamin.imbach@uqar.ca
			
	b. Research Associate Contact Information
		Name: Jean-Benoit Madore
		Institution: Université de Sherbrooke
		Email: jean-benoit.madore@usherbrooke.ca
		
	c. Research Associate Contact Information
		Name: Andrew Jones
		Institution: Parks Canada 
		Email: andrew.jones@pc.gc.ca 		
		
		Name: Catherine Brown
		Institution: Parks Canada 
		Email: catherine.brown@pc.gc.ca 
	
3. Data description:
This dataset contains snow profile observation taken by the Glacier National Park avalanche forecasting operation. The dataset is saved in CAAML format (http://caaml.org/index.html) as it is widely used for avalanche-related information. Each snow profile is saved as its unique caaml file, and shared in either the "Full" folder for snow profile to the ground, or "Test" folder for partial snow profiles. For more details, please refer to the README file. The name of each folder provide insight on the date of the first and last snow profile in this specific folder. 

4. Geographic location of data and site description:
Glacier National Park Forecasting region. Specific profile location is included in each file.

---------------------------
SHARING/ACCESS INFORMATION
---------------------------
1. Licenses: 
This dataset contains information licensed under the Open Licence – Parks Canada Agency. It is available using the Creative Commons Attribution-NonCommercial 4.0 (CC BY-NC 4.0) license (https://creativecommons.org/licenses/by-nc/4.0/) with approval from Parks Canada Agency. Reuse requires the attribution 'This dataset contains information licensed under the Open Licence – Parks Canada Agency.'

2. Recommended Citation for this dataset: 
	a. Citation: Imbach, B., Madore, J., Jones, A., Brown, C. (2025). Snow profile observation datasets, Glacier National Park, British Columbia, Canada. Federated Research Data Repository. doi: 10.20383/103.01523
	
	b. Acknowledgments: “Contains information licensed under the Open License – Parks Canada Agency.”
	
-----------------------------
PERIOD COVERED BY THE DATASET
-----------------------------
Version 1. (current version) 
	a. Full snow profile : 20150207 to 20240406
	b. hourly dataset : 20151209 to 20240411
	
---------------------
DATA & FILE OVERVIEW
---------------------
1. Naming methodology: 
Each folder represent an upload or update of the database and the dates represents the first and last observation. Inside each main folder, two subfolders separate "Full" snow profile (to the ground), or "Test" (partial snow profiles). Then, each separate files as the same naming strategies: [uniqueID]_[location full name]_[date (yyyy-mm-dd)].

2. Files Structure & Variable type: 
The file structure and variables type all correspond to the methodology specified in the Observation Guidelines and Recording Standards for Weather, Snowpack and Avalanches (OGRS) from the Canadian Avalanche Association. For more information see : www.avalancheassociation.ca/resource/resmgr/docs/ogrs/ogrs2024web.pdf
    
3. Correction and verification: 
Verification was done by the Glacier National Park avalanche forecasting team. Most locations were verified and corrected when error was noticed. However, errors might persist as this is an observational dataset with manual information inputs, user discretion is advised. 

-----------------------
READING AND USING DATA
-----------------------
The CAAML format (http://caaml.org/index.html) as it is widely used for avalanche related information. Each file can be easily read with online tools, such as Niviz (https://niviz.org/). Furthermore, the authors provided a python script to convert CAAML file into different dataframes (https://github.com/grimp-lab/Caaml_Reader)
	a. caaml_df_header : For information on location and weather conditions. 
	b. caaml_layers : For specification on each observed layers
	c. caaml_merged_stability : For each instability test done in the snow profile. 
