# ------------------------------
# Języki skryptowe -- semestr #3
# Mateusz Gębka (mg321459)
# ------------------------------
# Zadanie 42.
# ------------------------------

import math

# Kodowanie Shannona-Fano

def count_char_probabilities(text: str):
    probs = {}
    for char in text:
        # Przy zliczaniu prawdopodobieństwa zależy nam tylko na liczniku ułamka,
        # więc dodajemy 1 przy liczeniu znaków, zamiast 1/len(text)
        if char not in probs.keys():
            probs[char] =  1
        else:
            probs[char] += 1

    # Zwracamy znaki, posortowane nierosnąco względem prawdopodobieństw
    return sorted(probs.items(), key=lambda x : x[1], reverse=True)


def find_best_split(chars_with_probs: list):
    total_sum = sum(v for _, v in chars_with_probs)
    current_left_sum = 0.0
    current_smallest_diff = math.inf
    best_split_index = None
    for i in range(len(chars_with_probs) - 1):
        current_left_sum += chars_with_probs[i][1]
        right_sum = (total_sum - current_left_sum)
        diff = abs(current_left_sum - right_sum)

        # Szukamy najmniejszej różnicy pomiędzy prawdopodobieństwami podciągów
        if diff < current_smallest_diff:
            current_smallest_diff = diff
            best_split_index = i

    return best_split_index


def slice_char_list(chars_with_probs: list):
    codes = {}

    if len(chars_with_probs) == 1:
        codes[chars_with_probs[0][0]] = ""
        return codes

    split_index = find_best_split(chars_with_probs) + 1

    left_group = chars_with_probs[:split_index]
    right_group = chars_with_probs[split_index:]

    sum_left = sum(v for _, v in left_group)
    sum_right = sum(v for _, v in right_group)

    left_greater = sum_left >= sum_right

    # Indeks "0" otrzymuje zawsze strona, po której
    # prawdopodobieństwo jest większe
    left_prefix = "0" if left_greater else "1"
    right_prefix = "1" if left_greater else "0"

    for char, code in slice_char_list(left_group).items():
        codes[char] = left_prefix + code

    for char, code in slice_char_list(right_group).items():
        codes[char] = right_prefix + code

    return codes


def shannon_fano_encode(text: str):
    chars = count_char_probabilities(text)
    codes = slice_char_list(chars)

    if len(codes) == 1:
        codes = {char: "0" for char in chars}

    encoded_parts = [codes[char] for char in text]
    encoded_text = "".join(encoded_parts)

    return encoded_text, codes


def shannon_fano_decode(text: str, codes: dict[str, str]):
    codes_with_chars = {code: char for char, code in codes.items()}

    result = []
    buffer = ""

    # Przechodzimy bit po bicie, doklejając je do buforu.
    # Jeśli kod w buforze znajduje się w tablicy kodowej,
    # dodajemy daną literę do wynikowego tekstu.
    for bit in text:
        buffer += bit
        if buffer in codes_with_chars:
            result.append(codes_with_chars[buffer])
            buffer = ""

    if buffer:
        raise ValueError(f"Niepełny kod na końcu ciągu: {buffer}")

    return "".join(result)


# Przykład użycia:
phrase = "Hello, World!"
encoded, alphabet = shannon_fano_encode(phrase)
print(f"{phrase} --> {encoded}")
print(f"{encoded} --> {shannon_fano_decode(encoded, alphabet)}")
