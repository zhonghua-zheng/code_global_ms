PartMC-CESM Workflow
======================
[![DOI](https://zenodo.org/badge/261375968.svg)](https://zenodo.org/badge/latestdoi/261375968)   
<!-- @import "[TOC]" {cmd="toc" depthFrom=1 depthTo=6 orderedList=false} -->

<!-- code_chunk_output -->

- [Introduction](#introduction)
- [Prerequisite](#prerequisite)
- [Scirpts and Data](#scirpts-and-data)
  - [Notebooks](#notebooks)
  - [Data](#data)
  - [Others](#others)

<!-- /code_chunk_output -->

## Introduction 

This repository is a supplementary to the manuscript **"Estimating Submicron Aerosol Mixing State at the Global Scale with Machine Learning and Earth System Modeling"**.

The objectives of this project are:

- Use **[extreme gradient boosting (XGBoost or XGB)](https://xgboost.readthedocs.io/en/latest/)** to train the models (emulators) from the **[Particle-resolved Monte Carlo (PartMC)](http://lagrange.mechse.illinois.edu/partmc/)** version 2.5.0 simulations. You may use **[PartMC Scenario Generator](https://github.com/zzheng93/scenario_generator_james)** to create the scenarios
- Apply the models (emulators) to **[CESM2](http://www.cesm.ucar.edu/models/cesm2/)** simulations to predict submicron aerosol mixing state indices

## Prerequisite

- If you do not have the **"[conda](https://docs.conda.io/en/latest/)"** system

```bash
# Download and install conda
$ wget https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh
$ chmod +x Miniconda3-latest-Linux-x86_64.sh
$ ./Miniconda3-latest-Linux-x86_64.sh
# Edit .bash_profile or .bashrc
PATH=$PATH:$HOME/.local/bin:$HOME/bin:$HOME/miniconda3/bin
# Activate the conda system
$source .bash_profile
# OR source .bashrc
```

- Create and activate your own conda environment

```bash
# Create an environment "partmc" and install the necessary packages
conda env create -f environment.yml
# Activate the "partmc" environment
conda activate partmc
```

## Scirpts and Data

### Notebooks

| Tasks                                                        | Folders                          | Fig or Tab in paper    |
| ------------------------------------------------------------ | -------------------------------- | ---------------------- |
| Emulator Development and Application, and Feature Importance | emulator_development_application | Fig 3, Fig 4 and Tab 5 |
| Global Mixing State Indices Analysis                         | global_mixing_state_analysis     | Fig 5-9, and Fig S1-S2 |

### Data

| Folders                                        | Comments                                          |
| ---------------------------------------------- | ------------------------------------------------- |
| data                                           | training and testing data sets for ML emulators   |
| emulator_development_application/xgb_model/    | XGBoost emulators                                 |
| emulator_development_application/linear_model/ | OLS emulators                                     |
| global_mixing_state_analysis/nc_files/         | nc files for global mixing state indices analysis |

### Others

- Figures

| Folders                           | Comments                                                     |
| --------------------------------- | ------------------------------------------------------------ |
| figures                           | all the figures for the manuscript (including code of Fig 1) |
| mixing_state_indices_illustration | making the figures to illustrate different aerosol mixing state indices (Fig 2) |

- Global mixing state indices analysis

```
├── scripts
│   ├── fig_5_6_7_S_global_maps.ipynb.ipynb (global maps: Figs 5, 6, 7, S1, and S2)
│   ├── fig_8_cesm_chi_relationship.ipynb (heat maps: Fig 8)
│   ├── fig_9_boxplot_polluted_areas_northern_hemisphere.ipynb (box plots: Fig 9)
│   ├── analysis_spatial_pattern.ipynb (regional analysis, such as bar plot)
│   ├── analysis_global_counts.ipynb (general analysis, such as max, min, and mean)
│   ├── 3hr_statistics (3hr statistics, such as max and min)
│   ├── analysis_cities.ipynb (cities analysis)
│   ├── preprocessing.ipynb (get the ".nc" files in terms of seasons, and masked the areas)
│   └── util.py (useful functions)
└── nc_files (raw data from ML prediction and masked)
```

## Acknowledgments

We would like to acknowledge high-performance computing support from Cheyenne (doi: 10.5065/D6RX99HX) provided by NCAR’s Computational and Information Systems Laboratory, sponsored by the National Science Foundation. The CESM project is supported primarily by the National Science Foundation. This research used resources of the Oak Ridge Leadership Computing Facility, which is a DOE Office of Science User Facility supported under Contract DE-AC05-00OR22725. This research was supported in part by an appointment to the Oak Ridge National Laboratory ASTRO Program, sponsored by the U.S. Department of Energy and administered by the Oak Ridge Institute for Science and Education. We also acknowledge funding from DOE grant DE-SC0019192 and NSF grant AGS-1254428. This research is part of the Blue Waters sustained-petascale computing project, which is supported by the National Science Foundation (awards OCI-0725070 and ACI-1238993) the State of Illinois, and as of December, 2019, the National Geospatial-Intelligence Agency. Blue Waters is a joint effort of the University of Illinois at Urbana-Champaign and its National Center for Supercomputing Applications. Louisa Emmons is thanked for thoughful comments on the CESM2 simulations and the manuscript. We thank AWS for providing AWS Cloud Credits for Research.

