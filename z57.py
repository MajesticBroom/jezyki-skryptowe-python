# ------------------------------
# Języki skryptowe -- semestr #3
# Mateusz Gębka (mg321459)
# ------------------------------
# Zadanie 57.
# ------------------------------
import random

try:
    with open("z57_lista.txt") as file:
        list_a = [float(x) for x in file.readlines()]

        print(f"Lista z pliku: {list_a}")
        print(f"Losowy element: {random.choices(list_a)}")

except FileNotFoundError:
    print("Nie znaleziono pliku.")