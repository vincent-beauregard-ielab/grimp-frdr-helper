This README.txt file was generated on 2025-10-14 by Antoine Caron-Guay

--------------------
GENERAL INFORMATION
--------------------

1. Title of Dataset: High-Resolution Arctic Vegetation Maps and Photogrammetry Data from Drone Surveys at Trail Valley Creek, Northwest Territories (2023)

2. Author Information
	A. Project Lead Contact Information
		Name: Antoine Caron-Guay
		Institution: Institut de recherche en biologie végétale, Département de sciences biologiques, Université de Montréal
		Email: antoine.caron-guay@umontreal.ca

	B. Co-investigator Contact Information
		Name: Etienne Laliberté
		Institution: Institut de recherche en biologie végétale, Département de sciences biologiques, Université de Montréal
		Email: etienne.laliberte@umontreal.ca

	C. Co-investigator Contact Information
		Name: Oliver Sonnentag
		Institution: Département de géographie, Université de Montréal
		Email: oliver.sonnentag@umontreal.ca


3. Date of data collection: 
	from 2023-07-24 to 2023-07-29

4. Geographic location of data collection: 
	Trail Valley Creek researh station, Northwest Territories, Canada (68.7420508, -133.5018321)

5. Information about funding sources that supported the collection of the data:	
	ArcticNet

---------------------------
SHARING/ACCESS INFORMATION
---------------------------

1. Licenses/restrictions placed on the data: 
	These data are available under a CC0 1.0 license <https://creativecommons.org/publicdomain/zero/1.0/> 

2. Was data derived from another source? 
	No

3. Recommended citation for this dataset: 
	Caron-Guay, A., Laliberté, E., Sonnentag, O. (2025). High-resolution vegetation maps from drone imagery in Arctic upland tundra. Federated Research Data Repository. doi:https://doi.org/10.20383/103.01418

---------------------
DATA & FILE OVERVIEW
---------------------

1. Dataset Structure

     		|--labels
        		|--2023_tvc_grid.gpkg
			|--2023_tvc_labels_aoi.gpkg
			|--2023_tvc_labels.gpkg
		|--photogrammetry
        		|--2023_tvc_drone_missions_aoi.gpkg
        		|--20230724_alder25_m3m
				|--20230724_alder25_m3m_dsm.cog.tif
				|--20230724_alder25_m3m_pg.copc.laz
				|--20230724_alder25_m3m_report.pdf
				|--20230724_alder25_m3m_rgb.cog.tif
        		|--20230724_alder39_m3m
        		|--20230724_alder39_m3m
        		|--20230724_alder4_m3m
        		|--20230724_birch24_m3m
        		|--20230724_birch26_m3m
        		|--20230724_birch30_m3m
        		|--20230724_birch33_m3m
        		|--20230724_birch54_m3m
        		|--20230724_lichentundra17_m3m
        		|--20230724_lichentundra21_m3m
        		|--20230724_lichentundra35_m3m
        		|--20230724_lichentundra41_m3m
        		|--20230724_lichentundra45_m3m
        		|--20230724_polygon29_m3m
        		|--20230724_riparianshrub20_m3m
        		|--20230724_riparianshrub23_m3m
        		|--20230724_riparianshrub32_m3m
        		|--20230724_riparianshrub36_m3m
        		|--20230724_sedge_mosstundra16_m3m
        		|--20230724_sedge_mosstundra22_m3m
        		|--20230724_sedge_mosstundra34_m3m
        		|--20230724_sedge_mosstundra38_m3m
        		|--20230725_alder3_m3m
        		|--20230725_birch2_m3m
        		|--20230725_sedge_mosstundra10_m3m
        		|--20230725_sedge_mosstundra19_m3m
        		|--20230725_tussockfield_m3m
				|--20230725_tussockfield_m3m_chm_above20cm.tif
				|--20230725_tussockfield_m3m_chm_above40cm.tif
				|--20230725_tussockfield_m3m_chm.tif
				|--20230725_tussockfield_m3m_dtm.tif
				|--20230725_tussockfield_m3m_dsm.cog.tif
				|--20230725_tussockfield_m3m_pg.copc.laz
				|--20230725_tussockfield_m3m_report.pdf
				|--20230725_tussockfield_m3m_rgb.cog.tif
        		|--20230725_tussockfieldsub_m3m
        		|--20230726_lichentundra9_m3m
        		|--20230726_polygon5_m3m
        		|--20230726_smalltowerfpsub_m3m
        		|--20230728_birch42_m3m
        		|--20230728_lichentundra44_m3m
        		|--20230728_tussockfield46_m3m
        		|--20230728_tussockfield51_m3m
        		|--20230728_tussockfield53_m3m
        		|--20230729_smalltowerfp_m3m
		|--vegetation_map_models
			|--2023_tvc_highres_model.pth
			|--2023_tvc_lowres_model.pth
			|--2023_tvc_medres_model.pth
			|--2023_tvc_plots_highres_vegetation_map.gpkg
			|--2023_tvc_smalltowerfp_lowres_vegetation_map.gpkg
			|--2023_tvc_smalltowerfp_lowres_vegetation_map.tif
			|--2023_tvc_smalltowerfp_vegetation_map.png
			|--2023_tvc_subsample_medres_vegetation_map.gpkg
			|--2023_tvc_test_aoi.gpkg
			|--2023_tvc_tussockfield_lowres_vegetation_map.gpkg
			|--2023_tvc_tussockfield_lowres_vegetation_map.tif

2. Folder List

   A. Foldername: labels    
      Description: Contains geopackages for annotations and tiling.

   B. Foldername: photogrammetry    
      Description: Each subfolder contains metashape products for a drone mission (orthomosaic RGB (_rgb.cog.tif), digital surface model (_dsm.cog.tif), photogrammetric point cloud (_pg.copc.laz) and processing report (.pdf). n=38
      Two missions (20230725_tussockfield_m3m & 20230729_smalltowerfp_m3m) also include canopy height models (_chm*.tif) and a digital terrain model (_dtm.tif).

   C. Foldername: vegetation_map_models   
      Description: Trained model weights and derived vegetation map products.

3. File List

	A. Filename: labels/2023_tvc_grid.gpkg
	   Description: Grid made up of 25 by 25 cm squares overlaid on plot missions.

	B. Filename: labels/2023_tvc_labels_aoi.gpkg
	   Description: Area where species have been identified.

	C. Filename: labels/2023_tvc_labels.gpkg
	   Description: Labels with species identification.

	D. Filename: photogrammetry/2023_tvc_drone_missions_aoi.gpkg
	   Description: Area of interest (aoi) covered by drone missions.

	E. Filename: vegetation_map_models/2023_tvc_*_model.pth
	   Description: Model weights for different resolution models.

	F. Filename: vegetation_map_models/2023_tvc_plots_highres_vegetation_map.gpkg
	   Description: Model predictions at high resolution for all plot missions (n = 34).

	G. Filename: vegetation_map_models/2023_tvc_smalltowerfp_lowres_vegetation_map{.gpkg|.tif}
	   Description: Model predictions at low resolution for 20230729_smalltowerfp_m3m mission.

	H. Filename: vegetation_map_models/2023_tvc_smalltowerfp_vegetation_map.png
	   Description: Map of the model predictions at low resolution for 20230729_smalltowerfp_m3m mission. Green = graminoid, blue = lichen, purple = dwarf shrub (under 20 cm) and orange = tall shrub (above 20 cm).

	I. Filename: vegetation_map_models/2023_tvc_subsample_medres_vegetation_map.gpkg
	   Description: Model predictions at medium resolution for the two subsample missions (20230725_tussockfieldsub_m3m & 20230726_smalltowerfpsub_m3m).

	J. Filename: vegetation_map_models/2023_tvc_test_aoi.gpkg
	   Description: Test area to create the test dataset at each resolution.

	K. Filename: vegetation_map_models/2023_tvc_tussockfield_lowres_vegetation_map{.gpkg|.tif}
	   Description: Model predictions at low resolution for 20230725_tussockfield_m3m mission.

4. Relationship between files, if important: 
	Each file name for photogrammetry products contains a site ID.
	Each file related to a drone mission is identified by a mission ID, which is formatted according to the following convention: <yyyymmdd>_<site>_<instrument>.

5. Additional related data collected that was not included in the current data package: 
	Raw DJI Mavic 3M RGB images
	Raw DJI Mavic 3M multispectral images

---------------------------
METHODOLOGICAL INFORMATION
---------------------------

1. Description of methods used for collection/generation of data: 

	Imagery acquisition

	The missions were performed using the DJI Mavic 3 Multispectral. 
	The high resolution (plot) missions were flown at a height of 8-10 m above the ground to obtain a GSD of 2.5 mm/pixel, with 80% side overlap and 80% front overlap. 
	The medium resolution (subsample) missions (20230725_tussockfieldsub_m3m & 20230726_smalltowerfpsub_m3m) were flown at a height of 30 m above the ground to obtain a GSD of 8 mm/pixel, with 70% side overlap and 85% front overlap.
	The low resolution missions (20230725_tussockfield_m3m & 20230729_smalltowerfp_m3m) were flown at a height of 60 m above the ground to obtain a GSD of 1.6 cm/pixel, with 70% side overlap and 85% front overlap.
	For precise georeferencing, RTK base was used for all missions, achieving centimeter accuracy. 

	Annotations dataset

	Annotations were made in the office using data collected in the field and ArcGIS Pro v.3.0 software.
	Grids made up of 25 by 25 cm squares were created and overlaid on the plot missions surveyed by the drone. 
	Lines were drawn in a distinct map layer where species could be identified from photo interpretation.
	Areas to include where species have been identified were also drawn to distinguish from background.

2. Methods for processing the data: 

	The RGB photos were processed using Agisoft Metashape 2.1.0 software to generate the orthomosaic for each mission. 
	A DEM was generated from the sparse point cloud and a orthomosaic was generated from the DEM. 

3. Describe any quality-assurance procedures performed on the data: 
	Visual inspection of orthomosaics in ArcGIS Pro
	Visual inspection of vectors in ArcGIS Pro

4. People involved with sample collection, processing, analysis and/or submission: 
	Antoine Caron-Guay
	Tyra Cockney Goose
	Hannah Curie
	Etienne Laliberté
	Vincent Le Falher
	Sabrina Demers-Thibeault
	Oliver Sonnentag

-----------------------------------------------------------------
DATA-SPECIFIC INFORMATION FOR: labels/2023_tvc_labels.gpkg
-----------------------------------------------------------------

1. Number of variables: 5

2. Variable List:      

    A. Name: Class
       Description: Class of the species

    B. Name: taxonID
       Description: GBIF taxonKey

    C. Name: scientificName
       Description: Scientific name of the species

    D. Name: className
       Description: Name of the species

    E. Name: classCode
       Description: 4-letter code of the species

-----------------------------------------------------------------
DATA-SPECIFIC INFORMATION FOR: vegetation_map_models/2023_tvc_*_*_vegetation_map.gpkg
-----------------------------------------------------------------

1. Number of variables: 2

2. Variable List:      

    A. Name: raster
       Description: Corresponding tile used by the model to obtain prediction

    B. Name: predict
       Description: Vegetation group predicted by the model

-----------------------------------------------------------------
DATA-SPECIFIC INFORMATION FOR: vegetation_map_models/2023_tvc_smalltowerfp_lowres_vegetation_map.gpkg
-----------------------------------------------------------------

1. Number of variables: 5

2. Variable List:      

    A. Name: raster
       Description: Corresponding tile used by the model to obtain prediction

    B. Name: predict
       Description: Vegetation group predicted by the model

    C. Name: predictid
       Description: ID of the vegetation group predicted by the model (1 = graminoid, 2 = lichen, 3 = shrub)

    D. Name: above20cm_mean
       Description: Proportion of the tile (between 0 and 1) where vegetation is above 20 cm, calculated from the canopy height model

    E. Name: above40cm_mean
       Description: Proportion of the tile (between 0 and 1) where vegetation is above 40 cm, calculated from the canopy height model



