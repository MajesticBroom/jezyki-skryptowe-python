# ------------------------------
# Języki skryptowe -- semestr #3
# Mateusz Gębka (mg321459)
# ------------------------------
# Zadanie 3.
# ------------------------------

from random import random


def monte_carlo(samples: int) -> float:
    points_inside: int = 0

    for _ in range(samples):
        x = random()
        y = random()

        inside_circle = x**2 + y**2 <= 1

        if inside_circle:
            points_inside += 1

    pi_approx: float = 4 * (points_inside / samples)

    return pi_approx

shots = int(input("Podaj liczbę próbek: "))
print(f"Przybliżenie liczby Pi dla {shots} próbek: {monte_carlo(shots)}")