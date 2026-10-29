# ------------------------------
# Języki skryptowe -- semestr #3
# Mateusz Gębka (mg321459)
# ------------------------------
# Zadanie 44.
# ------------------------------

# Algorytm eliminacji Gaussa

systems = [
    {
        "A": [
            [1, 2, 1],
            [0, 1, 3],
            [2, 1, 1],
        ],
        "b": [
            3,
            1,
            2,
        ]
    },
    {
        "A": [
            [-3, 1, 2],
            [-5, 2, 3],
            [1, -8, 1],
        ],
        "b": [
            4,
            -2,
            3,
        ]
    },
    {
        "A": [
            [2, 1, -1],
            [-3, -1, 2],
            [-2, 1, 2],
        ],
        "b": [
            8,
            -11,
            -3,
        ]
    },
    {
        "A": [
            [2, 1, -1, 4],
            [-3, -1, 2, 6],
            [-1.2, 1, 2, -1],
            [-5, 1, 0.3, -0.5],
        ],
        "b": [
            4,
            -11,
            -3,
            -9
        ]
    },
]

def gaussian_elimination(matrix_A: list[list[float]], vector_b: list[float]) -> list[float]:
    # 1) Łączymy A i b w macierz rozszerzoną
    aug = [A + [b] for A, b in zip(matrix_A, vector_b)] # to tworzy całkowicie nową macierz

    # 2) Eliminacja w przód - potrójna pętla
    n = len(aug) # liczba wierszy

    for i in range(n): # Pętla zewnętrzna (i) wybiera aktualny wiersz roboczy ORAZ kolumnę, którą chcemy wyczyścić.
        max_row = i
        changed = False
        for r in range(i + 1, n):
            # Pętla pomocnicza (r) do sprawdzenia, w którym wierszu, w kolumnie `i`
            # jest największa wartość, co do wartości bezwzględnej.
            if abs(aug[r][i]) > abs(aug[max_row][i]):
                max_row = r # jeśli znajdziemy wartość większą, to zapisujemy jej indeks wiersza
                changed = True
        # Po sprawdzeniu wszystkich wierszy, jeśli coś zostało zamienione, to zamieniamy wiersze,
        # tak żeby największa wartość w tej kolumnie, była pod indeksem `aug[i][i]`.
        if changed:
            aug[i], aug[max_row] = aug[max_row], aug[i]

        for j in range(i + 1, n): # Pętla środkowa (j) wybiera wiersz, który chcemy zmodyfikować (w którym chcemy dostać zero).
            factor = aug[j][i] / aug[i][i] # To jest liczba, przez którą musimy pomnożyć wiersz `i`, żeby dostać 0 na początku.
            for k in range(i, n + 1):
                aug[j][k] = aug[j][k] - (factor * aug[i][k])

    # W tym miejscu mamy macierz aug w postaci schodkowej, czyli zera pod przekątną.

    # 3) Podstawianie wsteczne (od dołu do góry)
    x = [0.0] * n # Inicjujemy wektor odpowiedzi - do x0, x1, x2, ..., będziemy dodawać wartości
    for i in range(n - 1, -1, -1):
        # Zaczynamy od `n - 1`, czyli wiersza z ostatnim indeksem i cofamy się o 1, aż do wiersza 0 włącznie.
        row_sum = 0.0
        for j in range(i + 1, n):
            # Ta pętla przechodzi po kolumnach po prawo od przekątnej do końca
            # i sumuje wartości, wyliczając na koniec x[j], czyli odpowiednią szukaną niewiadomą.
            row_sum += aug[i][j] * x[j] # w pierwszej iteracji x[j] to 0
        x[i] = (aug[i][n] - row_sum) / aug[i][i] # odejmujemy sumę lewej strony od wyrazu wolnego i dzielimy przez liczbę stojącą przy niewiadomej


    return x



for s in systems:
    print(gaussian_elimination(s["A"], s["b"]))
