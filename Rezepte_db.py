import random
from recipe import Recipe
from Zutaten_db import ingredients_db

#Nicht Vegane Zutatentypen
ANIMAL_TYPES = {"meat", "dairy"}

# --------------------------------
# Rezepte generieren
# --------------------------------

def generate_recipe(ingredients_db, vegan=False):

    recipe = {}

    #Zulassen tierischer Produkte oder nicht
    if vegan:
        allowed = {k: v for k, v in ingredients_db.items()
                   if v["type"] not in ANIMAL_TYPES}
    else:
        allowed = ingredients_db

    #Zutaten nach Typ sortieren
    bases = [k for k,v in allowed.items() if v["type"] == "base"]
    vegetables = [k for k,v in allowed.items() if v["type"] == "vegetable"]
    vegan_proteins = [k for k,v in allowed.items() if v["type"] == "vegan_protein"]
    meats = [k for k,v in allowed.items() if v["type"] == "meat"]
    fats = [k for k,v in allowed.items() if v["type"] == "fat"]
    spices = [k for k,v in allowed.items() if v["type"] == "spice"]

    #Zufällige Zutaten wählen
    base = random.choice(bases)
    recipe[base] = random.randint(80,150)

    if vegan:
        protein = random.choice(vegan_proteins)
    else:
        protein = random.choice(meats + vegan_proteins)

    recipe[protein] = random.randint(100,200)

    for veg in random.sample(vegetables, random.randint(1,3)):
        recipe[veg] = random.randint(50,150)

    #Kleine Menge Fett Hinzufügen 50% Wahrscheinlichkeit
    if fats and random.random() > 0.5:
        fat = random.choice(fats)
        recipe[fat] = random.randint(5,15)

    #Kleine Menge Gewürze hinzufügen 1-2 Stk.
    if spices:
        for spice in random.sample(spices, random.randint(1,2)):
            recipe[spice] = random.randint(1,5)

    name = generate_recipe_name(recipe)

    #Objekt erzeugen/zurückgeben
    return Recipe(name, recipe)

# --------------------------------
# Rezeptnamen generieren
# --------------------------------

def generate_recipe_name(recipe):

    parts = []

    for ingredient in recipe:
        if len(parts) >= 3:
            break
        parts.append(ingredient)

    return "-".join(parts) + "-Gericht"

# --------------------------------
# Kosten berechnen
# --------------------------------

def calculate_recipe_cost(recipe):

    cost = 0

    for name, amount in recipe.ingredients.items():
        ingredient = ingredients_db[name]
        cost += amount * ingredient["price_per_unit"]
    return cost


# --------------------------------
# Kalorien berechnen
# --------------------------------

def calculate_recipe_calories(recipe):

    protein = carbs = fat = 0

    for name, amount in recipe.ingredients.items():
        ingredient = ingredients_db[name]
        protein += amount * ingredient["protein_per_unit"]
        carbs += amount * ingredient["carbs_per_unit"]
        fat += amount * ingredient["fat_per_unit"]
    return protein * 4 + carbs * 4 + fat * 9

# --------------------------------
# Hash für Rezept
# --------------------------------

#Soritert Tuple und macht es so vergleichbar (Duplikate verhindern/Effizienz steigern)
def recipe_to_hashable(recipe):
    return tuple(sorted(recipe.ingredients.items()))


# --------------------------------
# Rezeptpool erzeugen
# --------------------------------

def generate_recipe_pool(size, vegan_mode):

    pool = []
    seen = set()

    attempts = 0

    #Schleife mit Schutz vor Endlosschleife
    while len(pool) < size and attempts < size * 10:
        recipe = generate_recipe(ingredients_db, vegan=vegan_mode)
        key = recipe_to_hashable(recipe)

        #Duppliakte verhindern
        if key not in seen:
            seen.add(key)
            cost = calculate_recipe_cost(recipe)
            calories = calculate_recipe_calories(recipe)
            pool.append((recipe, cost, calories))

        attempts += 1

    return pool

