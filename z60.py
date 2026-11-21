# ------------------------------
# Języki skryptowe -- semestr #3
# Mateusz Gębka (mg321459)
# ------------------------------
# Zadanie 60.
# ------------------------------

import math

class Kolo:
    def __init__(self, radius: float):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)

    # Długość okręgu i obwód koła, to to samo pojęcie
    def circle_length(self):
        return 2 * math.pi * self.radius


kolo = Kolo(20)
print(f"Koło o promieniu: r = {kolo.radius}")
print(f"Pole koła: P = {kolo.area()}")
print(f"Długość okręgu / Obwód koła: L = {kolo.circle_length()}")