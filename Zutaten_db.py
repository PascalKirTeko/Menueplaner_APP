ingredients_db = {

# ================= GRUNDNAHRUNG (10) =================
"Spaghetti": {"price_per_unit": 0.02, "unit": "g", "protein_per_unit": 0.12, "carbs_per_unit": 0.72, "fat_per_unit": 0.015, "type": "base"},
"Penne": {"price_per_unit": 0.02, "unit": "g", "protein_per_unit": 0.12, "carbs_per_unit": 0.72, "fat_per_unit": 0.015, "type": "base"},
"Reis": {"price_per_unit": 0.015, "unit": "g", "protein_per_unit": 0.07, "carbs_per_unit": 0.78, "fat_per_unit": 0.006, "type": "base"},
"Risottoreis": {"price_per_unit": 0.02, "unit": "g", "protein_per_unit": 0.07, "carbs_per_unit": 0.78, "fat_per_unit": 0.006, "type": "base"},
"Quinoa": {"price_per_unit": 0.03, "unit": "g", "protein_per_unit": 0.14, "carbs_per_unit": 0.64, "fat_per_unit": 0.06, "type": "base"},
"Couscous": {"price_per_unit": 0.02, "unit": "g", "protein_per_unit": 0.13, "carbs_per_unit": 0.77, "fat_per_unit": 0.01, "type": "base"},
"Kartoffeln": {"price_per_unit": 0.01, "unit": "g", "protein_per_unit": 0.02, "carbs_per_unit": 0.17, "fat_per_unit": 0.001, "type": "base"},
"Süsskartoffeln": {"price_per_unit": 0.015, "unit": "g", "protein_per_unit": 0.016, "carbs_per_unit": 0.20, "fat_per_unit": 0.001, "type": "base"},
"Brot": {"price_per_unit": 0.015, "unit": "g", "protein_per_unit": 0.09, "carbs_per_unit": 0.49, "fat_per_unit": 0.03, "type": "base"},
"Tortilla": {"price_per_unit": 0.02, "unit": "g", "protein_per_unit": 0.08, "carbs_per_unit": 0.52, "fat_per_unit": 0.07, "type": "base"},

# ================= FLEISCH (8) =================
"Hackfleisch": {"price_per_unit": 0.055, "unit": "g", "protein_per_unit": 0.26, "carbs_per_unit": 0, "fat_per_unit": 0.20, "type": "meat"},
"Rindfleisch": {"price_per_unit": 0.065, "unit": "g", "protein_per_unit": 0.27, "carbs_per_unit": 0, "fat_per_unit": 0.21, "type": "meat"},
"Pouletbrust": {"price_per_unit": 0.055, "unit": "g", "protein_per_unit": 0.31, "carbs_per_unit": 0, "fat_per_unit": 0.036, "type": "meat"},
"Schweinefleisch": {"price_per_unit": 0.055, "unit": "g", "protein_per_unit": 0.25, "carbs_per_unit": 0, "fat_per_unit": 0.22, "type": "meat"},
"Kalbfleisch": {"price_per_unit": 0.065, "unit": "g", "protein_per_unit": 0.30, "carbs_per_unit": 0, "fat_per_unit": 0.07, "type": "meat"},
"Speck": {"price_per_unit": 0.06, "unit": "g", "protein_per_unit": 0.37, "carbs_per_unit": 0, "fat_per_unit": 0.42, "type": "meat"},
"Wienerli": {"price_per_unit": 2.2, "unit": "Stk", "protein_per_unit": 12, "carbs_per_unit": 2, "fat_per_unit": 22, "type": "meat"},
"Salami": {"price_per_unit": 0.06, "unit": "g", "protein_per_unit": 0.22, "carbs_per_unit": 0.01, "fat_per_unit": 0.38, "type": "meat"},

# ================= FISCH (6) =================
"Lachs": {"price_per_unit": 0.07, "unit": "g", "protein_per_unit": 0.22, "carbs_per_unit": 0, "fat_per_unit": 0.13, "type": "meat"},
"Thunfisch": {"price_per_unit": 0.05, "unit": "g", "protein_per_unit": 0.29, "carbs_per_unit": 0, "fat_per_unit": 0.01, "type": "meat"},
"Kabeljau": {"price_per_unit": 0.06, "unit": "g", "protein_per_unit": 0.18, "carbs_per_unit": 0, "fat_per_unit": 0.007, "type": "meat"},
"Forelle": {"price_per_unit": 0.065, "unit": "g", "protein_per_unit": 0.20, "carbs_per_unit": 0, "fat_per_unit": 0.12, "type": "meat"},
"Garnelen": {"price_per_unit": 0.08, "unit": "g", "protein_per_unit": 0.24, "carbs_per_unit": 0, "fat_per_unit": 0.003, "type": "meat"},
"Sardinen": {"price_per_unit": 0.05, "unit": "g", "protein_per_unit": 0.25, "carbs_per_unit": 0, "fat_per_unit": 0.11, "type": "meat"},

# ================= VEGANE PROTEINE (6) =================
"Tofu": {"price_per_unit": 0.04, "unit": "g", "protein_per_unit": 0.15, "carbs_per_unit": 0.02, "fat_per_unit": 0.08, "type": "vegan_protein"},
"Tempeh": {"price_per_unit": 0.045, "unit": "g", "protein_per_unit": 0.20, "carbs_per_unit": 0.09, "fat_per_unit": 0.11, "type": "vegan_protein"},
"Linsen": {"price_per_unit": 0.02, "unit": "g", "protein_per_unit": 0.25, "carbs_per_unit": 0.60, "fat_per_unit": 0.01, "type": "vegan_protein"},
"Kichererbsen": {"price_per_unit": 0.02, "unit": "g", "protein_per_unit": 0.19, "carbs_per_unit": 0.61, "fat_per_unit": 0.06, "type": "vegan_protein"},
"Kidneybohnen": {"price_per_unit": 0.02, "unit": "g", "protein_per_unit": 0.24, "carbs_per_unit": 0.60, "fat_per_unit": 0.01, "type": "vegan_protein"},
"Sojahack": {"price_per_unit": 0.03, "unit": "g", "protein_per_unit": 0.50, "carbs_per_unit": 0.30, "fat_per_unit": 0.01, "type": "vegan_protein"},

# ================= GEMÜSE (12) =================
"Tomaten": {"price_per_unit": 0.03, "unit": "g", "protein_per_unit": 0.009, "carbs_per_unit": 0.039, "fat_per_unit": 0.002, "type": "vegetable"},
"Zwiebeln": {"price_per_unit": 0.02, "unit": "g", "protein_per_unit": 0.011, "carbs_per_unit": 0.09, "fat_per_unit": 0.001, "type": "vegetable"},
"Knoblauch": {"price_per_unit": 0.05, "unit": "g", "protein_per_unit": 0.063, "carbs_per_unit": 0.33, "fat_per_unit": 0.005, "type": "vegetable"},
"Paprika": {"price_per_unit": 0.04, "unit": "g", "protein_per_unit": 0.01, "carbs_per_unit": 0.06, "fat_per_unit": 0.003, "type": "vegetable"},
"Brokkoli": {"price_per_unit": 0.03, "unit": "g", "protein_per_unit": 0.028, "carbs_per_unit": 0.07, "fat_per_unit": 0.003, "type": "vegetable"},
"Karotten": {"price_per_unit": 0.02, "unit": "g", "protein_per_unit": 0.009, "carbs_per_unit": 0.10, "fat_per_unit": 0.002, "type": "vegetable"},
"Zucchini": {"price_per_unit": 0.03, "unit": "g", "protein_per_unit": 0.012, "carbs_per_unit": 0.03, "fat_per_unit": 0.003, "type": "vegetable"},
"Champignons": {"price_per_unit": 0.04, "unit": "g", "protein_per_unit": 0.031, "carbs_per_unit": 0.03, "fat_per_unit": 0.003, "type": "vegetable"},
"Spinat": {"price_per_unit": 0.03, "unit": "g", "protein_per_unit": 0.029, "carbs_per_unit": 0.036, "fat_per_unit": 0.004, "type": "vegetable"},
"Blumenkohl": {"price_per_unit": 0.03, "unit": "g", "protein_per_unit": 0.019, "carbs_per_unit": 0.05, "fat_per_unit": 0.003, "type": "vegetable"},
"Aubergine": {"price_per_unit": 0.035, "unit": "g", "protein_per_unit": 0.01, "carbs_per_unit": 0.06, "fat_per_unit": 0.002, "type": "vegetable"},
"Erbsen": {"price_per_unit": 0.025, "unit": "g", "protein_per_unit": 0.054, "carbs_per_unit": 0.14, "fat_per_unit": 0.004, "type": "vegetable"},

# ================= MILCHPRODUKTE (8) =================
"Milch": {"price_per_unit": 0.15, "unit": "dl", "protein_per_unit": 3.4, "carbs_per_unit": 5, "fat_per_unit": 1, "type": "dairy"},
"Rahm": {"price_per_unit": 1.2, "unit": "dl", "protein_per_unit": 2, "carbs_per_unit": 3, "fat_per_unit": 35, "type": "dairy"},
"Butter": {"price_per_unit": 0.04, "unit": "g", "protein_per_unit": 0.01, "carbs_per_unit": 0.01, "fat_per_unit": 0.81, "type": "dairy"},
"Mozzarella": {"price_per_unit": 0.03, "unit": "g", "protein_per_unit": 0.22, "carbs_per_unit": 0.02, "fat_per_unit": 0.22, "type": "dairy"},
"Reibkäse": {"price_per_unit": 0.035, "unit": "g", "protein_per_unit": 0.25, "carbs_per_unit": 0.02, "fat_per_unit": 0.33, "type": "dairy"},
"Parmesan": {"price_per_unit": 0.05, "unit": "g", "protein_per_unit": 0.36, "carbs_per_unit": 0.04, "fat_per_unit": 0.29, "type": "dairy"},
"Frischkäse": {"price_per_unit": 0.035, "unit": "g", "protein_per_unit": 0.06, "carbs_per_unit": 0.04, "fat_per_unit": 0.34, "type": "dairy"},
"Eier": {"price_per_unit": 0.6, "unit": "Stk", "protein_per_unit": 7, "carbs_per_unit": 0.5, "fat_per_unit": 6, "type": "dairy"},

# ================= ÖLE & GEWÜRZE (10) =================
"Olivenöl": {"price_per_unit": 0.9, "unit": "dl", "protein_per_unit": 0, "carbs_per_unit": 0, "fat_per_unit": 100, "type": "fat"},
"Rapsöl": {"price_per_unit": 0.8, "unit": "dl", "protein_per_unit": 0, "carbs_per_unit": 0, "fat_per_unit": 100, "type": "fat"},
"Salz": {"price_per_unit": 0.03, "unit": "g", "protein_per_unit": 0, "carbs_per_unit": 0, "fat_per_unit": 0, "type": "spice"},
"Pfeffer": {"price_per_unit": 0.05, "unit": "g", "protein_per_unit": 0.1, "carbs_per_unit": 0.6, "fat_per_unit": 0.03, "type": "spice"},
"Paprikapulver": {"price_per_unit": 0.06, "unit": "g", "protein_per_unit": 0.14, "carbs_per_unit": 0.54, "fat_per_unit": 0.13, "type": "spice"},
"Chilipulver": {"price_per_unit": 0.06, "unit": "g", "protein_per_unit": 0.12, "carbs_per_unit": 0.50, "fat_per_unit": 0.14, "type": "spice"},
"Oregano": {"price_per_unit": 0.07, "unit": "g", "protein_per_unit": 0.09, "carbs_per_unit": 0.69, "fat_per_unit": 0.04, "type": "spice"},
"Basilikum": {"price_per_unit": 0.07, "unit": "g", "protein_per_unit": 0.03, "carbs_per_unit": 0.48, "fat_per_unit": 0.06, "type": "spice"},
"Petersilie": {"price_per_unit": 0.06, "unit": "g", "protein_per_unit": 0.03, "carbs_per_unit": 0.06, "fat_per_unit": 0.008, "type": "spice"},
"Sojasauce": {"price_per_unit": 0.2, "unit": "dl", "protein_per_unit": 8, "carbs_per_unit": 4, "fat_per_unit": 0, "type": "spice"}

}