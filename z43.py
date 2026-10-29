# ------------------------------
# Języki skryptowe -- semestr #3
# Mateusz Gębka (mg321459)
# ------------------------------
# Zadanie 43.
# ------------------------------

# Kodowanie Huffmana

class HuffmanNode:
    def __init__(self, prob: int, char: str, left: HuffmanNode = None, right: HuffmanNode = None):
        self.prob = prob
        self.char = char
        self.left = left
        self.right = right
        self.code = ""

    def __str__(self):
        return f"{self.char}-{self.prob}-C:'{self.code}'-L:({self.left})-R:({self.right})"

def calc_probs(text: str):
    """Funkcja pomocnicza do wyliczenia prawdopodobieństw wystąpienia znaków w ciągu."""
    probs = {}
    for char in text:
        # Przy zliczaniu prawdopodobieństwa zależy nam tylko na liczniku ułamka,
        # więc dodajemy 1 przy liczeniu znaków, zamiast 1/len(text)
        if char not in probs.keys():
            probs[char] = 1
        else:
            probs[char] += 1

    # Zwracamy znaki, posortowane nierosnąco względem prawdopodobieństw
    return dict(sorted(probs.items(), key=lambda x: x[1], reverse=True))


def calc_codes(node: HuffmanNode, val="", codes=None):
    # Inicjalizacja słownika kodów przy pierwszym wywołaniu
    if codes is None:
        codes = {}

    # Kod Huffmana dla aktualnego noda
    new_val = val + str(node.code)

    if node.left:
        calc_codes(node.left, val=new_val, codes=codes)

    if node.right:
        calc_codes(node.right, val=new_val, codes=codes)

    if not node.left and not node.right:
        # Przechodzimy rekurencją tak głęboko, aż będziemy na liściu,
        # czyli nie będzie left ani right w danym node.
        # Wtedy przypisujemy kod do danego znaku w codes.
        codes[node.char] = new_val

    return codes


def output_encoded(data, code_table):
    encoded_output = []
    for c in data:
        encoded_output.append(code_table[c])

    return "".join([str(item) for item in encoded_output])


def encode(data):
    chars_with_prob = calc_probs(data)
    chars = chars_with_prob.keys()

    nodes = []

    for char in chars:
        nodes.append(HuffmanNode(chars_with_prob[char], char))

    while len(nodes) > 1:
        nodes = sorted(nodes, key=lambda x : x.prob)

        right = nodes[0]
        left = nodes[1]

        left.code = 0
        right.code = 1

        new_node = HuffmanNode(left.prob + right.prob, left.char + right.char, left, right)

        nodes.remove(left)
        nodes.remove(right)
        nodes.append(new_node)

    huffman_encoding = calc_codes(nodes[0])

    print("Tablica kodów:", huffman_encoding)

    encoded_output = output_encoded(data, huffman_encoding)
    return encoded_output, huffman_encoding

def decode(encoded_text: str, code_table: dict):
    # Musimy odwrócić tablicę kodowania, żeby móc odwołać się do nie po kodzie, a nie znaku.
    reversed_coding_table = {code: char for char, code in code_table.items()}
    result = []
    buffer = ""
    for bit in encoded_text:
        buffer += bit
        if buffer in reversed_coding_table:
            result.append(reversed_coding_table[buffer])
            buffer = ""

    if len(buffer) > 0:
        raise ValueError(f"Niepełny kod na końcu ciągu: {buffer}")

    return "".join(result)


# Przykład użycia:
phrases = (
    "ABBA",
    "MATEUSZ",
    "ELEKTROENERGETYKA",
    "STUDIUJĘ NA KIERUNKU INFORMATYKA",
    "KONSTANTYNOPOLITAŃCZYKOWIANECZKA"
)

for i in range(len(phrases)):
    phrase = phrases[i]
    print(f"Tekst {i + 1}. -- {phrase}")
    encoded, coding = encode(phrase)
    print("Kodowanie:")
    print(f"{phrase} --> {encoded}")

    decoded = decode(encoded, coding)
    print("Dekodowanie:")
    print(f"{encoded} --> {decoded}\n")
