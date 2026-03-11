# recipe.py

class Recipe:

    def __init__(self, name, ingredients):
        self.name = name
        self.ingredients = ingredients   # dict {ingredient: amount}

    def items(self):
        return self.ingredients.items()

    def __repr__(self):
        return f"Recipe({self.name})"