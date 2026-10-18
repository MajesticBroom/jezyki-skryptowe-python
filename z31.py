# ------------------------------
# Języki skryptowe -- semestr #3
# Mateusz Gębka (mg321459)
# ------------------------------
# Zadanie 31.
# ------------------------------

def save_stats(result_file, base, iterations):
    with open(result_file, "w") as file:
        file.write("licznik\tsuma\n")
        file.write("**0**\t**0**\n")
        file.write("-----\t-----\n")

        sum = 0

        for i in range(1, iterations + 1):
            sum += base

            line = f"**{i}** | **{sum}**\n"
            file.write(line)

save_stats("z31_wynik.txt", -4, 10)