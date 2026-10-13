# ------------------------------
# Języki skryptowe -- semestr #3
# Mateusz Gębka (mg321459)
# ------------------------------
# Zadanie 18.
# ------------------------------

def get_number_and_check_type():
    x = input("Podaj liczbę: ")

    try:
        int(x)
        return "Liczba całkowita"

    except ValueError:
        # To nie jest liczba całkowita
        pass

    try:
        float(x)
        return "Liczba rzeczywista"

    except ValueError:
        # To nie jest liczba rzeczywista
        pass

    return "Podana wartość nie jest liczbą"



y = get_number_and_check_type()
print(y)