import urllib.request as ul
x = input("Podaj adres strony: ")
try:
    ul.urlopen(x)
    print("Strona istnieje.")
except:
    print("Nie znaleziono strony.")
