napis = input("Podaj jakis napis: ")
srodek = input("Co wstawic w srodek napisu?: ")
napisDl = len(napis) // 2 #okreslam dlugosc polowy napisu
napisCz1 = napis[0:napisDl] #wycinam 1 i nizej druga polowe
napisCz2 = napis[napisDl:]
print(napisCz1 + srodek + napisCz2) #lacze napisy
