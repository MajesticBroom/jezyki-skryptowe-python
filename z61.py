# ------------------------------
# Języki skryptowe -- semestr #3
# Mateusz Gębka (mg321459)
# ------------------------------
# Zadanie 61.
# ------------------------------

class StringOperations:
    def __init__(self, s: str):
        self.s = s

    def reverse_words(self):
        words = []
        for w in self.s.split(" "):
            words.append(w)
        words.reverse()

        return " ".join(words)


so = StringOperations("Jestem studentem. Jestem studentem.")
print(so.reverse_words())