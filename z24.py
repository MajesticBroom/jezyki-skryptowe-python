# ------------------------------
# Języki skryptowe -- semestr #3
# Mateusz Gębka (mg321459)
# ------------------------------
# Zadanie 24.
# ------------------------------

# Wersja z rekurencją
def factorial_recursion(n: int):
    if n < 0:
        return None

    if n == 0 or n == 1:
        return 1

    return n * factorial_recursion(n - 1)

print("-- Rekurencyjnie --")
print(f"5! = {factorial_recursion(5)}")
print(f"7! = {factorial_recursion(7)}")
print(f"(-2)! = {factorial_recursion(-2)}")

# Wersja z pętlą
def factorial_iteration(n: int):
    if n < 0:
        return None

    wynik = 1

    for i in range(2, n + 1):
        wynik *= i

    return wynik

print("-- Iteracyjnie --")
print(f"5! = {factorial_iteration(5)}")
print(f"7! = {factorial_iteration(7)}")
print(f"(-2)! = {factorial_iteration(-2)}")
