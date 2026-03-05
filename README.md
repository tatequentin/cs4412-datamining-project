# CS 4412 Data Mining Project – MLB Player Aging Analysis

## Project Overview

This repository contains work for a CS 4412 Data Mining project investigating patterns in Major League Baseball (MLB) player offensive performance and aging. The goal of the project is to explore how player performance evolves over the course of a career and identify patterns related to offensive production and aging.

Rather than focusing on prediction, the project emphasizes **pattern discovery** using exploratory analysis and unsupervised learning methods.

---

## Milestone 2 Summary

Milestone 2 focuses on constructing a usable dataset and performing exploratory data analysis (EDA) prior to applying data mining techniques.

The analysis includes:

- Dataset construction using historical MLB statistics
- Feature engineering for offensive metrics
- Exploratory data visualizations
- K-Means clustering to identify offensive player profiles

The notebook used for the analysis can be found here:
notebooks/M2_baseball_aging_analysis.ipynb


---

## Data Source

The project uses the **Lahman Baseball Database**, a widely used structured dataset containing historical Major League Baseball statistics.

Source:

https://www.seanlahman.com/baseball-archive/statistics/

The following tables are used:

- `Batting.csv`
- `People.csv`

These tables allow player-season offensive statistics to be combined with demographic information such as birth year to calculate player age.

---

## Data Reproduction

Raw data files are not committed to the repository.

To reproduce the dataset used in the notebook:

1. Create the following directory:
data/raw/lahman/
2. Download the following files from the Lahman database:


Batting.csv
People.csv


3. Place the files into:


data/raw/lahman/


Running the notebook will then construct the cleaned player-season dataset.

---

## Repository Structure


cs4412-datamining-project
│
├── notebooks/
│ └── M2_baseball_aging_analysis.ipynb
│
├── data/
│ └── mlb_player_seasons_1980_2025_lahman_batting.csv
│
├── docs/
│ └── proposal.pdf
│
└── README.md


---

## Author

Tate York  
CS 4412 – Data Mining
