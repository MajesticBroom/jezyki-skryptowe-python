# ------------------------------
# Języki skryptowe -- semestr #3
# Mateusz Gębka (mg321459)
# ------------------------------
# Zadanie 17.
# ------------------------------

def get_int() -> int:
    while True:
        try:
            x: int = int(input("Podaj liczbę całkowitą: "))
            break
        except ValueError:
            print("To nie jest liczba całkowita. Spróbuj ponownie.")

    return x

y = get_int()
print(y)