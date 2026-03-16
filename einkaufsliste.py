# einkaufsliste.py

from Zutaten_db import ingredients_db


def generate_shopping_list(menu):

    shopping = {}

    for day in menu:
        for meal in day:
            for ingredient, amount in meal.recipe.ingredients.items():

                if ingredient not in shopping:
                    shopping[ingredient] = 0

                shopping[ingredient] += amount

    return shopping


def print_shopping_list(menu):

    shopping = generate_shopping_list(menu)

    # Kategorien sammeln
    categories = {}

    for ingredient, amount in shopping.items():

        category = ingredients_db[ingredient]["type"]

        if category not in categories:
            categories[category] = []

        categories[category].append((ingredient, amount))

    total_cost = 0

    print("\n==============================")
    print("EINKAUFSLISTE")
    print("==============================")

    for category in sorted(categories):

        print(f"\n--- {category.upper()} ---")

        for ingredient, amount in sorted(categories[category]):

            data = ingredients_db[ingredient]

            unit = data["unit"]
            price = data["price_per_unit"]

            cost = amount * price
            total_cost += cost

            print(f"{ingredient:<15} {amount:>5}{unit}   {cost:>6.2f} CHF")

    print("\n------------------------------")
    print(f"Gesamtkosten Einkauf: {total_cost:.2f} CHF")