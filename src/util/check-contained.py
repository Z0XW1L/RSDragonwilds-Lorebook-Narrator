from pathlib import Path

# ---- configuration ----
file_path = Path("ue-lorecoords.json")      # file to search in
terms = [
    "CathanJournal_Vannaka",
    "DragonAttack_A3",
    "DragonAttack_A1",
    "Guthix_C3",
    "Guthix_C4",
    "DragonAttack_A2",
    "Goblin_B4",
    "DragonAttack_A5",
    "Goblin_B2",
    "CathanJournal_Castle_Content",
    "CastleExtra_2",
    "CastleExtra_1",
    "Guthix_C5",
    "Guthix_C1",
    "VaultHunterJournal",
    "Guthix_C2",
    "DragonAttack_A4",
    "Garou_D2",
    "Garou_D1",
    "Goblin_B3",
    "Goblin_B1",
    "Goblin_B5",
    "Garou_D5",
    "Dragonkin_E1",
    "CathanJournal_Ghornfell",
    "Garou_D3",
    "Abyssal_F2",
    "Abyssal_F1",
    "Dragonkin_E3",
    "Dragonkin_E4",
    "Garou_D4",
    "DogDays_RitualText",
    "Dragonkin_E2",
    "Fellhollow_Necromancer_1",
    "Fellhollow_Withering_1",
    "Fellhollow_Necromancer_3",
    "Fellhollow_RisingDead_1",
    "Fellhollow_Necromancer_4",
    "Fellhollow_Withering_4",
    "Fellhollow_Withering_5",
    "Fellhollow_Necromancer_7",
    "Fellhollow_Necromancer_5",
    "Fellhollow_Dragonkin_1",
    "Fellhollow_Dragonwolves_1",
    "Fellhollow_Zogre_2",
    "Fellhollow_Withering_3",
    "Fellhollow_Necromancer_2",
    "Fellhollow_Withering_2",
    "Fellhollow_Necromancer_6",
    "Fellhollow_Dragonwolves_2",
    "Fellhollow_RisingDead_5",
    "Fellhollow_Zogre_1",
    "Fellhollow_Dragonwolves_3",
    "Fellhollow_Zogre_3",
    "Fellhollow_RisingDead_4",
    "Fellhollow_RisingDead_2",
    "Fellhollow_Dragonkin_2",
    "Fellhollow_VaultPuzzle_1",
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
