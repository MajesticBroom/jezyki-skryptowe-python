# ------------------------------
# Języki skryptowe -- semestr #3
# Mateusz Gębka (mg321459)
# ------------------------------
# Zadanie 55.
# ------------------------------

# Generator pseudolosowy

class LCG:
    def __init__(self, m: int, a: int, c: int, seed: int):
        self.seed = seed
        self.c = c
        self.a = a
        self.m = m

    def next(self):
        temp = ((self.a * self.seed) + self.c) % self.m
        self.seed = temp

        return temp

    def generate(self, n: int):
        x = []
        for i in range(n):
            x.append(self.next())

        print("Losowe liczby:")
        for l in x:
            print(l)

# Test na stałych danych (zawsze ten sam wynik, bo generator jest deterministyczny)
lcg = LCG(m=47, a=28, c=8, seed=17)
lcg.generate(5)