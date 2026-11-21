# ------------------------------
# Języki skryptowe -- semestr #3
# Mateusz Gębka (mg321459)
# ------------------------------
# Zadanie 58.
# ------------------------------

def int_to_roman(a: int) -> str:

    if a > 3999:
        raise ValueError("Za duża liczba.")

    symbols = [
        ["I", 1],
        ["IV", 4],
        ["V", 5],
        ["IX", 9],
        ["X", 10],
        ["XL", 40],
        ["L", 50],
        ["XC", 90],
        ["C", 100],
        ["CD", 400],
        ["D", 500],
        ["CM", 900],
        ["M", 1000]
    ]

    roman = []

    for sym, val in reversed(symbols):
        if a // val:
            count = a // val
            roman.append(sym * count)
            a = a % val

    return "".join(roman)



numbers = [
    236,
    394,
    12,
    36,
    3999,
    4000,
    4532,
    5324
]

for n in numbers:
    try:
        print(f"{n:4} --> {int_to_roman(n)}")

    except ValueError as e:
        print(f"Błąd: {n} --> {e.args[0]}")