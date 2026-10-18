# ------------------------------
# Języki skryptowe -- semestr #3
# Mateusz Gębka (mg321459)
# ------------------------------
# Zadanie 34.
# ------------------------------

def create_label(sex, color, size, i):
    with open(f"z34_metki/metka_{i}.txt", "w") as file:
        file.write(f"{sex}\n")
        file.write(f"{color}\n")
        file.write(f"{size}")


def generate_labels():
    sexes = ("Mężczyzna", "Kobieta")
    colors = (
        "biały",
        "czarny",
        "zielony",
        "czerwony",
        "niebieski",
        "żółty",
        "szary"
    )
    sizes = (
        "XXL",
        "XL",
        "L",
        "M",
        "S",
        "XS"
    )

    i = 0
    for sex in sexes:
        for color in colors:
            for size in sizes:
                create_label(sex, color, size, i)
                i += 1

generate_labels()