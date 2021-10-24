import math

a = float(input("Podaj a: "))
b = float(input("Podaj b: "))
alfa = float(input("Podaj kąt: "))
print("Pole wynosi: ")
pole = 1 / 2 * a * b * math.sin(math.radians(alfa))
print(pole)
