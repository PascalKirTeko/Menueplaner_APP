# menueplan.py

from Rezepte_db import generate_recipe
from Zutaten_db import ingredients_db
from debug_stats import DebugStats
from meal import Meal


BREAKFAST_RANGE = (300, 700)
LUNCH_RANGE = (500, 1000)
DINNER_RANGE = (400, 900)


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
# Rezept eindeutig machen
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

    while len(pool) < size and attempts < size * 20:

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

    breakfast_pool = generate_recipe_pool(30, vegan_mode)
    lunch_pool = generate_recipe_pool(30, vegan_mode)
    dinner_pool = generate_recipe_pool(30, vegan_mode)

    breakfast_target = max_calories_per_day * 0.3
    lunch_target = max_calories_per_day * 0.4
    dinner_target = max_calories_per_day * 0.3

    breakfast_pool.sort(key=lambda x: abs(x[2] - breakfast_target))
    lunch_pool.sort(key=lambda x: abs(x[2] - lunch_target))
    dinner_pool.sort(key=lambda x: abs(x[2] - dinner_target))

    # nur beste Kandidaten behalten
    breakfast_pool = breakfast_pool[:20]
    lunch_pool = lunch_pool[:20]
    dinner_pool = dinner_pool[:20]

    best_menu = None
    lowest_cost = float("inf")
    best_difference = float("inf")

    used_recipes = set()

    def backtrack(day_index, current_menu, current_cost):

        nonlocal best_menu, lowest_cost, best_difference

        stats.visit_node()

        if day_index == days:

            stats.valid_day()

            total_difference = 0

            for day in current_menu:

                day_kcal = sum(meal.calories for meal in day)

                total_difference += max_calories_per_day - day_kcal

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

            return

        for b_recipe, b_cost, b_cal in breakfast_pool:

            if not (BREAKFAST_RANGE[0] <= b_cal <= BREAKFAST_RANGE[1]):
                stats.prune_calories()
                continue

            b_key = recipe_to_hashable(b_recipe)

            if b_key in used_recipes:
                stats.duplicate()
                continue

            for l_recipe, l_cost, l_cal in lunch_pool:

                if not (LUNCH_RANGE[0] <= l_cal <= LUNCH_RANGE[1]):
                    stats.prune_calories()
                    continue

                l_key = recipe_to_hashable(l_recipe)

                if l_key in used_recipes:
                    stats.duplicate()
                    continue

                for d_recipe, d_cost, d_cal in dinner_pool:

                    if not (DINNER_RANGE[0] <= d_cal <= DINNER_RANGE[1]):
                        stats.prune_calories()
                        continue

                    d_key = recipe_to_hashable(d_recipe)

                    if d_key in used_recipes:
                        stats.duplicate()
                        continue

                    day_kcal = b_cal + l_cal + d_cal

                    if day_kcal > max_calories_per_day:
                        stats.prune_calories()
                        continue

                    day_cost = b_cost + l_cost + d_cost

                    if current_cost + day_cost >= lowest_cost:
                        stats.prune_cost()
                        continue

                    used_recipes.update([b_key, l_key, d_key])

                    day_menu = [

                        Meal("breakfast", b_recipe, b_cal),
                        Meal("lunch", l_recipe, l_cal),
                        Meal("dinner", d_recipe, d_cal),

                    ]

                    current_menu.append(day_menu)

                    backtrack(
                        day_index + 1,
                        current_menu,
                        current_cost + day_cost,
                    )

                    current_menu.pop()

                    used_recipes.difference_update([b_key, l_key, d_key])

    backtrack(0, [], 0)

    stats.print_report()

    return best_menu, lowest_cost, best_difference