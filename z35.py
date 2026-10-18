# ------------------------------
# Języki skryptowe -- semestr #3
# Mateusz Gębka (mg321459)
# ------------------------------
# Zadanie 35.
# ------------------------------

def factorial_iter(n: int) -> int | None:
    if n < 0:
        return None

    if n == 0 or n == 1:
        return 1

    factorial = 2

    for i in range(3, n + 1):
        factorial *= i

    return factorial


for i in range(-1, 6):
    if i < 0:
        print(f"({i})! = {factorial_iter(i)}")
    else:
        print(f"{i}! = {factorial_iter(i)}")