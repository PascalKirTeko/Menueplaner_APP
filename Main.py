# main.py

from menueplan import generate_menu
from Kalorienbedarf import berechne_gesamtbedarf
from Zutaten_db import ingredients_db


def main():

    print("==== Menüplan Generator ====\n")

    days = int(input("Anzahl Wochentage (1-7): "))

    print("\nErnährungsform:")
    print("1 - Vegan")
    print("2 - Fleisch erlaubt")

    vegan_mode = input("Zahl eingeben: ") == "1"

    print("\nKalorien:")
    print("1 - Manuell eingeben")
    print("2 - Automatisch berechnen")

    kcal_mode = input("Zahl eingeben: ")

    if kcal_mode == "1":
        max_calories = float(input("Max Kalorien pro Tag: "))
    else:
        max_calories = berechne_gesamtbedarf()

    print("\nMenü wird berechnet...\n")

    menu, cost, difference = generate_menu(days, max_calories, vegan_mode)

    meal_names = {
        "breakfast": "Frühstück",
        "lunch": "Mittagessen",
        "dinner": "Abendessen"
    }

    # -------------------------------
    # Strukturprüfung
    # -------------------------------

    for day in menu:
        assert len(day) == 3, "Ein Tag muss 3 Mahlzeiten haben"

        for meal in day:
            assert hasattr(meal, "meal_type")
            assert hasattr(meal, "recipe")
            assert hasattr(meal, "calories")

    # -------------------------------
    # Ausgabe
    # -------------------------------

    for i, day in enumerate(menu, 1):

        print("\n==============================")
        print(f"Tag {i}")
        print("==============================")

        day_calories = 0

        for meal in day:

            print(f"\n{meal_names[meal.meal_type]}")
            print(meal.recipe.name)

            for ingredient, amount in meal.recipe.ingredients.items():

                unit = ingredients_db[ingredient]["unit"]

                print(f"{ingredient:<15} {amount}{unit}")

            print(f"Kalorien: {meal.calories:.0f}")

            day_calories += meal.calories

        print("\n----- Tagesübersicht -----")
        print("Kalorien:", int(day_calories))

    print("\nGesamtkosten:", round(cost, 2), "CHF")


if __name__ == "__main__":
    main()