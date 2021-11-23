def usun_powt(t):
    t.sort() #sortuje tablice
    t = list(dict.fromkeys(t)) #tworze z tablicy klucze slownika a poniewaz klucze nie moga sie powtarzac duplikaty zostaja usuniete
    return t

n = int(input("Podaj ilosc elementow tablicy: "))
print("Podawaj kolejno elementy tablicy: ")
tab = []
for _ in range(0,n):
    elem = int(input())
    tab.append(elem)
print("Lista: ", tab)
print("Lista bez powtorzen: ", usun_powt(tab))