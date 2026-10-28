# ------------------------------
# Języki skryptowe -- semestr #3
# Mateusz Gębka (mg321459)
# ------------------------------
# Zadanie 41.
# ------------------------------

# Szyfr Cezara

def caesar_cipher(text: str, shift: int, decode: bool = False):
    text = text.upper()
    result = []

    for l in text:
        if not l.isalpha():
            result.append(l)
            continue

        base = ord("A")

        if not decode:
            new_char_code = ((ord(l) - base + shift) % 26) + base
            result.append(chr(new_char_code))
        else:
            new_char_code = ((ord(l) - base - shift) % 26) + base
            result.append(chr(new_char_code))

    if not decode:
        print("Kodowanie")
    else:
        print("Dekodowanie")

    print(f"{text} -> {''.join(result)}")

# caesar_cipher("abc", 2, False)
# caesar_cipher("jcy", 3, True)

caesar_cipher("spider-man", 5)