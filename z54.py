# ------------------------------
# Języki skryptowe -- semestr #3
# Mateusz Gębka (mg321459)
# ------------------------------
# Zadanie 54.
# ------------------------------
import math


def convert_fraction(x: float) -> str:
    x_str = str(x)
    if "." not in x_str:
        return x_str

    int_part, frac_part = x_str.split(".")

    denominator = "1" + ("0" * len(frac_part))

    gcd = math.gcd(int(frac_part), int(denominator))

    frac_part = str(int(frac_part) // gcd)
    denominator = str(int(denominator) // gcd)

    return f"{int_part + ' ' if int_part != '0' else ''}{frac_part if frac_part != '0' else ''}{'/' + denominator if frac_part != '0' else ''}"


nums = [
    3.2,
    0.5,
    0.42,
    12,
    23.0,
    21.56
]

for n in nums:
    print(f"{n} --> {convert_fraction(n)}")