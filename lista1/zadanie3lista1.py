import math

a = float(input("Podaj a: "))
b = float(input("Podaj b: "))
alfa = float(input("Podaj kąt: "))
print("Pole wynosi: ")
pole = 1 / 2 * a * b * math.sin(math.radians(alfa)) #obliczam pole, funkcja math.radians zamienia stopnie na radiany
print(pole) #wyswietlam pole w konsoli
