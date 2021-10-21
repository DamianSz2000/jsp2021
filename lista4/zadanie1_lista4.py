def sumaEl(t):
    suma = 0
    dl = len(t)
    for _ in range(0,dl):
        suma = suma + t[_]
    return suma

n = int(input("Podaj ilosc elementow tablicy: "))
print("Podawaj kolejno elementy tablicy: ")
tab = []
for _ in range(0,n):
    elem = int(input())
    tab.append(elem)
print("Suma elementow tablicy wynosi: ", sumaEl(tab))