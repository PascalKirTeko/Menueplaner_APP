import pytest
from menueplan import generate_menu
from einkaufsliste import generate_shopping_list
from Zutaten_db import ingredients_db


def test_menu_generation():

    days = 3
    calories = 2000
    vegan = False

    menu, cost, diff = generate_menu(days, calories, vegan)

    assert len(menu) == days

    for day in menu:
        assert len(day) == 3


def test_calories_limit():

    days = 3
    calories = 2000

    menu, cost, diff = generate_menu(days, calories, False)

    for day in menu:
        total = sum(meal.calories for meal in day)
        assert total <= calories * 1.15


def test_shopping_list():

    menu, cost, diff = generate_menu(2, 2000, False)

    shopping = generate_shopping_list(menu)

    assert isinstance(shopping, dict)
    assert len(shopping) > 0


def test_vegan_mode():

    menu, cost, diff = generate_menu(2, 2000, True)

    for day in menu:
        for meal in day:
            for ingredient in meal.recipe.ingredients:

                typ = ingredients_db[ingredient]["type"]

                assert typ not in {"meat", "dairy"}