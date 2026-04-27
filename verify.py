import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.metrics import adjusted_rand_score, accuracy_score
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split

df = pd.read_csv("data/mlb_player_seasons_1980_2025_lahman_batting.csv")
print(f"Loaded {len(df):,} player-seasons\n")

feats = ["BA", "OBP", "SLG", "HR", "SO", "OPS_plus_lg"]
X = df[feats].dropna()
X_scaled = StandardScaler().fit_transform(X)

km = KMeans(n_clusters=4, random_state=42, n_init=10).fit(X_scaled)
y = km.labels_

X_tr, X_te, y_tr, y_te = train_test_split(X, y, test_size=0.25,
                                          random_state=42, stratify=y)
tree = DecisionTreeClassifier(max_depth=4, random_state=42).fit(X_tr, y_tr)

print(f"Decision tree train accuracy: {accuracy_score(y_tr, tree.predict(X_tr)):.3f}")
print(f"Decision tree test  accuracy: {accuracy_score(y_te, tree.predict(X_te)):.3f}\n")

imp = pd.Series(tree.feature_importances_, index=feats).sort_values(ascending=False)
print("Feature importance (sklearn DecisionTreeClassifier):")
for f, v in imp.items():
    print(f"  {f:<14} {v:.4f}")

print("\nSeed stability (ARI vs seed=42):")
for s in [0, 7, 13, 21, 99]:
    alt = KMeans(n_clusters=4, random_state=s, n_init=10).fit(X_scaled).labels_
    print(f"  seed={s:3d}: ARI={adjusted_rand_score(y, alt):.4f}")
