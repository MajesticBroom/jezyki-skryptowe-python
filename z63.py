# ------------------------------
# Języki skryptowe -- semestr #3
# Mateusz Gębka (mg321459)
# ------------------------------
# Zadanie 63.
# ------------------------------
import math


def absolute_value(a: int | float | complex):
    return (a.real ** 2 + a.imag ** 2) ** 0.5

nums: list[int | float | complex] = [
    32,
    -21,
    13.14,
    -25,32,
    math.e,
    -math.e,
    math.pi,
    -math.pi,
    2 + 4j,
    -3 + 2j,
    10 - 2j,
    -1 - 2j
]

for n in nums:
    print(f"|{n}| = {absolute_value(n)}")