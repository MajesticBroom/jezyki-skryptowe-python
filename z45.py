# ------------------------------
# Języki skryptowe -- semestr #3
# Mateusz Gębka (mg321459)
# ------------------------------
# Zadanie 45.
# ------------------------------

# ISO to datetime formatter

from datetime import datetime

string_dates = [
    "2005-03-10T18:20",
    "2026-10-29T20:20"
]
formatted_dates: list[datetime] = []

for s in string_dates:
    datetime_object = datetime.fromisoformat(s)

    formatted_dates.append(datetime_object)

for el in formatted_dates:
    print(f"Data: {el.date()}")
    print(f"Godzina: {el.time()}")
