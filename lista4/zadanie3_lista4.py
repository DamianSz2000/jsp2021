import math
#a to stopnie/radiany otrzymywane od użytkownika a b to wybór czy chcemy konwertowac na radiany ("r") czy na stopnie ("d")
def konwersja(a,b):
    if b == "r": #jezeli b to r to przeliczamy a na radiany
        wynik = a * math.pi / 180
    elif b == "d": #jezelie b to d to przeliczamy a na stopnie
        wynik = a * 180 / math.pi
    else:
        print("Drugi argument powinien okreslac typ konwersji, r dla konwersji na radiany, d dla konwersji na stopnie!")
    return wynik


print("Konwersja na radiany = r, konwersja na stopnie = d")
a = float(input("Podaj liczbe stopni/radianow: "))
b = input("Podaj typ konwersji(r lub d): ")
print("Wynik konwersji to: ", konwersja(a,b))
