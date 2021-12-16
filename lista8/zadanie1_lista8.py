#Damian Szmulik zadanie 1
import SzyfrCezara
import datetime
from pathlib import Path
while(True):
    path = input("Podaj sciezke do pliku tekstowego ktory chcesz zaszyfrowac: ")
    try:
        txt = open(path, "r")
        break
    except FileNotFoundError:
        print("Niepoprawna sciezka do pliku.")
key = int(input("Podaj klucz do szyfrowania w zakresie od 1 do 10: "))
while(key not in range(1,11)):
    key = int(input("Podaj klucz do szyfrowania w zakresie od 1 do 10: "))
sentence = txt.read()
sentence = SzyfrCezara.encrypt(sentence, key)
txt.close()
path = input("Gdzie zapisac plik z wynikiem? ")
Path(path).mkdir(parents=True, exist_ok=True)
x = datetime.datetime.now()
path += "/plik_zaszyfrowany" + str(key) + "_" + x.strftime("%Y") + "-" + x.strftime("%m") + "-" + x.strftime("%d") + ".txt"
txt = open(path, "w")
txt.write(sentence)
txt.close()
print("Pomyslnie zapisano w lokalizacji : {}".format(path))
