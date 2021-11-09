lista = []
for _ in range(100,401):
    a = (_%1000)//100 #liczba setek
    b = (_%100)//10 #dziesiatek
    c = _%10 #jednosci
    if a%2 == 0 and b%2 == 0 and c%2 == 0: #sprawdzam czy kazda z cyfr jest parzysta, jezeli tak dodaje ja do listy
        lista.append(_)
print(lista)