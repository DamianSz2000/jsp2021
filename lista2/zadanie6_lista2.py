lista = ["Kasia", "Basia", "Marek", "Darek"]
listaB = ["Ania", "Basia"]
lista.append("Józek")
lista.extend(listaB)
lista.sort()
print("Czwarty student: ", lista[3])
print("Dwoch pierwszych studentow: ", lista[:2])
print("Dwoch ostatnich studentow: ", lista[-2:])
lista.remove("Basia")
print("Lista uczniow bez Basi: ", lista)
dl = len(lista)
print("Dlugosc list: ", dl)
print("Krotka: ", tuple(lista))