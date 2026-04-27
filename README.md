# CS 4412 Data Mining Project — MLB Player Aging by Offensive Profile

A semester-long pattern-discovery project for CS 4412 (Data Mining) at Kennesaw
State University. The project uses the public Lahman Baseball Database to ask
two questions:

1. **How does offensive performance change with age?**
2. **Do aging curves differ across offensive player profiles?**

The analysis covers 1980–2025, builds a clean player-season dataset, identifies
four offensive profiles via K-Means clustering, examines aging curves by
profile, and uses a decision tree as an interpretability tool to explain what
distinguishes the profiles.

## Headline Findings

- Player-seasons cluster into four interpretable offensive profiles:
  **power**, **balanced**, **contact**, and **low-production**.
- The four profiles remain clearly separated across age. The general aging
  shape — rise through the early-to-mid 20s, plateau, decline in the
  mid-30s — is shared, but production *level* differs substantially by
  profile.
- Decision-tree feature importance shows that league-adjusted OPS,
  home runs, and strikeouts are the variables that most cleanly separate
  the profiles.
- Late-career decline is likely understated due to survivorship bias —
  older player-seasons are disproportionately drawn from above-average
  hitters who survived in the league. The notebook treats this explicitly
  in the validity-and-limitations section.

## Repository Layout

```
.
├── README.md                              <- this file
├── requirements.txt                       <- Python dependencies
├── notebooks/
│   └── M3_analysis.ipynb                  <- end-to-end analysis pipeline
├── data/
│   ├── .gitignore                         <- raw data is not committed
│   └── mlb_player_seasons_1980_2025_lahman_batting.csv
│                                            (cleaned dataset, output of the notebook)
├── docs/
│   ├── York_CS4412_M1_Project_Proposal.pdf
│   ├── York_CS4412_M3_Complete_Implementation.pdf
│   └── York_CS4412_M4_Final_Report.pdf    <- M4 final deliverable
├── figures/                               <- exported figures from the notebook
│   └── README.md
└── slides/
    └── York_CS4412_M4_Presentation.pptx   <- 5–6 minute video deck
```

## Quick Start

### 1. Clone

```bash
git clone https://github.com/tatequentin/cs4412-datamining-project.git
cd cs4412-datamining-project
```

### 2. Install dependencies

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### 3. Get the raw data

The raw Lahman tables are not committed. Download `Batting.csv` and
`People.csv` from the [Lahman Baseball Database](https://sabr.org/lahman-database/)
and place them at:

```
data/raw/lahman/Batting.csv
data/raw/lahman/People.csv
```

### 4. Run the notebook

```bash
jupyter notebook notebooks/M3_analysis.ipynb
```

Run the cells in order. The notebook builds the cleaned player-season
dataset, runs the full analysis, and produces all figures inline.

## Methods at a Glance

| Step | Technique |
|------|-----------|
| Dataset construction | aggregate Lahman Batting by `(playerID, yearID)`, join birth year, compute BA/OBP/SLG/OPS, filter to PA ≥ 200 |
| League adjustment | `OPS_plus_lg = 100 × OPS / LgAvgOPS` (per season and league) |
| Clustering | K-Means on standardized `[BA, OBP, SLG, HR, SO, OPS_plus_lg]` |
| Cluster selection | elbow + silhouette over `k ∈ {2, ..., 8}`, `k = 4` chosen |
| Profile labeling | deterministic mapping from cluster centroids → `{power, balanced, contact, low-production}` |
| Aging analysis | mean OPS by `(profile, Age)` with min-cell-size guard |
| Interpretability | decision tree (`max_depth=4`) trained on cluster labels; feature importance |
| Validity check | seed-stability of the clustering via Adjusted Rand Index |

## Reproducibility Notes

- Random seeds are pinned (`random_state=42`) for both K-Means and the
  decision tree.
- The seed-stability section in the notebook fits K-Means with several
  alternate seeds and reports the Adjusted Rand Index against the
  reference partition.
- The cleaned player-season CSV is committed so that the post-preprocessing
  analysis can be reproduced even without the raw Lahman files.

## Documents

- [Milestone 1 — Project Proposal](docs/York_CS4412_M1_Project_Proposal.pdf)
- [Milestone 3 — Complete Implementation](docs/York_CS4412_M3_Complete_Implementation.pdf)
- [Milestone 4 — Final Report](docs/York_CS4412_M4_Final_Report.pdf)

## Author

**Tate York** — CS 4412 Data Mining, Kennesaw State University.

## Data Source

Lahman Baseball Database, distributed by SABR:
[https://sabr.org/lahman-database/](https://sabr.org/lahman-database/).
