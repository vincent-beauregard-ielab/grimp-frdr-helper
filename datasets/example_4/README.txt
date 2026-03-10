This README.txt file was generated on 2025-09-29 by Prabin Rokaya


--------------------
GENERAL INFORMATION
--------------------

1. Title of Dataset: Snow Survey Data from Lower Athabasca Region in northern Alberta

2. Author Information
	A. Principal Investigator Contact Information
		Name: Prabin Rokaya
		Institution: Alberta Environment and Protected Areas
		Email: Prabin.Rokaya@gov.ab.ca


3. Date of data collection: 2009/02/01-2024/04/05



4. Geographic location of data collection: Lower Athabasca Region, North-east Alberta, Canada



5. Information about funding sources that supported the collection of the data: Oil Sands Monitoring Program


---------------------------
SHARING/ACCESS INFORMATION
---------------------------

1. Licenses/restrictions placed on the data: These data are available under a CC BY 4.0 license <https://creativecommons.org/licenses/by/4.0/> 


2. Links to publications that cite or use the data: 

3. Links/relationships to ancillary data sets or software packages: 

5. Was data derived from another source? No

6. Recommended citation for this dataset: Rokaya, P. (2025). Snow Survey Data from Lower Athabasca Region in northern Alberta. Federated Research Data Repository. doi:https://doi.org/10.20383/103.01458


---------------------
DATA & FILE OVERVIEW
---------------------

1. File List

   A. Filename: OSM_snow_survey_data.csv      
      Short description: Snow data from manual surveys      


2. Relationship between files, if important: NA

3. Additional related data collected that was not included in the current data package: weather conditions, snow conditions, field notes 

4. Are there multiple versions of the dataset? No


---------------------------
METHODOLOGICAL INFORMATION
---------------------------

1. Description of methods used for collection/generation of data: Data was collected through manual snow surveys conducted three times a year during snow cover period (i.e., Feb 1st, March 1st and April 1st). Standard Federal Snow Sampler was used for snow measurements. Snow depth was directly measured, whereas snow water equivalent was obtained through manual profiling by taking vertical snow cores from the top to the bottom of the snowpack with the snow sampler. Snow density was then calculated based on the snow depth and snow water equivalent data for cores. Forty snow depth measurements are taken for each site in a rectangular plot (with four transects that are 10 meters apart with each point measurement 5 meters apart). A mean snow depth was then calculated for each site from 40 snow depth measurements. Afterwards, using the mean snow density and mean snow depth, a mean snow water equivalent was calculated for each survey site. Banker’s rounding or “rounding to the evens”: i.e. 20.5 = 20, 19.5 = 20 was used in calculations.

The detail methodology is described in a manuscript that is currently submitted to Earth System Science Data. This README file will be updated once the publication is accepted to provide a link.


2. Methods for processing the data: Snow depth and snow water equivalent were measured at field. Snow density was then calculated based on the snow depth and snow water equivalent data.


3. Instrument- or software-specific information needed to interpret the data: Standard Federal Snow Sampler was used for snow measurements. No external software has been used to interpret data, except a field sheet, which is hard-coded with equations to generate snow density from snow depth and snow water equivalent, and average values from number of observations.

4. Standards and calibration information, if appropriate: NA

5. Environmental/experimental conditions: variable over the years

6. Describe any quality-assurance procedures performed on the data: Field calculation sheets from each survey were reviewed to ensure outliers were not errors and that survey values were consistent with site conditions as documented in field notes. Several calculation errors were found that ranged from typo mistakes (e.g., 97 for 79) to use of incorrect cells or formulas in density and snow water equivalent calculations. All the errors were corrected in generating a consistent snow survey data from 2009 to 2024. Similarly, this process was also helpful in establishing if data gap was due to absence of snow (e.g., earlier melt in April of 2024), which is still a data vs inability to conduct snow survey (e.g. in April of 2020 due to COVID restrictions).

7. People involved with sample collection, processing, analysis and/or submission: Several monitoring technicians were involved in data collection over the years. The recent year's data collection, all data processing and analyses were conducted by Principal Investigator


-----------------------------------------------------------------
DATA-SPECIFIC INFORMATION FOR: OSM_snow_survey_data.csv     
-----------------------------------------------------------------

1. Number of variables: 3

2. Number of cases/rows: 768

3. Missing data codes: NA

4. Variable List:

    A. Name: Date
       Description: Year, month and day of when manual field survey was performed

    B. Name: Year
       Description: The calendar year

    C. Name: Watershed
       Description: A watershed is a geographic area where all precipitation, like rain and snowmelt, drains to a common body of water, such as a lake, river, or ocean, via a network of streams and groundwater.

    D. Name: Plot	
       Description: The plot name is a unique code that identifies all survey sites. Its consist of oil sands operators acronym and stand code.

    E. Name: Latitude
       Description: Latitude is a geographical coordinate that measures a location's distance north or south of the Earth's Equator, expressed in degrees from 0° at the Equator to 90° at the North and South Poles. Here it represent the survey site location. 

    F. Name: Longitude
       Description: Longitude is a geographic coordinate that measures the east-west position of a point on the Earth's surface. It is measured in degrees, from 0° at the prime meridian to 180° east or west. Here it represent the survey site location. 

    G. Name: Snow depth
       Description: Depth of snow on ground in cm. The measurement date, watershed and plot (including latitude and longitude) is provided for each measurement value.

    H. Name: Snow water equivalent in mm
       Description: water content in snow pack in mm. The measurement date, watershed and plot (including latitude and longitude) is provided for each measurement value.

    I. Name: Snow density
       Description: Density of snow calculated using snow depth and water content in gram per cubic meters. The measurement date, watershed and plot (including latitude and longitude) is provided for each measurement value.

    J. Stand Code: FL = Flat Low Lying, OP = Open, JP = Jack Pine and MD = Mixed Deciduous	
