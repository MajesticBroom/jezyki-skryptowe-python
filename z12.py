# ------------------------------
# Języki skryptowe -- semestr #3
# Mateusz Gębka (mg321459)
# ------------------------------
# Zadanie 12.
# ------------------------------

list_a = []
prompt = "Wprowadź element listy (\"x\" aby zakończyć wprowadzanie): "

while (nowy_element := input(prompt)) != "x":
    list_a.append(nowy_element)

print(*list_a, sep="\n") # inny sposób na wypisanie zawartości listy w osobnych liniach, niż pętla z printami