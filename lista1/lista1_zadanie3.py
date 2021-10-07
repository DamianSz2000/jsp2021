import math

a = int(input("Podaj a: "))
b = int(input("Podaj b: "))
alfa = int(input("Podaj kąt: "))
print("Pole wynosi: ")
pole = 1 / 2 * a * b * math.sin(math.radians(alfa))
print(pole)
