#Damian Szmulik 331899 zadanie 1
import urllib.request as ul
x = input("Podaj adres strony: ")
try:
    ul.urlopen(x) #próbujemy otworzyc url
    print("Strona istnieje.")
except: #zwracamy komunikat w razie bledu
    print("Nie znaleziono strony.")
