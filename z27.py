# ------------------------------
# Języki skryptowe -- semestr #3
# Mateusz Gębka (mg321459)
# ------------------------------
# Zadanie 27.
# ------------------------------

def count_letters(text: str, letters: list[str]):
    existing_letters: dict[str, int] = {letter: 0 for letter in letters}

    # text.lower()

    for text_letter in text:
        if text_letter in letters:
            existing_letters[text_letter] += 1

    return existing_letters

try:
    with open("z27_tekstwejsciowy.txt") as file:
        text = file.read()
        letters = count_letters(text, ["g", "r", "a", "w"])

        for letter in letters:
            print(f"Litera {letter}: x{letters[letter]}")

except FileNotFoundError:
    print("Nie znaleziono pliku.")

