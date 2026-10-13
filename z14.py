# ------------------------------
# Języki skryptowe -- semestr #3
# Mateusz Gębka (mg321459)
# ------------------------------
# Zadanie 14.
# ------------------------------

while True:
    try:
        number = float(input("Wprowadź liczbę: "))

        print(f"Wpisana liczba: {number}")

        break
    except ValueError:
        print("To nie jest liczba. Podaj poprawną wartość!\n")