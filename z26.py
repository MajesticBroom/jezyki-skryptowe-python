# ------------------------------
# Języki skryptowe -- semestr #3
# Mateusz Gębka (mg321459)
# ------------------------------
# Zadanie 26.
# ------------------------------

import math

# Funkcje pomocnicze
def add(a: float | int, b: float | int):
    return a + b

def subtract(a: float | int, b: float | int):
    return a - b

# a) Suma sinusów
def sum_of_sines(alpha: float, beta: float, sub: bool = False):
    return 2 * math.sin(
        (add(alpha, beta) if not sub else subtract(alpha, beta)) / 2
    ) * math.cos(
        (subtract(alpha, beta) if not sub else add(alpha, beta)) / 2
    )

print("Suma sinusów:", sum_of_sines(30, 60))


# b) (1 + x)^n
def binominal_series(x: float, n: float, eps: float = 1e-7, max_iter = 1000) -> float:
    total_sum = 1
    term = 1
    k = 1

    while k < max_iter:
        term *= ((n - k - 1) * x) / k
        total_sum += term

        if abs(term) < eps:
            break

        k += 1

    return total_sum

print(binominal_series(0.4, 0.3))


# c) Delta - trójmian kwadratowy
def quadratic_formula(a: float, b: float, c: float):
    delta = (b ** 2) - (4 * a * c)

    if delta < 0:
        return None
    elif delta == 0:
        return -b / (2 * a)
    else:
        return (
            (-b - math.sqrt(delta)) / (2 * a),
            (-b + math.sqrt(delta)) / (2 * a),
        )

print(quadratic_formula(-3, 4, 7))


# d) Szereg Maclaurina - przybliżenie e^x
def exp_approx(x: float, elements_count: int):
    sum = 0
    for n in range(elements_count):
        element = (x ** n) / math.factorial(n)
        sum += element

    return sum

print(exp_approx(2, 1000))


# e) Szereg Fouriera -> oblicza wartość funkcji f rozwiniętej w szereg Fouriera
def fourier_series(x: float, a0: float, L: float, a_n: list[float], b_n: list[float]):
    result = a0

    N = min(len(a_n), len(b_n))

    for i in range(N):
        n = i + 1

        angle = (n * math.pi * x) / L

        result += a_n[i] * math.cos(angle) + b_n[i] * math.sin(angle)

    return result

