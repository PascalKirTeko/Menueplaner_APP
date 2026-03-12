import random
from recipe import Recipe
from Zutaten_db import ingredients_db

ANIMAL_TYPES = {"meat", "dairy"}

def generate_recipe(ingredients_db, vegan=False):

    recipe = {}

    if vegan:
        allowed = {k: v for k, v in ingredients_db.items()
                   if v["type"] not in ANIMAL_TYPES}
    else:
        allowed = ingredients_db

    bases = [k for k,v in allowed.items() if v["type"] == "base"]
    vegetables = [k for k,v in allowed.items() if v["type"] == "vegetable"]
    vegan_proteins = [k for k,v in allowed.items() if v["type"] == "vegan_protein"]
    meats = [k for k,v in allowed.items() if v["type"] == "meat"]
    fats = [k for k,v in allowed.items() if v["type"] == "fat"]
    spices = [k for k,v in allowed.items() if v["type"] == "spice"]

    base = random.choice(bases)
    recipe[base] = random.randint(80,150)

    if vegan:
        protein = random.choice(vegan_proteins)
    else:
        protein = random.choice(meats + vegan_proteins)

    recipe[protein] = random.randint(100,200)

    for veg in random.sample(vegetables, random.randint(1,3)):
        recipe[veg] = random.randint(50,150)

    if fats and random.random() > 0.5:
        fat = random.choice(fats)
        recipe[fat] = random.randint(5,15)

    if spices:
        for spice in random.sample(spices, random.randint(1,2)):
            recipe[spice] = random.randint(1,5)

    name = generate_recipe_name(recipe)

    return Recipe(name, recipe)


def generate_recipe_name(recipe):

    parts = []

    for ingredient in recipe:
        if len(parts) >= 3:
            break
        parts.append(ingredient)

    return "-".join(parts) + "-Gericht"