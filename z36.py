# ------------------------------
# Języki skryptowe -- semestr #3
# Mateusz Gębka (mg321459)
# ------------------------------
# Zadanie 36.
# ------------------------------

def factorial_rec(n: int) -> int | None:
    if n < 0:
        return None

    if n == 0 or n == 1:
        return 1

    return n * factorial_rec(n - 1)


for i in range(-1, 6):
    if i < 0:
        print(f"({i})! = {factorial_rec(i)}")
    else:
        print(f"{i}! = {factorial_rec(i)}")