# ------------------------------
# Języki skryptowe -- semestr #3
# Mateusz Gębka (mg321459)
# ------------------------------
# Zadanie 30.
# ------------------------------

def wersaliki(text: str) -> str:
    return text.upper()

try:
    with open("z30_tekstdostatystyki.txt") as file:
        text = file.read()
except FileNotFoundError:
    print("Nie znaleziono pliku")

with open("z30_wersaliki.txt", "w+") as write_file:
    write_file.write(wersaliki(text))