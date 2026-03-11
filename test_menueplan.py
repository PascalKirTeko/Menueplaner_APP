# test_menueplan.py

from menueplan import generate_menu


def test_menu_generation():

    days = 3
    calories = 2000
    vegan = True

    menu, cost, diff = generate_menu(days, calories, vegan)

    assert menu is not None
    assert len(menu) == days


def test_meal_structure():

    days = 2
    calories = 2000
    vegan = False

    menu, cost, diff = generate_menu(days, calories, vegan)

    for day in menu:

        assert len(day) == 3

        for meal in day:

            meal_type, recipe, kcal = meal

            assert meal_type in ["breakfast", "lunch", "dinner"]
            assert isinstance(recipe, dict)
            assert kcal > 0


def test_calorie_limit():

    days = 2
    calories = 2000
    vegan = False

    menu, cost, diff = generate_menu(days, calories, vegan)

    for day in menu:

        day_kcal = sum(meal[2] for meal in day)

        assert day_kcal <= calories


def test_cost_positive():

    days = 3
    calories = 2000
    vegan = False

    menu, cost, diff = generate_menu(days, calories, vegan)

    assert cost > 0