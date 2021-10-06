import math

print("Podaj a: ")
a = int(input())
print("Podaj b: ")
b = int(input())
print("Podaj kat: ")
alfa = int(input())
print("Pole wynosi: ")
pole = 1 / 2 * a * b * math.sin(math.radians(alfa))
print(pole)
