# ------------------------------
# Języki skryptowe -- semestr #3
# Mateusz Gębka (mg321459)
# ------------------------------
# Zadanie 21.
# ------------------------------

def fill_table_and_save(sciezka: str, liczba: float):
    wiersze = 7
    kolumny = 5

    with open(sciezka, "w+") as file:
        for _ in range(wiersze):
            wiersz = [str(liczba) for _ in range(kolumny)]
            file.write("  ".join(wiersz) + "\n")

fill_table_and_save("z21_wyjsciezadanie.txt", 3.14)