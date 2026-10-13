# ------------------------------
# Języki skryptowe -- semestr #3
# Mateusz Gębka (mg321459)
# ------------------------------
# Zadanie 13.
# ------------------------------

samogloski = (
    "a",
    "e",
    "i",
    "o",
    "u",
    "ó",
    "y",
    "ą",
    "ę"
)

def licz_i_zwroc_samogloski(wyrazenie: str):
    wystepujace_samogloski = {}

    for znak in wyrazenie.lower():
        if znak in samogloski:
            if znak not in wystepujace_samogloski.keys():
                wystepujace_samogloski[znak] = 1
            else:
                wystepujace_samogloski[znak] += 1

    return wystepujace_samogloski


slowa_do_testu = (
    "Mateusz",
    "kserokopiarka",
    "dwudziestopięciotysięcznik"
)

for slowo in slowa_do_testu:
    print(f"Słowo: {slowo}")
    wystepujace_samogloski = licz_i_zwroc_samogloski(slowo)
    for samogloska in wystepujace_samogloski:
        print(f"{samogloska} -> {wystepujace_samogloski[samogloska]}")
