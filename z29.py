# ------------------------------
# Języki skryptowe -- semestr #3
# Mateusz Gębka (mg321459)
# ------------------------------
# Zadanie 29.
# ------------------------------
import string


def text_stats(text: str) -> dict[str, int]:
    stats = {
        "lines_count": 0,
        "words_count": 0,
        "letters_count": 0,
        "punctuation_marks_count": 0
    }

    if not text:
        return stats

    stats["lines_count"] = len(text.splitlines())
    stats["words_count"] = len(text.split())
    stats["letters_count"] = sum(1 for char in text if char.isalpha())
    stats["punctuation_marks_count"] = sum(1 for char in text if char in string.punctuation)

    return stats

def print_text(text: str):
    lines = text.splitlines()
    lines_lengths = [len(line) for line in lines]
    longest_line = max(lines_lengths)

    print("=" * longest_line)
    print(text)
    print("=" * longest_line)


try:
    with open("z29_tekstdostatystyki.txt") as file:
        text = file.read()
        stats = text_stats(text)

        print_text(text)

        if stats:
            for key, value in stats.items():
                print(f"{key}: {value}")
except FileNotFoundError:
    print("Nie znaleziono pliku")