def usunPowt(t):
    t.sort()
    t = list(dict.fromkeys(t))
    return t

n = int(input("Podaj ilosc elementow tablicy: "))
print("Podawaj kolejno elementy tablicy: ")
tab = []
for _ in range(0,n):
    elem = int(input())
    tab.append(elem)
print("Lista: ", tab)
print("Lista bez powtorzen: ", usunPowt(tab))