# CS 4412 Data Mining Project – MLB Player Aging Analysis

## Project Overview
This repository contains work for a CS 4412 Data Mining project investigating patterns in Major League Baseball (MLB) player offensive performance and aging. The main goal of the project is to study how offensive performance changes with age and determine whether aging patterns differ across different types of hitters.

Rather than focusing on prediction alone, the project emphasizes pattern discovery through exploratory analysis, clustering, and classification-based interpretation.

## Milestone 3 Summary
Milestone 3 focuses on completing the end-to-end analysis pipeline and expanding the work beyond Milestone 2.

The analysis includes:
- Dataset construction using historical MLB statistics from the Lahman Baseball Database
- Feature engineering for offensive metrics such as BA, OBP, SLG, OPS, and league-adjusted OPS
- Exploratory data analysis and visualizations
- K-Means clustering with elbow method and silhouette scoring to justify cluster selection
- Cluster profile interpretation using summary statistics
- Aging curve analysis by offensive player profile
- Decision tree analysis used as an interpretability tool to explain the clusters

The main notebook used for the analysis can be found here:

`notebooks/M3_analysis.ipynb`

The Milestone 3 PDF writeup can be found here:

`docs/CS4412_M3_TateYork.pdf`

## Data Source
This project uses the Lahman Baseball Database, a publicly available dataset containing historical Major League Baseball statistics for players, teams, and seasons.

Official source:  
https://sabr.org/lahman-database/

The analysis uses the following tables from the dataset:
- `Batting.csv`
- `People.csv`

These tables are used to combine player-season offensive statistics with demographic information such as birth year in order to calculate player age and construct a player-season dataset.

## Data Reproduction
Raw data files are not committed to the repository.

To reproduce the dataset used in the notebook:

1. Create the following directory:
   `data/raw/lahman/`

2. Download the following files from the Lahman database:
   - `Batting.csv`
   - `People.csv`

3. Place them into:
   `data/raw/lahman/`

4. Open and run:
   `notebooks/M3_analysis.ipynb`

Running the notebook will construct the cleaned player-season dataset and reproduce the analysis outputs.

## Repository Structure
- `data/` – data folders and raw data location
- `docs/` – milestone PDF writeups
- `notebooks/` – Jupyter notebooks for the project
- `README.md` – project overview and instructions

## Author
Tate York  
CS 4412 – Data Mining

## About
CS 4412 Data Mining project exploring MLB player aging patterns using the Lahman Baseball Database.
