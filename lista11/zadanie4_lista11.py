#Damian Szmulik 331899 zadanie 4
import re

tekst = input("Podaj tekst: ")
wynik = re.findall(r'a\w+', tekst) #szukamy slow na a
wynik.extend(re.findall(r'e\w+', tekst)) #szukamy slow na e
print("Wyrazy zaczynajace sie na a lub e: ", wynik)