# ------------------------------
# Języki skryptowe -- semestr #3
# Mateusz Gębka (mg321459)
# ------------------------------
# Zadania 49. - 53.
# ------------------------------
import math

# Liczby zespolone


# 49. Dodawanie
a1 = 2 + 4j
b1 = -9 + 3j
complex_sum = a1 + b1
print(f"Dodawanie: {complex_sum}")

# 50. Mnożenie
a2 = -5 + 1j
b2 = -3 - 2j
complex_factor = a2 * b2
print(f"Mnożenie: {complex_factor}")

# 51. Dzielenie
a3 = 2 + 7j
b3 = -3 - 20j
complex_quotient = a3 / b3
print(f"Dzielenie: {complex_quotient}")

# 52. Moduł
a4 = 4 - 8j
absolute_value = (a4.real ** 2 + a4.imag ** 2) ** 0.5
print(f"Moduł: {absolute_value}")

# 53. Długość łuku
a5 = 3 + 12j
arc = math.atan2(a5.imag, a5.real)
print(f"Długość łuku: {arc}")