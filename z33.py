# ------------------------------
# Języki skryptowe -- semestr #3
# Mateusz Gębka (mg321459)
# ------------------------------
# Zadanie 33.
# ------------------------------

def show_leap_years(from_which: int, to_which: int) -> list[int]:
    result = []
    for i in range(from_which, to_which + 1):
        if (i % 4 == 0 and i % 100 != 0) or i % 400 == 0:
            result.append(i)

    return result

print(show_leap_years(1892, 1920))
print(show_leap_years(1990, 2018))
print(show_leap_years(1582, 1610))