import plotly.express as px

# Points with custom labels
points = [
    {"coords": (15511.87, 178838.08, -2662.06), "label": "Cathan's note", "key": "CathanJournal_Vannaka"},
    {"coords": (13009.77, 192183.18, -3076.79), "label": "Priest's Journal", "key": "DragonAttack_A3"},
    {"coords": (5158.74, 190522.33, -3152.06), "label": "Dust-covered Diary", "key": "DragonAttack_A1"},
    {"coords": (31204.24, 163832.16, -857.15), "label": "Soot-stained Diary", "key": "Guthix_C3"},
    {"coords": (29118.59, 156991.25, -795.24), "label": "Ancient Journal Page", "key": "Guthix_C4"},
    {"coords": (19773.88, 173386.00, -1209.76), "label": "Bloodstained Journal", "key": "DragonAttack_A2"},
    {"coords": (48282.27, 177692.72, -4126.38), "label": "Pungent Scribble", "key": "Goblin_B4"},
    {"coords": (73772.44, 186935.55, 649.79), "label": "Tear-Stained Journal", "key": "DragonAttack_A5"},
    {"coords": (68968.64, 178598.08, -344.81), "label": "Grubby Note", "key": "Goblin_B2"},
    {"coords": (61409.37, 160992.44, 4280.25), "label": "Cathan's Journal [Castle]", "key": "CathanJournal_Castle_Content"},
    {"coords": (63040.00, 160405.00, 3415.00), "label": "Duke's Diary", "key": "CastleExtra_2"},
    {"coords": (61445.00, 159035.00, 2935.00), "label": "Servant's Secret Diary", "key": "CastleExtra_1"},
    {"coords": (50467.02, 153659.06, 967.73), "label": "Forgotten Diary", "key": "Guthix_C5"},
    {"coords": (62614.22, 172179.39, -1233.97), "label": "Druid's Memoirs", "key": "Guthix_C2"},
    {"coords": (52153.23, 172030.70, -3823.28), "label": "Scrawled Diary Page", "key": "DragonAttack_A4"},
    {"coords": (55318.52, 126503.59, 2659.44), "label": "Garou Writings", "key": "Garou_D2"},
    {"coords": (68009.06, 135975.21, -1089.97), "label": "Torn Journal Page", "key": "Garou_D1"},
    {"coords": (85904.18, 162732.88, 237.22), "label": "Weathered Diary", "key": "Goblin_B3"},
    {"coords": (81422.86, 173925.76, 759.93), "label": "Grimey Parchment", "key": "Goblin_B1"},
    {"coords": (79928.54, 153565.39, 1696.58), "label": "Muddy Scrawl", "key": "Goblin_B5"},
    {"coords": (87042.54, 133040.86, -1331.81), "label": "Elder's Storybook Page", "key": "Garou_D5"},
    {"coords": (94588.20, 127362.55, 714.95), "label": "Dragonkin Journal Page", "key": "Dragonkin_E1"},
    {"coords": (78184.42, 134319.82, -1343.64), "label": "Cathan's Journal [Ghornfell]", "key": "CathanJournal_Ghornfell"},
    {"coords": (71521.15, 124448.93, -263.95), "label": "Scorched Journal", "key": "Garou_D3"},
    {"coords": (105591.01, 130745.62, -662.41), "label": "Leaf-scented Page", "key": "Abyssal_F2"},
    {"coords": (124886.21, 136676.65, -1276.04), "label": "Bloodstained Page", "key": "Abyssal_F1"},
    {"coords": (138421.51, 76160.98, 4362.87), "label": "Infused Journal", "key": "Dragonkin_E3"},
    {"coords": (140829.65, 123526.97, -26.60), "label": "Dragonkin Notebook Page", "key": "Dragonkin_E4"},
    {"coords": (33581.73, 99721.81, 7101.04), "label": "Leathery Parchment", "key": "Garou_D4"},
    {"coords": (25979.11, 99944.11, 7927.89), "label": "Ritual of Purification", "key": "DogDays_RitualText"},
    {"coords": (19144.77, 72491.17, 14987.82), "label": "Dragonkin Diary Page", "key": "Dragonkin_E2"},
    {"coords": (132249.11, 30610.75, -4076.61), "label": "Ravanna's First Journal", "key": "Fellhollow_Necromancer_1"},
    {"coords": (133234.03, 25634.79, -4582.18), "label": "Weathered Diary", "key": "Fellhollow_Withering_1"},
    {"coords": (136002.69, 5285.60, -3657.03), "label": "Ravanna's Third Journal", "key": "Fellhollow_Necromancer_3"},
    {"coords": (129346.82, -20226.77, -7417.77), "label": "Mould-Covered Journal", "key": "Fellhollow_RisingDead_1"},
    {"coords": (151791.52, -29479.77, -11949.61), "label": "Withered Diary", "key": "Fellhollow_Withering_6"},
    {"coords": (165792.90, -50608.96, -12300.94), "label": "Ravanna's Fourth Journal", "key": "Fellhollow_Necromancer_4"},
    {"coords": (141002.73, -44138.25, -7101.24), "label": "Battered Diary", "key": "Fellhollow_Withering_4"},
    {"coords": (112897.13, -36564.96, -7377.87), "label": "Weathered Journal", "key": "Fellhollow_Withering_5"},
    {"coords": (129159.89, -64598.76, -6727.84), "label": "Ravanna's Seventh Journal", "key": "Fellhollow_Necromancer_7"},
    {"coords": (139716.57, -56387.63, -7309.97), "label": "Ravanna's Fifth Journal", "key": "Fellhollow_Necromancer_5"},
    {"coords": (183590.30, -71401.74, -11666.78), "label": "Lacrussa's Journal", "key": "Fellhollow_Dragonkin_1"},
    {"coords": (157079.98, -57241.76, -12342.03), "label": "Withered Journal", "key": "Fellhollow_RisingDead_2"},
    {"coords": (200467.71, -74865.47, -10352.68), "label": "Laboratory Note", "key": "Fellhollow_Dragonwolves_1"},
    {"coords": (185933.82, -31739.82, -12100.48), "label": "Lacrussa's Writings", "key": "Fellhollow_Dragonkin_4"},
    {"coords": (98009.66, -29908.99, -6891.84), "label": "Dragon-Embossed Journal", "key": "Fellhollow_Withering_3"},
    {"coords": (52872.42, -47313.99, -6991.17), "label": "Ravanna's Second Journal", "key": "Fellhollow_Necromancer_2"},
    {"coords": (59376.08, -48011.97, -6665.92), "label": "Lazilly-Penned Diary", "key": "Fellhollow_Withering_2"},
    {"coords": (58460.12, -46299.69, -6608.43), "label": "Ravanna's Sixth Journal", "key": "Fellhollow_Necromancer_6"},
    {"coords": (27961.52, -40874.98, -4896.20), "label": "Experiment Log", "key": "Fellhollow_Dragonwolves_2"},
    {"coords": (70230.51, -54332.27, -6647.99), "label": "Priestly Journal", "key": "Fellhollow_RisingDead_5"},
    {"coords": (60837.63, -69819.84, -4860.69), "label": "Farmer Fred's Journal", "key": "Fellhollow_Zogre_1"},
    {"coords": (86217.37, -62653.96, -6678.24), "label": "The Tale of the Ghost Wolves", "key": "Fellhollow_Dragonwolves_3"},
    # missing: Lacrussa's Notes
    # {"coords": (-454559.45, -313086.74, -37548.00), "label": "Unknown Journal 1", "key": ""},
    # {"coords": (-455929.76, -325534.06, -37962.00), "label": "Unknown Journal 2", "key": ""},
    # {"coords": (-468570.89, -310195.92, -37327.00), "label": "Unknown Journal 3", "key": ""},
    
]

# Extract x, y, and hover labels
xs = [p["coords"][0] for p in points]
ys = [p["coords"][1] for p in points]
hover_labels = [p["label"] for p in points]

# Build the plot
fig = px.scatter(
    x=xs,
    y=ys,
    hover_name=hover_labels  # this shows your custom labels on hover
)

fig.update_traces(marker=dict(size=10, color="blue"), hoverinfo="text")
fig.update_layout(
    xaxis_title="X",
    yaxis_title="Y",
    title="2D Projection with Custom Labels",
    width=800,
    height=600
)

fig.show()
