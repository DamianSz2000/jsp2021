def sumaEl(tab):
    suma = 0
    dl = len(tab)
    for _ in range(0,dl):
        suma = suma + tab[_]
    return suma

n = int(input("Podaj ilosc elementow tablicy: "))
print("Podawaj kolejno elementy tablicy: ")
tab = []
for _ in range(0,n):
    elem = int(input())
    tab.append(elem)
print("Suma elementow tablicy wynosi: ", sumaEl(tab))