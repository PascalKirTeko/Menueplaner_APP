# debug_stats.py

class DebugStats:

    def __init__(self):
        self.nodes_visited = 0
        self.valid_days = 0
        self.pruned_cost = 0
        self.pruned_calories = 0
        self.duplicate_recipes = 0

    def visit_node(self):
        self.nodes_visited += 1

    def valid_day(self):
        self.valid_days += 1

    def prune_cost(self):
        self.pruned_cost += 1

    def prune_calories(self):
        self.pruned_calories += 1

    def duplicate(self):
        self.duplicate_recipes += 1

    def print_report(self):

        print("\n========== DEBUG REPORT ==========")
        print("Besuchte Knoten:", self.nodes_visited)
        print("Gültige Tagesmenüs:", self.valid_days)
        print("Pruning (Kosten):", self.pruned_cost)
        print("Pruning (Kalorien):", self.pruned_calories)
        print("Verworfene Duplikate:", self.duplicate_recipes)
        print("==================================\n")