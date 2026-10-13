# ------------------------------
# Języki skryptowe -- semestr #3
# Mateusz Gębka (mg321459)
# ------------------------------
# Zadanie 19.
# ------------------------------

import random

def random_from_list():
    try:
        with open("z19_lista.txt") as list_file:
            elements: list[str] = [*map(str, list_file.read().split("\n"))]

            if not elements:
                return None

            return random.choice(elements)
    except FileNotFoundError:
        print("Nie znaleziono pliku.")
        return None

def draw_and_save(a: int, b: int):
    random_list_element = random_from_list()
    if random_list_element is None:
        return


    random_number = random.randrange(a, b)

    with open("z19_wynikzadanie.txt", "w") as result_file:
        result_file.write(f"Losowy element: {random_list_element}\nLosowa liczba: {random_number}")


draw_and_save(4, 19)