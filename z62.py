# ------------------------------
# Języki skryptowe -- semestr #3
# Mateusz Gębka (mg321459)
# ------------------------------
# Zadanie 62.
# ------------------------------

class Math:
    def __init__(self, a: int | float, b: int | float = None):
        self.a = a
        self.b = b
        pass

    def pow(self):
        if self.b is None:
            raise ValueError("Liczba `b` jest niezdefiniowana.")

        return self.a ** self.b

    @staticmethod
    def print_parentheses_if_needed(x: int | float):
        if x < 0:
            return f"({x})"

        return str(x)


nums = [
    (2, 3),
    (-3, 2),
    (-3, 3),
    (-2, -3),
    (2, -3)
]

for p in nums:
    m = Math(p[0], p[1])
    print(f"{m.print_parentheses_if_needed(m.a)}^{m.print_parentheses_if_needed(m.b)} = {m.pow()}")

