# ------------------------------
# Języki skryptowe -- semestr #3
# Mateusz Gębka (mg321459)
# ------------------------------
# Zadanie 10.
# ------------------------------

list_a = [
    "Mateusz",
    "Maciej",
    "Gliwice",
    "Mateusz"
]

el = "Mateusz"
if el in list_a:
    print(f"Element \"{el}\" znajduje się w liście A")
    print(f"Liczba wystąpień w liście: {list_a.count(el)}")