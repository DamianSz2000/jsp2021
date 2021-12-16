#Damian Szmulik zadanie 2
import SzyfrCezara
import datetime
from pathlib import Path
import os
while(True):
    path = input("Podaj sciezke do folderu w ktorym znajduja sie zaszyfrowane pliki: ")
    try:
        files = os.listdir(path)
        break
    except FileNotFoundError:
        print("Niepoprawna sciezka do folderu.")
onlyencrypted = [x for x in files if "plik_zaszyfrowany" in x]
path2 = input("W jakim folderze zapisac pliki z wynikami? ")
Path(path2).mkdir(parents=True, exist_ok=True)
path3 = path2
counter = 1
for file in onlyencrypted:
    key = int(file[17])
    txt = open(path+"/"+file, "r")
    sentence = txt.read()
    sentence = SzyfrCezara.decrypt(sentence, key)
    txt.close()
    x = datetime.datetime.now()
    path2 += "/plik_deszyfrowany" + str(key) + "_" + x.strftime("%Y") + "-" + x.strftime("%m") + "-" + x.strftime("%d") + "nr" + str(counter) + ".txt"
    counter += 1
    txt = open(path2, "w")
    txt.write(sentence)
    txt.close()
    path2 = path3
print("Wszystkie pliki zapisane w podanej lokalizacji. ")