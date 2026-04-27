# Figures

This folder is the export target for figures generated from
`notebooks/M3_analysis.ipynb`. The notebook produces all figures inline; to
produce static copies for the report or slides, save them while running the
notebook.

For example, immediately before each `plt.show()` call, you can add:

```python
plt.savefig("../figures/age_distribution.png")
```

Suggested filenames (one per figure in the notebook):

| Section | Figure | Suggested filename |
|---------|--------|--------------------|
| 5. EDA | Age distribution | `age_distribution.png` |
| 5. EDA | Mean OPS by age | `mean_ops_by_age.png` |
| 5. EDA | Active players by age | `active_players_by_age.png` |
| 5. EDA | Correlation heatmap | `correlation_heatmap.png` |
| 6. Clustering | Elbow + silhouette panel | `elbow_silhouette.png` |
| 6. Clustering | OBP vs SLG cluster scatter | `cluster_scatter_obp_slg.png` |
| 7. Aging | Aging curves by profile | `aging_curves_by_profile.png` |
| 8. Decision tree | Feature importance | `decision_tree_importance.png` |
| 8. Decision tree | Top-three-levels tree plot | `decision_tree_topology.png` |

The folder is intentionally checked in so the figure paths exist even before
the notebook is run.
