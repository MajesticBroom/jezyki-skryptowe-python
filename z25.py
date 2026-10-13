# ------------------------------
# Języki skryptowe -- semestr #3
# Mateusz Gębka (mg321459)
# ------------------------------
# Zadanie 25.
# ------------------------------

def get_number(path: str):
    try:
        with open(path) as file:
            number = int(file.readline())
            return number

    except ValueError:
        return None
    except FileNotFoundError:
        return None

def convert_and_save():
    number = get_number("z25_danezadanie.txt")

    number_oct = oct(number)
    number_hex = hex(number)

    with open("z25_liczbykonwertowane.txt", "w+") as result_file:
        result_file.writelines([
            f"Liczba konwertowana: {number}\n",
            f"System oktalny: {number_oct[2:]}\n",
            f"System heksadecymalny: {number_hex[2:].upper()}\n",
        ])

convert_and_save()