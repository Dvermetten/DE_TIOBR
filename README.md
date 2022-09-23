This repository contains code accompanying the paper "The Importance of Being Restrained".
This code can be viewed in terms of the 4 types of artifacts as described in the reproducibility guidelines of the Evolutionary Computation journal, and is split on a per-section basis.

The other artefacts (data, figures etc.) can be found on zenodo at https://doi.org/10.5281/zenodo.5900705. The full citation information can be found in the last section of this readme.


## Pre-processing and algorithm code for section 4:

The symbolic computations and the graphical illustrations corresponding to the theoretical analysis (section 4) have been done using Wolfram Mathematica 12.1.1.0 and are included in the following notebooks (readable also using Wolfram Player - https://www.wolfram.com/player)

### BoundViolationProbabilitySaturation.nb  

It contains the visualization of the evolution of the probability to generate components outside the bounding box when the infeasible elements are corrected by applying the saturation strategy and the computation of the limits of this probability (by computing the fixed point of the recurrence relation derived in Section 4.1

### DE_EmpiricalEstimationViolationProbability.nb

Basic implementation of DE/rand/1 combined with five correction strategies: saturation, uniform, mirror, toroidal, halfway-to-violated-bounds. The bound violation probability is estimated as relative frequency of components of the mutant which are generated outside the bounding box (total number of cases divided by the product between problem size, populations size, number of generations and number of independent runs)

### CosineSimilarity.nb

It contains the symbolic computation used to find sufficient conditions under which the similarity between the uncorrected and the corrected search direction is higher for saturation SDIS than for SDISs generating components within the bounds

### PopulationDiversity.nb

It contains the generation of the plots corresponding to the evolution of the population diversity (quantified using standard deviation averaged over all components) based on the theoretical estimations of the variance obtained in Section 4.4 for saturation, uniform and mirroring. The meaning of the used variables and the assumptions under which the results have been derived are specified as comments in the notebook.

## Pre-processing and algorithm code for section 5:
For the results shown in section 5, the code used to access both the function f0 and the DE algorithm is designed in the SOS-platform, with the full code and reproduction steps available at https://github.com/facaraff/SOS/releases/tag/ECJ-ReproducibilityInEC. The files resulting from this process are quite large, and are thus only included in the (aforementioned) zenodo archive of this project.

## Processing code for section 5:
For the processing of the f0-based files is done in 'process_f0.ipyb' notebook, where the SOS-based txt-files are processed into csv-files with the needed information.  

## Presentation code for section 5:
The csv-files generated from the previous header are used in 'visualize_f0' notebook to create the figures as shown in the paper. In addition to the figures from the paper, a large number of additional figure types can be generated using this code. These figures are also included in the Figshare repository of this project, available at https://doi.org/10.6084/m9.figshare.18319394.v1.

## Pre-processing code for section 6:
For the results shown in section 6, the code used to access the function-instances is IOHexperimenter, specifically version "ioh==0.3.2.4" used with python 3.8.10. All experimental conditions and scripts used for parameter settings are integraded directly in the algorithm code

## Algorithm code for section 6:
We make use of ModDE (https://github.com/Dvermetten/ModDE), 
The code used to generate the benchmark data can be found in the notebook 'Generate_DATA_BBOB.ipynb'. This file should be located in the same directory as the ModDe code during execution.

The in-between results are made available as well, in the zenodo repository of this project. The folder 'BBOB-DE' contains the data from the benchmarking stage, in both raw IOH-format as well as processed rds-files generated with IOHanalyzer (these have also been made avaialbe on the IOHanalyzer GUI, when setting datasource to TIOBR). The R-notebook 'Process_BBOB.ipynb' shows the script used to generate the rds-files.

## Processing code for section 6:
For the processing of benchmark data, IOHanalyzer is used (version 0.1.6.3). As mentioned previously, the processed data is avialable on zenodo and on the GUI. 

## Presentation code for section 6:
For the benchmark data, we make use of the standard GUI of IOHanalyzer (version 0.1.6.1). The multi-function plots are generated using the 'multi_function_layout.rds' settings, which can be uploaded in the 'settings' tab of IOHanalyzer. The ECDF plots use default settings, with target option set to 'bbob'. 

For the POIS-based data (including the diversity), the notebook 'Visualize_BBOB' is used. This contains the functions needed to generate all plots based on the  rds files described in the previous section.

<!-- ## Pre-processing code for section 6:
For the results shown in section 6, the code used to access the function-instances is IOHexperimenter, specifically version "ioh==0.3.2.4" used with python 3.8.10. All experimental conditions and scripts used for parameter settings are integrated directly in the algorithm code

## Algorithm code for section 6:
We make use of pyade (https://github.com/xKuZz/pyade), but with a modified version (modified only in terms of initialization and SDIS + some output options). 
The modified code can be found on the github page, in the folder 'pyade'. 
The code used to generate the benchmark data can be found in the script 'benchmark_pyade.py'. Note that because of the original design of pyade, this script can only be executed when in a folder where 'pyade'-folder is included as a subfolder.

To integrate the tracking of POIS and diversity, the file 'commons.py' in the pyade-folder contains a trigger (_write_output) determining whether to write output or not. This is used to collect data, as a more conventional way of storing data would require a full overhaul of the design of each of the included DE-versions. For collecting the POIS data, this trigger should be True, which causes the relevant data to be printed to standard output, which can then be captured into a file (the included 'generate_POIS' notebook shows this process). These files can be processed with the code described in the next section. 

The in-between results are made available as well in the zenodo repository. The folder 'benchmark-data' contains the data from the benchmarking stage, in both raw IOH-format as well as processed rds-files generated with IOHanalyzer (these have also been made available on the IOHanalyzer GUI, when setting datasource to pyade).
The folder 'POIS_data' contains both the raw output-logs as well as the processed pickled dictionaries as described in the next section.

## Processing code for section 6:
For the processing of benchmark data, IOHanalyzer is used (version 0.1.6.1). As mentioned previously, the processed data is available on zenodo and on the GUI. 
For the processing of the raw POIS-data, we use the 'process_POIS' notebook, which turns the raw text-files into pickled dictionaries containing corrections, diversity, fitness and population size.

## Presentation code for section 6:
For the benchmark data, we make use of the standard GUI of IOHanalyzer (version 0.1.6.1). The multi-function plots are generated using the 'multi_function_layout.rds' settings, which can be uploaded in the 'settings' tab of IOHanalyzer. The ECDF plots use default settings. 

For the POIS-based data (including the diversity), the notebook 'POIS_analysis' is used. This contains the functions needed to generate all plots based on the pickled dictionaries from the previous section.  -->

## Citation information

Citation for the data and code:
@dataset{diederick_vermetten_2022_5900706,
  author       = {Diederick Vermetten and
                  Anna V. Kononova and
                  Fabio Caraffini and
                  Madalina Mitran and
                  Daniela Zaharie},
  title        = {The Importance of Being Constrained - Dataset},
  month        = jan,
  year         = 2022,
  publisher    = {Zenodo},
  doi          = {10.5281/zenodo.5900706},
  howpublished = {\url{https://doi.org/10.5281/zenodo.5900706}}
}

Citation for the paper:
To appear later