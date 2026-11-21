# ------------------------------
# Języki skryptowe -- semestr #3
# Mateusz Gębka (mg321459)
# ------------------------------
# Zadanie 64.
# ------------------------------

# Zliczanie samogłosek

def count_vowels(text: str) -> int:
    vowels = "AEIOUÓYĄĘ"
    count = 0
    for l in text:
        if l.upper() in vowels:
            count += 1

    return count

strings = [
    "Mateusz Gębka",
    "Politechnika Śląska",
    "Konstantynopolitańczykowianeczka",
    "Ogórek",
    "Zupa ogórkowa"
]

for s in strings:
    print(f"Liczba samogłosek w ciągu `{s}`: {count_vowels(s)}")