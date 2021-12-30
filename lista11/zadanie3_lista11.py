import re

tekst = input("Podaj tekst do wyszukania adresów url: ")

adresy = re.findall('https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+', tekst)
print("Znalezione adresy: {}".format(adresy))