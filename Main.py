# main.py

from menueplan import generate_menu
from Kalorienbedarf import berechne_gesamtbedarf
from Zutaten_db import ingredients_db
from einkaufsliste import print_shopping_list
from pdf_export import export_menu_pdf


def main():

    print("==== Menüplan Generator ====\n")

    while True:
        try:

            days = int(input("Bitte geben Sie die Anzahl Wochentage an, für die das Menü generiert werden soll (1-7): "))

            if 1 <= days <=7:
                break
            else:
                print("Bitte geben Sie einen Wert zwischen 1 und 7 Wochentagen an")
        except ValueError:
            print("Bitte geben Sie eine Zahl für 1 bis 7 Wochentage ein")

    print("\nBitte geben Sie Ihre Ernährungsform an:")
    print("1 - Vegan")
    print("2 - Fleisch erlaubt")

    while True:
        vegan_input = input("Zahl eingeben: ")

        if vegan_input in ["1", "2"]:
            vegan_mode = vegan_input == "1"
            break
        else:
            print("Bitte geben Sie 1 für Vegan oder 2 für Fleisch erlaubt ein.")



    print("\nBitte geben Sie an, ob Sie die Kalorien automatisch berechnen oder manuell eingeben möchten:")
    print("1 - Manuell eingeben")
    print("2 - Automatisch berechnen")

    while True:
        kcal_mode = input("Zahl eingeben: ")

        if kcal_mode in ["1", "2"]:
            break
        else:
            print("Bitte geben Sie 1 für manuell oder 2 für automatisch ein.")

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
    # Menü Ausgabe
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

    # -------------------------------
    # Einkaufsliste Abfrage
    # -------------------------------

    print("\nEinkaufsliste anzeigen?")
    print("1 - Ja")
    print("2 - Nein")

    if input("Zahl eingeben: ") == "1":

        print_shopping_list(menu)

    # -------------------------------
    # PDF Export
    # -------------------------------

    print("\nPDF Export erstellen?")
    print("1 - Ja")
    print("2 - Nein")

    if input("Zahl eingeben: ") == "1":

        export_menu_pdf(menu)


if __name__ == "__main__":
    main()