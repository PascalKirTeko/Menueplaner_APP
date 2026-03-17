def berechne_gesamtbedarf():
    # --- Gewicht ---
    while True:
        try:
            gewicht = float(input("Bitte geben Sie Ihr Gewicht in kg an: "))
            if 0 < gewicht <= 500:
                break
        except ValueError:
            pass
        print("Bitte eine gültige Zahl zwischen 0 und 500 eingeben.")

    # --- Größe ---
    while True:
        try:
            groesse = float(input("Bitte geben Sie Ihre Grösse in cm an: "))
            if 50 <= groesse <= 300:
                break
        except ValueError:
            pass
        print("Bitte eine gültige Größe zwischen 50 und 300 cm eingeben.")

    # --- Alter ---
    while True:
        try:
            alter = int(input("Wie alt sind Sie? (Jahre): "))
            if 0 < alter <= 120:
                break
        except ValueError:
            pass
        print("Bitte ein gültiges Alter zwischen 1 und 120 eingeben.")

    # --- Geschlecht ---
    print("\nBitte geben Sie Ihr Geschlecht an:")
    print("1 - männlich")
    print("2 - weiblich")
    print("3 - sonstige")

    while True:
        geschlecht_input = input("Zahl eingeben: ")
        if geschlecht_input in {"1", "2", "3"}:
            break
        print("Ungültige Eingabe, bitte geben Sie mit 1, 2 oder 3 Ihr Geschlecht an.")

    # --- PAL ---
    print("\nAlltagsaktivität:")
    print("1 - Wenig Aktiv")
    print("2 - Leicht Aktiv")
    print("3 - Normal Aktiv")
    print("4 - Sehr Aktiv")

    while True:
        pal_input = input("Zahl eingeben: ")
        if pal_input in {"1", "2", "3", "4"}:
            break
        print("Ungültige Eingabe, bitte 1, 2, 3 oder 4.")

    pal_dict = {
        "1": 1.2,
        "2": 1.375,
        "3": 1.55,
        "4": 1.725
    }

    pal_factor = pal_dict[pal_input]

    # --- Grundumsatz (Mifflin-St Jeor) ---
    if geschlecht_input == "1":  # männlich
        grundumsatz = 10 * gewicht + 6.25 * groesse - 5 * alter + 5
    elif geschlecht_input == "2": #weiblich
          grundumsatz = 10 * gewicht + 6.25 * groesse - 5 * alter - 161
    else:  #sonstige
        grundumsatz = 10 * gewicht + 6.25 * groesse - 5 * alter - 80
        

    # --- Gesamtbedarf ---
    gesamtbedarf = grundumsatz * pal_factor

    return round(gesamtbedarf)