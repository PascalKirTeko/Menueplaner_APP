
from Rezepte_db import generate_recipe
from Rezepte_db import calculate_recipe_cost
from Rezepte_db import calculate_recipe_calories
from Rezepte_db import recipe_to_hashable
from Rezepte_db import generate_recipe_pool
from debug_stats import DebugStats
from meal import Meal
import time

# --------------------------------
# Menü generieren
# --------------------------------

def generate_menu(days, max_calories_per_day, vegan_mode):

    start_time = time.perf_counter() #stats
    stats = DebugStats() #stats

    # größere Pools erzeugen und auf Mahlzeiten aufteilen
    breakfast_pool = generate_recipe_pool(30, vegan_mode)
    lunch_pool = generate_recipe_pool(30, vegan_mode)
    dinner_pool = generate_recipe_pool(30, vegan_mode)

    # --------------------------------
    # Dynamische Kalorienbereiche
    # --------------------------------

    #Kalorien nach Mahlzeiten aufteilen mit Toleranz
    breakfast_target = max_calories_per_day * 0.3
    lunch_target = max_calories_per_day * 0.4
    dinner_target = max_calories_per_day * 0.3

    tolerance = max_calories_per_day * 0.2

    #Tupel für Range bei Tageskombinationen
    BREAKFAST_RANGE = (
        breakfast_target - tolerance,
        breakfast_target + tolerance
    )

    LUNCH_RANGE = (
        lunch_target - tolerance,
        lunch_target + tolerance
    )

    DINNER_RANGE = (
        dinner_target - tolerance,
        dinner_target + tolerance
    )

    # --------------------------------
    # Pools nach Zielkalorien sortieren
    # --------------------------------

    #Pool nach nähesten Ergebnissen zu Zielkalorien sortieren
    breakfast_pool.sort(key=lambda x: abs(x[2] - breakfast_target))
    lunch_pool.sort(key=lambda x: abs(x[2] - lunch_target))
    dinner_pool.sort(key=lambda x: abs(x[2] - dinner_target))

    #Beste Kandidaten behalten
    breakfast_pool = breakfast_pool[:8]
    lunch_pool = lunch_pool[:8]
    dinner_pool = dinner_pool[:8]

    best_menu = None
    lowest_cost = float("inf")
    best_difference = float("inf")

    used_recipes = set()
    used_days = set()

    # --------------------------------
    # Tageskombinationen einmal berechnen
    # --------------------------------

    day_combinations = []

    for b_recipe, b_cost, b_cal in breakfast_pool:
        #Verwerfen von zu hohen/tiefen Kalorien
        if not (BREAKFAST_RANGE[0] <= b_cal <= BREAKFAST_RANGE[1]):
            stats.prune_calories() #stats
            continue

        for l_recipe, l_cost, l_cal in lunch_pool:
            if not (LUNCH_RANGE[0] <= l_cal <= LUNCH_RANGE[1]):
                stats.prune_calories() #stats
                continue

            #Früher Kaloriencheck. Wenn Frühstück und Mittagessen zu hoch -> Abbruch
            if b_cal + l_cal > max_calories_per_day * 1.15:
                stats.prune_calories() #stats
                continue

            for d_recipe, d_cost, d_cal in dinner_pool:
                if not (DINNER_RANGE[0] <= d_cal <= DINNER_RANGE[1]):
                    continue

                day_kcal = b_cal + l_cal + d_cal

                if day_kcal > max_calories_per_day * 1.15:
                    stats.prune_calories() #stats
                    continue
                 
                #Gesamtkosten berechnen für 1 Tag       
                day_cost = b_cost + l_cost + d_cost

                #Tagesmenü erstellen mit Rezept und Kalorien
                day_menu = [
                    Meal("breakfast", b_recipe, b_cal),
                    Meal("lunch", l_recipe, l_cal),
                    Meal("dinner", d_recipe, d_cal),
                ]

                #Erstellen Hashes für eindeutige Identifikation
                keys = [
                    recipe_to_hashable(b_recipe),
                    recipe_to_hashable(l_recipe),
                    recipe_to_hashable(d_recipe),
                ]

                day_combinations.append((day_menu, day_cost, keys))

    #Sortieren nach billigste Tage zuerst (Effizienzsteigerung)
    day_combinations.sort(key=lambda x: x[1])
    

    # --------------------------------
    # Backtracking
    # --------------------------------

    def backtrack(day_index, current_menu, current_cost):

        #Zugriff auf globale Variabeln
        nonlocal best_menu, lowest_cost, best_difference

        stats.visit_node() #stats

        #Kosten Bounding. Druchschnittskosten berechnen. Wenn Schlechter -> Abbruch
        if len(current_menu) > 0:
            avg_cost = current_cost / len(current_menu)
            estimated_total = avg_cost * days

            if estimated_total >= lowest_cost:
                stats.prune_cost()
                return
        
        #Wenn keine bessere Lösung -> Abbruch 
        if best_difference == 0:
            return

        #Wenn alle Tage gefüllt -> Abbruch
        if day_index == days:

            stats.valid_day() #stats
        
            total_difference = 0

            #Vergleich Menü zu Zielkalorien
            for day in current_menu:
                day_kcal = sum(meal.calories for meal in day)
                total_difference += abs(max_calories_per_day - day_kcal)

            #Aktuallieren beste Lösung (Prio: Kalorien > Kosten)
            if (
                total_difference < best_difference
                or (
                    total_difference == best_difference
                    and current_cost < lowest_cost
                )
            ):
                #Speichern bestes Menü (Kopie)
                best_menu = [d.copy() for d in current_menu]
                lowest_cost = current_cost
                best_difference = total_difference

                if best_difference == 0:
                    return

            return

        # ------------------------------
        # Tageskombinationen testen
        # ------------------------------


        for day_menu, day_cost, keys in day_combinations:

            #Tages Hash erstellen 
            day_key = tuple(sorted(keys))
            
            #Doppelte Tage verhindern
            if day_key in used_days:
                continue

            #Wenn Kosten zu hoch -> Abbruch
            if current_cost + day_cost >= lowest_cost:
                stats.prune_cost() #stats
                continue

            #Doppelte Rezepte verhindern respektive Wiederholungen verhindern
            if any(key in used_recipes for key in keys):
                stats.duplicate() #stats
                continue

            #Neuen Tag hinzufügen / Aktuallisierung    
            used_days.add(day_key)        
            used_recipes.update(keys)

            current_menu.append(day_menu)

            #Rekursion -> nächster Tag
            backtrack(
                day_index + 1,
                current_menu,
                current_cost + day_cost,
            )

            #Zustand Reset
            current_menu.pop()

            used_recipes.difference_update(keys)
            used_days.remove(day_key)

    backtrack(0, [], 0)

    # --------------------------------
    # Fallback
    # --------------------------------

    if best_menu is None:

        print("Fallback Menü aktiviert")

        best_menu = []

        for _ in range(days):
            b = breakfast_pool[0]
            l = lunch_pool[0]
            d = dinner_pool[0]
            best_menu.append([

                Meal("breakfast", b[0], b[2]),
                Meal("lunch", l[0], l[2]),
                Meal("dinner", d[0], d[2]),
            ])

        lowest_cost = b[1] + l[1] + d[1]
        best_difference = 0

    print(f"\nAlgorithmus-Zeit: {time.perf_counter() - start_time:.3f}s")    
    stats.print_report()
    print("Day combinations:", len(day_combinations)) #stats
    print("Breakfast pool:", len(breakfast_pool)) #stats
    print("Lunch pool:", len(lunch_pool)) #stats
    print("Dinner pool:", len(dinner_pool)) #stats
    

    return best_menu, lowest_cost, best_difference