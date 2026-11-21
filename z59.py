# ------------------------------
# Języki skryptowe -- semestr #3
# Mateusz Gębka (mg321459)
# ------------------------------
# Zadanie 59.
# ------------------------------

def roman_to_int(a: str) -> int:
    roman = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }

    result = 0
    occurs = 0

    for i in range(len(a)):
        if i == 0:
            occurs = 1
        elif i > 0:
            if a[i] == a[i - 1]:
                occurs += 1
            else:
                occurs = 1

            if occurs == 4:
                raise ValueError("Niepoprawna liczba rzymska.")

        if i + 1 < len(a) and roman[a[i]] < roman[a[i + 1]]:
            result -= roman[a[i]]
        else:
            result += roman[a[i]]

    return result


romans = [
    "XXXII",
    "IX",
    "CDVII",
    "MMM",
    "MMMM",
    "XIIIII"
]

for r in romans:
    try:
        print(f"{r} --> {str(roman_to_int(r)):4}")

    except ValueError as e:
        print(f"Błąd: {r} --> {e.args[0]}")