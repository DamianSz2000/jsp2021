import re

tekst = input("Podaj tekst: ")
wynik = re.findall(r'a\w+', tekst)
wynik.extend(re.findall(r'e\w+', tekst))
print("Wyrazy zaczynajace sie na a lub e: ", wynik)