import json
from pathlib import Path

NB = Path("notebooks/M3_analysis.ipynb")
nb = json.loads(NB.read_text())

def lines(text):
    parts = text.split("\n")
    return [p + "\n" for p in parts[:-1]] + ([parts[-1]] if parts[-1] else [])

LOAD_SRC = """import pandas as pd
from pathlib import Path

# Lahman raw files not required — load the cleaned, committed dataset directly.
# The full raw->clean pipeline is preserved in the markdown above for documentation.
df = pd.read_csv("../data/mlb_player_seasons_1980_2025_lahman_batting.csv")
ps = df.copy()
print(f"Loaded cached dataset: {df.shape}")
df.head()
"""

NOOP_SRC = """# Skipped — the cleaned dataset was loaded directly above.
print("Skipped: dataset already loaded.")
"""

for cell in nb["cells"]:
    if cell["cell_type"] != "code":
        continue
    src = "".join(cell["source"])
    if "lahman_dir" in src and "pd.read_csv" in src:
        cell["source"] = lines(LOAD_SRC)
    elif "bat = batting[batting" in src or "lg_ops = ps.groupby" in src:
        cell["source"] = lines(NOOP_SRC)

NB.write_text(json.dumps(nb, indent=1))
print(f"Patched {NB}")

