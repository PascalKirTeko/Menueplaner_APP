# menueplan.py

from Rezepte_db import generate_recipe
from Zutaten_db import ingredients_db
from debug_stats import DebugStats
from meal import Meal


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

def recipe_to_hashable(recipe):

    return tuple(sorted(recipe.ingredients.items()))


# --------------------------------
# Rezeptpool erzeugen
# --------------------------------

def generate_recipe_pool(size, vegan_mode):

    pool = []
    seen = set()

    attempts = 0

    while len(pool) < size and attempts < size * 10:

        recipe = generate_recipe(ingredients_db, vegan=vegan_mode)

        key = recipe_to_hashable(recipe)

        if key not in seen:

            seen.add(key)

            cost = calculate_recipe_cost(recipe)
            calories = calculate_recipe_calories(recipe)

            pool.append((recipe, cost, calories))

        attempts += 1

    return pool


# --------------------------------
# Menü generieren
# --------------------------------

def generate_menu(days, max_calories_per_day, vegan_mode):

    stats = DebugStats()

    # größere Pools erzeugen
    breakfast_pool = generate_recipe_pool(30, vegan_mode)
    lunch_pool = generate_recipe_pool(30, vegan_mode)
    dinner_pool = generate_recipe_pool(30, vegan_mode)

    # --------------------------------
    # Dynamische Kalorienbereiche
    # --------------------------------

    breakfast_target = max_calories_per_day * 0.3
    lunch_target = max_calories_per_day * 0.4
    dinner_target = max_calories_per_day * 0.3

    tolerance = max_calories_per_day * 0.05

    BREAKFAST_RANGE = (
        breakfast_target - tolerance,
        breakfast_target + tolerance
    )

    LUNCH_RANGE = (
        lunch_target - tolerance,
        lunch_target + tolerance
    )

    DINNER_RANGE = (
        dinner_target - tolerance,
        dinner_target + tolerance
    )

    # --------------------------------
    # Pools nach Zielkalorien sortieren
    # --------------------------------

    breakfast_pool.sort(key=lambda x: abs(x[2] - breakfast_target))
    lunch_pool.sort(key=lambda x: abs(x[2] - lunch_target))
    dinner_pool.sort(key=lambda x: abs(x[2] - dinner_target))

    # wichtigste Kandidaten behalten
    breakfast_pool = breakfast_pool[:6]
    lunch_pool = lunch_pool[:6]
    dinner_pool = dinner_pool[:6]

    best_menu = None
    lowest_cost = float("inf")
    best_difference = float("inf")

    used_recipes = set()

    # --------------------------------
    # Tageskombinationen einmal berechnen
    # --------------------------------

    day_combinations = []

    for b_recipe, b_cost, b_cal in breakfast_pool:

        if not (BREAKFAST_RANGE[0] <= b_cal <= BREAKFAST_RANGE[1]):
            continue

        for l_recipe, l_cost, l_cal in lunch_pool:

            if not (LUNCH_RANGE[0] <= l_cal <= LUNCH_RANGE[1]):
                continue

        # früher Kaloriencheck
            if b_cal + l_cal > max_calories_per_day * 1.15:
                continue

            for d_recipe, d_cost, d_cal in dinner_pool:

                if not (DINNER_RANGE[0] <= d_cal <= DINNER_RANGE[1]):
                    continue

                day_kcal = b_cal + l_cal + d_cal

                if day_kcal > max_calories_per_day * 1.15:
                    continue

                day_cost = b_cost + l_cost + d_cost

                day_menu = [

                    Meal("breakfast", b_recipe, b_cal),
                    Meal("lunch", l_recipe, l_cal),
                    Meal("dinner", d_recipe, d_cal),

                ]

                keys = [
                    recipe_to_hashable(b_recipe),
                    recipe_to_hashable(l_recipe),
                    recipe_to_hashable(d_recipe),
                ]

                day_combinations.append((day_menu, day_cost, keys))


    # --------------------------------
    # Backtracking
    # --------------------------------

    def backtrack(day_index, current_menu, current_cost):

        nonlocal best_menu, lowest_cost, best_difference

        if best_difference == 0:
            return

        if day_index == days:

            stats.valid_day()

            total_difference = 0

            for day in current_menu:

                day_kcal = sum(meal.calories for meal in day)

                total_difference += abs(max_calories_per_day - day_kcal)

            if (
                total_difference < best_difference
                or (
                    total_difference == best_difference
                    and current_cost < lowest_cost
                )
            ):

                best_menu = [d.copy() for d in current_menu]
                lowest_cost = current_cost
                best_difference = total_difference

                if best_difference == 0:
                    return

            return

        # ------------------------------
        # Tageskombinationen testen
        # ------------------------------

        for day_menu, day_cost, keys in day_combinations:

            if current_cost + day_cost >= lowest_cost:
                stats.prune_cost()
                continue

        # doppelte Rezepte verhindern
            if any(key in used_recipes for key in keys):
                stats.duplicate()
                continue

            used_recipes.update(keys)

            current_menu.append(day_menu)

            backtrack(
                day_index + 1,
                current_menu,
                current_cost + day_cost,
            )

            current_menu.pop()

            used_recipes.difference_update(keys)


    backtrack(0, [], 0)

    # --------------------------------
    # Fallback
    # --------------------------------

    if best_menu is None:

        print("Fallback Menü aktiviert")

        best_menu = []

        for _ in range(days):

            b = breakfast_pool[0]
            l = lunch_pool[0]
            d = dinner_pool[0]

            best_menu.append([

                Meal("breakfast", b[0], b[2]),
                Meal("lunch", l[0], l[2]),
                Meal("dinner", d[0], d[2]),

            ])

        lowest_cost = b[1] + l[1] + d[1]
        best_difference = 0

    stats.print_report()

    return best_menu, lowest_cost, best_difference