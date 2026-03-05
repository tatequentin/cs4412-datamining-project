\# CS 4412 Data Mining Project – MLB Aging (Milestone 2)



This repository contains the Milestone 2 work for a data mining project exploring patterns in MLB player offensive performance and aging.



\## Contents

\- `notebooks/M2\_analysis.ipynb`  

&nbsp; Builds a player-season dataset from the Lahman Baseball Database, performs exploratory data analysis (EDA), and applies K-Means clustering to identify offensive player profiles.



\## Data Source

This project uses the Lahman Baseball Database (Batting + People tables).



Raw data files are not committed to the repo. To reproduce:

1\. Create `data/raw/lahman/`

2\. Download:

&nbsp;  - `Batting.csv`

&nbsp;  - `People.csv`

3\. Place them into `data/raw/lahman/`



\## Output

The notebook produces a cleaned player-season dataset and visualizations used for the Milestone 2 summary PDF. the M2 summary PDF


# CS 4412 Data Mining Project

## Project Title
Pattern Discovery in MLB Player Aging Curves

## Project Description
This project investigates pattern discovery questions related to Major League Baseball (MLB) player aging, with a specific focus on whether and how player performance deteriorates after age 33. The emphasis is on discovering interpretable patterns, clusters, and outliers in historical performance data rather than predicting future outcomes.

## Dataset Source
Primary data source: Baseball-Reference  
https://www.baseball-reference.com/

## Data Collection Approach
Player-season level data will be collected by scraping MLB league-season "standard" tables (e.g., standard batting and standard pitching pages) from Baseball-Reference. These tables include player age and performance metrics and allow longitudinal analysis across multiple seasons. Raw HTML pages will be cached locally and parsed into structured CSV files for analysis.

## Repository Structure
- `docs/` — LaTeX-generated proposal PDF
- `data/` — data files and cache (large files ignored)
- `src/` — scraping and analysis scripts (added in later milestones)

## Author
Tate York
