# ------------------------------
# Języki skryptowe -- semestr #3
# Mateusz Gębka (mg321459)
# ------------------------------
# Zadanie 8.
# ------------------------------

list_a = [
    "Mateusz",
    21,
    True
]

print("Oryginalna:")
for el in list_a:
    print(f"{el}")

list_a.append("Gębka")
list_a.append(False)
list_a.append(4.22)

print("\nZmodyfikowana:")
for el in list_a:
    print(f"{el}")
