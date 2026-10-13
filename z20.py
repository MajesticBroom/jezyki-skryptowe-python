# ------------------------------
# Języki skryptowe -- semestr #3
# Mateusz Gębka (mg321459)
# ------------------------------
# Zadanie 20.
# ------------------------------

def fill_table(liczba: float):
    wiersze = 7
    kolumny = 5

    for _ in range(wiersze):
        wiersz = [str(liczba) for _ in range(kolumny)]
        print("  ".join(wiersz))

fill_table(5)
fill_table(3.14)