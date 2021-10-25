import itertools
def permutacje(lista):
    listap = list(itertools.permutations(lista))
    return listap

lista = []
n = int(input("Podaj ilosc elementow listy: "))
print("Podawaj kolejno elementy listy i zatwierdzaj enter: ")
for _ in range(0,n):
    elem = int(input())
    lista.append(elem)
print("Lista przed dzialaniem funkcji: ", lista)
print("Wszystkie permutacje listy: ",permutacje(lista))
