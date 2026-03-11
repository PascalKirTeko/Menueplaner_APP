# meal.py

class Meal:

    def __init__(self, meal_type, recipe, calories):
        self.meal_type = meal_type
        self.recipe = recipe
        self.calories = calories

    def __repr__(self):
        return f"Meal({self.meal_type}, {self.recipe.name}, {self.calories} kcal)"