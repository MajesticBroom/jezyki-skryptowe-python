# ------------------------------
# Języki skryptowe -- semestr #3
# Mateusz Gębka (mg321459)
# ------------------------------
# Zadanie 48.
# ------------------------------

import math

# Pole wielokąta foremnego

def regular_polygon_area(n: int, a: float) -> float:
    """Należy podać ilość kątów i długość boku."""
    return round((1 / 4) * n * (a ** 2) * (1 / math.tan(math.pi / n)), 2)


try:
    n = int(input("Podaj liczbę kątów: "))
    a = float(input("Podaj długość boku: "))

    print(regular_polygon_area(n, a), "[j^2]")
except ValueError as e:
    print("Błędne dane.")
