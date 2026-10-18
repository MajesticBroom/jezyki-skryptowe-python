# ------------------------------
# Języki skryptowe -- semestr #3
# Mateusz Gębka (mg321459)
# ------------------------------
# Zadanie 37.
# ------------------------------

import re

def links_count(source: str):
    try:
        with open(source) as file:
            text = file.read()

            links = re.findall(f'href=[\'"]([^\'" >]+)', text)

            print(f"Zbadane źródło: {source}")
            print(f"Liczba znalezionych linków: {len(links)}")

    except FileNotFoundError:
        print("Nie znaleziono pliku.")

links_count("z37_strona.html")