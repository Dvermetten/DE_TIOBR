This repository contains code accompanying the paper "The Importance of Being Restrained", in particular for section 6 of the paper.
This code can be viewed in terms of the 4 types of artifacts as described in the reproducibility guidelines of Evolutionary Computation Journal

## Pre-processing code for section 6:
For the results shown in section 6, the code used to access the function-instances is IOHexperimenter, specifically version "ioh==0.3.2.4" used with python 3.8.10. All experimental conditions and scripts used for parameter settings are integraded directly in the algorithm code

## Algorithm code for section 6:
We make use of pyade (https://github.com/xKuZz/pyade), but with a modified version (modified only in terms of initialization and SDIS + some output options). 
The modified code can be found on the github page, in the folder 'pyade'. 
The code used to generate the benchmark data can be found in the script 'benchmark_pyade.py'. Note that because of the original design of pyade, this script can only be executed when in a folder where 'pyade'-folder is included as a subfolder.

To integrate the tracking of POIS and diversity, the file 'commons.py' in the pyade-folder contains a trigger (_write_output) determining whether to write output or not. This is used to collect data, as a more conventional way of storing data would require a full overhaul of the design of each of the included DE-versions. For collecting the POIS data, this trigger should be True, which causes the relevant data to be printed to standard output, which can then be captured into a file (the included 'generate_POIS' notebook shows this process). These files can be processed with the code described in the next section. 

The in-between results are made available as well, in a zenodo repository (). The folder 'benchmark-data' contains the data from the benchmarking stage, in both raw IOH-format as well as processed rds-files generated with IOHanalyzer (these have also been made avaialbe on the IOHanalyzer GUI, when setting datasource to pyade).
The folder 'POIS_data' contains both the raw output-logs as well as the processed pickled dictionaries as described in the next section.

## Processing code for section 6:
For the processing of benchmark data, IOHanalyzer is used (version 0.1.6.1). As mentioned previously, the processed data is avialable on zenodo and on the GUI. 
For the processing of the raw POIS-data, we use the 'process_POIS' notebook, which turns the raw text-files into pickled dictionaries containing corrections, diversity, fitness and population size.

## Presentation code for section 6:
For the benchmark data, we make use of the standard GUI of IOHanalyzer (version 0.1.6.1). The multi-function plots are generated using the 'multi_function_layout.rds' settings, which can be uploaded in the 'settings' tab of IOHanalyzer. The ECDF plots use default settings. 

For the POIS-based data, the notebook 'POIS_analysis' is used. This contains the functions needed to generate all plots based on the pickled dictionaries from the previous section. 

## Citation information
