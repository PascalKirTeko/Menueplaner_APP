# pdf_export.py

from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet

from Zutaten_db import ingredients_db
from einkaufsliste import generate_shopping_list


def export_menu_pdf(menu, filename="menueplan.pdf"):

    styles = getSampleStyleSheet()
    elements = []

    elements.append(Paragraph("Menüplan", styles['Title']))
    elements.append(Spacer(1, 20))

    meal_names = {
        "breakfast": "Frühstück",
        "lunch": "Mittagessen",
        "dinner": "Abendessen"
    }

    # -------------------------
    # Menü
    # -------------------------

    for i, day in enumerate(menu, 1):

        elements.append(Paragraph(f"Tag {i}", styles['Heading2']))
        elements.append(Spacer(1, 10))

        for meal in day:

            elements.append(
                Paragraph(f"<b>{meal_names[meal.meal_type]}</b>", styles['Normal'])
            )

            elements.append(
                Paragraph(meal.recipe.name, styles['Normal'])
            )

            for ingredient, amount in meal.recipe.ingredients.items():

                unit = ingredients_db[ingredient]["unit"]

                elements.append(
                    Paragraph(f"{ingredient}: {amount}{unit}", styles['Normal'])
                )

            elements.append(
                Paragraph(f"Kalorien: {int(meal.calories)}", styles['Normal'])
            )

            elements.append(Spacer(1, 10))

        elements.append(Spacer(1, 20))

    # -------------------------
    # Einkaufsliste
    # -------------------------

    elements.append(Paragraph("Einkaufsliste", styles['Heading1']))
    elements.append(Spacer(1, 10))

    shopping = generate_shopping_list(menu)

    for ingredient, amount in sorted(shopping.items()):

        unit = ingredients_db[ingredient]["unit"]

        elements.append(
            Paragraph(f"{ingredient}: {amount}{unit}", styles['Normal'])
        )

    doc = SimpleDocTemplate(filename)

    doc.build(elements)

    print(f"\nPDF gespeichert: {filename}")