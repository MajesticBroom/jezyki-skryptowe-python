# ------------------------------
# Języki skryptowe -- semestr #3
# Mateusz Gębka (mg321459)
# ------------------------------
# Zadanie 22.
# ------------------------------

import random

def generate_and_save_matrix(path: str, rows: int, cols: int, a: int, b: int):
    with open(path, "w+") as plik:
        for _ in range(rows):
            row = [str(random.randrange(a, b)) for _ in range(cols)]
            plik.write("  ".join(row) + "\n")

generate_and_save_matrix(
    "z22_danewygenerowane.txt",
    4,
    6,
    2,
    29
)