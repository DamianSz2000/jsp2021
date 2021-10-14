napis = input("Podaj jakis napis: ")
srodek = input("Co wstawic w srodek napisu?: ")
napisDl = len(napis)//2
napisCz1 = napis[0:napisDl]
napisCz2 = napis[napisDl:]
print(napisCz1 + srodek + napisCz2)
