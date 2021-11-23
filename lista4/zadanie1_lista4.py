def suma_el(tab):
    suma = 0
    dl = len(tab)
    for _ in range(0,dl):
        suma = suma + tab[_]
    return suma
def iloczyn_el(tab):
    iloczyn = 1
    dl = len(tab)
    for _ in range(0,dl):
        iloczyn *= tab[_]
    return iloczyn

n = int(input("Podaj ilosc elementow tablicy: "))
print("Podawaj kolejno elementy tablicy: ")
tab = []
for _ in range(0,n):
    elem = int(input())
    tab.append(elem)
print("Suma elementow tablicy wynosi: ", suma_el(tab))
print("Iloczyn elementow tablicy wynosi: ", iloczyn_el(tab))