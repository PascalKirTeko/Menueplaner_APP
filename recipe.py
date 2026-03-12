class Recipe:

    def __init__(self, name, ingredients):
        self.name = name
        self.ingredients = ingredients

    def key(self):
        return tuple(sorted(self.ingredients.items()))

    def __repr__(self):
        return f"Recipe({self.name})"