# ------------------------------
# Języki skryptowe -- semestr #3
# Mateusz Gębka (mg321459)
# ------------------------------
# Zadanie 32.
# ------------------------------


# Równanie kwadratowe w ciele liczb zespolonych
def solve_complex_quadratic_formula(a: complex, b: complex, c: complex):
    delta = b ** 2 - (4 * a * c)

    delta_sqrt = delta ** 0.5

    x1 = (-b - delta_sqrt) / 2 * a
    x2 = (-b + delta_sqrt) / 2 * a

    return x1, x2

try:
    with open("z32_wspolczynniki.txt") as file:
        coefficients = (complex(el) for el in file.read().splitlines())

        i = 1
        for solution in solve_complex_quadratic_formula(*coefficients):
            print(f"z_{i} = {solution}")
            i += 1

except FileNotFoundError:
    print("Nie znaleziono pliku.")

