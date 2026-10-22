# ------------------------------
# Języki skryptowe -- semestr #3
# Mateusz Gębka (mg321459)
# ------------------------------
# Zadanie 38.
# ------------------------------
import random
import time

# Trzy rodzaje sortowania danych

# 1. Sortowanie bąbelkowe
def bubble_sort(data: list):
    for i in range(len(data) - 1):
        for j in range(len(data) - 1 - i):
            if data[j] > data[j + 1]:
                # Python pozwala na zamianę wartości w jednej linii
                data[j], data[j + 1] = data[j + 1], data[j]


# 2. Sortowanie przez wstawianie
def insertion_sort(data: list):
    temp = 0
    for i in range(1, len(data)):
        temp = data[i]
        j = i
        while j > 0 and temp < data[j - 1]:
            data[j] = data[j - 1]
            j -= 1
        data[j] = temp


# Funkcja pomocnicza dla Quicksort
def partitioning_algorithm(data: list, start: int, end: int):
    pivot = data[start]
    p = start
    q = end

    while p != q:
        while p < q and data[q] >= pivot:
            q -= 1

        if p != q:
            data[p] = data[q]
            data[q] = pivot
        else:
            break

        while p < q and data[p] <= pivot:
            p += 1

        if p != q:
            data[q] = data[p]
            data[p] = pivot
        else:
            break

    return p
# 3. Quicksort
def quicksort(data: list, start: int = 0, end: int = None):
    if end is None:
        end = len(data) - 1

    # Warunek zakończenia rekurencji: przedział ma więcej niż 1 element
    if start < end:
        pivot_index = partitioning_algorithm(data, start, end)

        quicksort(data, start, pivot_index - 1)

        quicksort(data, pivot_index + 1, end)

def test_sort(data: list):
    x = data[:]
    print("a) Sortowanie bąbelkowe")
    print(f"Przed: {x}")
    bubble_sort(x)
    print(f"Po: {x}\n")

    x = data[:]
    print("b) Sortowanie przez wstawianie")
    print(f"Przed: {x}")
    insertion_sort(x)
    print(f"Po: {x}\n")

    x = data[:]
    print("c) Sortowanie szybkie")
    print(f"Przed: {x}")
    quicksort(x)
    print(f"Po: {x}\n")

def clear_results_file(path: str):
    with open(path, "w") as result_file:
        pass

def save_results(path: str, data: list, title: str):
    with open(path, "a") as result_file:
        result_file.write(f"{title}:\n")
        data = [str(el) for el in data]
        result_file.write(", ".join(data))
        result_file.write("\n\n")

if __name__ == "__main__":
    try:
        with open("z38_dane.txt") as data_file:
            numbers = [int(el) for el in data_file.readlines()]
            print("=" * 30)
            print("Dane do posortowania:")
            print(numbers)
            print("=" * 30, "\n")

            clear_results_file("z38_posortowane.txt")

            x = numbers[:]
            bubble_sort(x)
            save_results("z38_posortowane.txt", x, "Bubble Sort")

            y = numbers[:]
            insertion_sort(y)
            save_results("z38_posortowane.txt", x, "Insertion Sort")

            z = numbers[:]
            quicksort(z)
            save_results("z38_posortowane.txt", x, "Quicksort")

    except FileNotFoundError:
        print("Nie znaleziono pliku z danymi.")