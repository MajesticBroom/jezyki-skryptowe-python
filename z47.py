# ------------------------------
# Języki skryptowe -- semestr #3
# Mateusz Gębka (mg321459)
# ------------------------------
# Zadanie 47.
# ------------------------------

# Szukanie daty pierwszego poniedziałku w zadanym tygodniu

from datetime import datetime

def find_first_monday(year: int, week: int):
    schema = f"{year}-W{week:02d}-1"

    # Wykorzystujemy formatowanie ISO
    date = datetime.strptime(schema, "%G-W%V-%u")
    # %G -- 2026
    # -W%V -- -Wweek
    # -%u -- -1 (chodzi o poniedziałek, który jest 1 dniem tygodnia w standardzie ISO)

    return date

try:
    year = int(input("Podaj rok: "))
    week = int(input("Podaj tydzień: "))

    print(find_first_monday(year, week))
except ValueError as e:
    print("Błędne dane.")
