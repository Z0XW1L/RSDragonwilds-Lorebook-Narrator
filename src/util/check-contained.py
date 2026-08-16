from pathlib import Path

# ---- configuration ----
file_path = Path("ue-lorecoords.json")      # file to search in
terms = [
    "Fellhollow_VaultPuzzle_2",
]
case_sensitive = False
# -----------------------

def load_text(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="ignore")

def normalize(text: str) -> str:
    return text if case_sensitive else text.lower()

text = normalize(load_text(file_path))

results = {}
for term in terms:
    t = normalize(term)
    results[term] = text.count(t)

# ---- output ----
for term, count in results.items():
    if count > 0:
        print(f"[FOUND]   {term} ({count} occurrence(s))")
    else:
        print(f"[MISSING] {term}")
