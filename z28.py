# ------------------------------
# Języki skryptowe -- semestr #3
# Mateusz Gębka (mg321459)
# ------------------------------
# Zadanie 28.
# ------------------------------

# Rozwiązywanie układów równań

def solve_system_of_equations(A, b):
    # Eliminacja Gaussa
    n = len(b)

    extended_matrix: list[list[float]] = []
    for i in range(n):
        extended_matrix.append(A[i].copy() + [b[i]])


    # Przechodzimy po wszystkich wierszach
    for i in range(n):
        max_value_row = i
        max_val = abs(extended_matrix[i][i]) # zaznaczamy element na przekątnej, bo interesują nas elementy po nią

        # sprawdzamy wartości od max_val w dół
        for k in range(i + 1, n): # n + 1, bo nie sprawdzamy siebie
            if abs(extended_matrix[k][i]) > max_val:
                max_val = abs(extended_matrix[k][i])
                max_value_row = k # jeśli niżej znajdziemy większą wartość, to zapisujemy, w którym to wierszu

        # jeśli znaleziono większą wartość od początkowej, zamieniamy wiersze
        if max_value_row != i:
            extended_matrix[i], extended_matrix[max_value_row] = extended_matrix[max_value_row].copy(), extended_matrix[i].copy()

        pivot_element = extended_matrix[i][i]

        try:
            if abs(pivot_element) < 1e-12:
                raise ValueError("Układ nie ma jednoznaczego rozwiązania.")
        except ValueError:
            print("Układ nie ma jednoznaczego rozwiązania.")
            return None

        # doprowadzamy do 1 na przekątnej
        for col in range(i, len(extended_matrix[i])):
            extended_matrix[i][col] /= pivot_element

        # eliminujemy elementy niżej do 0
        for j in range(i + 1, n):
            factor = extended_matrix[j][i]
            for col in range(i, len(extended_matrix[i])):
                extended_matrix[j][col] = extended_matrix[j][col] - factor * extended_matrix[i][col]


    # print(extended_matrix)

    results: list[float] = [0.0] * n
    for i in range(n - 1, -1, -1):
        results[i] = extended_matrix[i][-1]
        for j in range(i + 1, n):
            results[i] = results[i] - extended_matrix[i][j] * results[j]

    return results


# A = [
#     [3, -1, -1],
#     [1, 1, 0],
#     [2, 0, -3]
# ]
#
# b = [
#     5,
#     0,
#     2
# ]

# A = [
#     [5, 1, 1],
#     [3, 2, 2],
#     [1, 3, 3]
# ]
#
# b = [
#     15,
#     10,
#     5
# ]

# A = [
#     [2, 1, -1],
#     [-3, -1, 2],
#     [-2, 1, 2]
# ]
#
# b = [
#     8,
#     -11,
#     -3
# ]

A = [
    [2, 1],
    [1, 2]
]

b = [
    3,
    2
]

print(solve_system_of_equations(A, b))