# ------------------------------
# Języki skryptowe -- semestr #3
# Mateusz Gębka (mg321459)
# ------------------------------
# Zadanie 28.
# ------------------------------

# Rozwiązywanie układów równań

def solve_system_of_equations(A, b):
    # Metoda wyznaczników
    W = (A[0][0] * A[1][1]) - (A[0][1] * A[1][0])
    if W == 0:
        return None
    else:
        Wx = (b[0] * A[1][1]) - (A[0][1] * b[1])
        Wy = (A[0][0] * b[1]) - (A[1][0] * b[0])

        x = Wx/W
        y = Wy/W

        return x, y

A = [
    [3, 2],
    [2, -1]
]

b = [
    1,
    2
]

print(solve_system_of_equations(A, b))