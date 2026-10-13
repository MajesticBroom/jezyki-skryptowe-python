# ------------------------------
# Języki skryptowe -- semestr #3
# Mateusz Gębka (mg321459)
# ------------------------------
# Zadanie 16.
# ------------------------------

from math import ceil


# Suma
def f_sum(values: list[int]):
    sum = 0
    for number in values:
        sum += number

    return sum

# Średnia arytmetyczna
def f_avg(values: list[int]):
    return f_sum(values) / len(values)

# Mediana
def f_med(values: list[int]):
    values.sort()

    if len(values) % 2 == 1:
        return values[ceil(len(values) / 2) - 1]
    else:
        half_length = int(len(values) / 2)
        return (values[half_length - 1] + values[half_length]) / 2


def do_calculations(values: list[int]):
    sum: int = f_sum(values)

    avg: float = f_avg(values)

    med: float = f_med(values)

    return {
        "Suma": sum,
        "Średnia": avg,
        "Mediana": med
    }


try:
    with open("z16.txt") as f:

        user_values: list[int] = [*map(int, f.read().split("\n"))]
        print(user_values)

        calculations = do_calculations(user_values)
        print("Obliczenia:")
        for el in calculations:
            print(f"{el} = {calculations[el]}")

except FileNotFoundError:
    print("Nie znaleziono pliku.")