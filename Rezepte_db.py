import random
from Zutaten_db import ingredients_db
from recipe import Recipe

ANIMAL_TYPES = {"meat", "dairy"}

def generate_recipe(ingredients_db, vegan=False):
    recipe = {}

    # ---- Zutaten nach Typ filtern ----
    if vegan:
        allowed = {k: v for k, v in ingredients_db.items()
                   if v["type"] not in ANIMAL_TYPES}
    else:
        allowed = ingredients_db.copy()

    # Kategorien extrahieren
    bases = [k for k,v in allowed.items() if v["type"] == "base"]
    vegetables = [k for k,v in allowed.items() if v["type"] == "vegetable"]
    vegan_proteins = [k for k,v in allowed.items() if v["type"] == "vegan_protein"]
    meats = [k for k,v in allowed.items() if v["type"] in {"meat", "fish"}]
    fats = [k for k,v in allowed.items() if v["type"] == "fat"]
    spices = [k for k,v in allowed.items() if v["type"] == "spice"]

    # ---- Basis (immer) ----
    base = random.choice(bases)
    recipe[base] = random.randint(80, 150)

    # ---- Protein ----
    if vegan:
        protein = random.choice(vegan_proteins)
    else:
        protein_pool = meats + vegan_proteins
        protein = random.choice(protein_pool)

    recipe[protein] = random.randint(100, 200)

    # ---- Gemüse (1–3) ----
    selected_veg = random.sample(vegetables, random.randint(1,3))
    for veg in selected_veg:
        recipe[veg] = random.randint(50,150)

    # ---- Optional Fett ----
    if fats and random.random() > 0.5:
        fat = random.choice(fats)
        recipe[fat] = random.randint(5,15)

    # ---- Optional Gewürze ----
    if spices:
        selected_spices = random.sample(spices, random.randint(1,2))
        for spice in selected_spices:
            recipe[spice] = random.randint(1,5)

    name = generate_recipe_name(recipe, ingredients_db)

    return Recipe(name, recipe)



def generate_recipe_name(recipe, ingredients_db):

    base = None
    protein = None
    vegetable = None

    for ingredient in recipe:

        t = ingredients_db[ingredient]["type"]

        if t == "base" and base is None:
            base = ingredient

        elif t in ["vegan_protein", "meat"] and protein is None:
            protein = ingredient

        elif t == "vegetable" and vegetable is None:
            vegetable = ingredient

    parts = []

    if protein:
        parts.append(protein)

    if vegetable:
        parts.append(vegetable)

    if base:
        parts.append(base)

    if len(parts) == 0:
        return "Gemüsegericht"

    return "-".join(parts) + "-Gericht"