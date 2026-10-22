# ------------------------------
# Języki skryptowe -- semestr #3
# Mateusz Gębka (mg321459)
# ------------------------------
# Zadanie 39.
# ------------------------------

def list_min_max_mean(a: list[int | float]):
    if len(a) <= 1:
        raise ValueError("Przekazana lista jest za krótka.\n")

    a_min = min(a)
    a_max = max(a)

    return (a_min + a_max) / 2

number_lists = [
    [],
    [4],
    [2, 5, 3, 2],
    [-3, 1, 9, 2, 3]
]

for nl in number_lists:
    try:
        print(f"Dla listy: {nl}")
        print(f"Średnia arytmetyczna elementu najmniejszego i największego: {list_min_max_mean(nl)}")
        print("=" * 30, "\n")

    except ValueError as e:
        print(e.args[0])
