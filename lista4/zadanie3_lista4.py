import math
#a to stopnie/radany otrzymywane od użytkownika a b to wybór czy chcemy konwertowac na radiany ("r") czy na stopnie ("d")
def konwersja(a,b):
    if b == "r":
        wynik = a * math.pi / 180
    elif b == "d":
        wynik = a * 180 / math.pi
    else:
        print("Drugi argument powinien okreslac typ konwersji, r dla konwersji na radiany, d dla konwersji na stopnie!")
    return wynik


print("Konwersja na radiany = r, konwersja na stopnie = d")
a = float(input("Podaj liczbe stopni/radianow: "))
b = input("Podaj typ konwersji(r lub d): ")
print("Wynik konwersji to: ", konwersja(a,b))
