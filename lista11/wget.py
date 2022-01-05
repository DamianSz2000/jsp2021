#Damian Szmulik 331899 zadanie 2
import urllib.request


x = input("Podaj adres strony: ")
nazwa = ""
if(x[-1] == "/"): #jezeli ostatnim znakiem adresu jest /
    nazwa = "index.html"
else:
    nazwa = x.split("/") #dzielimy adres na czesci
    print(nazwa)
    nazwa = nazwa[-1] #ostatnia czesc jest nazwa pliku do pobrania

urllib.request.urlretrieve(x, nazwa) #pobieramy plik



