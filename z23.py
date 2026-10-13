# ------------------------------
# Języki skryptowe -- semestr #3
# Mateusz Gębka (mg321459)
# ------------------------------
# Zadanie 23.
# ------------------------------

from math import floor


def is_palindrome(text: str):

    text = text.replace(" ", "").lower()
    print(text)

    check_count = floor(len(text) / 2)

    for i in range(check_count):
        lewa = text[i]
        prawa = text[len(text) - i - 1]
        if lewa != prawa:
            return False

    return True


print(is_palindrome("kajak"))
print(is_palindrome("Kamil Ślimak"))
print(is_palindrome("kapusta"))
print(is_palindrome("saippuakivikauppias"))
