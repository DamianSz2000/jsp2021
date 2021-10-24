import math
#a to stopnie/radany otrzymywane od użytkownika a b to wybór czy chcemy konwertowac na radiany ("r") czy na stopnie ("d")
def konwersja(a,b):
    if b == 'r':
        radiany = a * math.pi / 180
        return radiany
    elif b == 'd':
        stopnie = a * 180 / math.pi
        return stopnie
    else:
        print("Drugi argument powinien okreslac typ konwersji, r dla konwersji na radiany, d dla konwersji na stopnie!")
print("Konwersja na radiany = r, konwersja na stopnie = d")
a = float(input("Podaj liczbe stopni/radianow"))
a = float(input("Podaj typ konwersji(r lub d)"))