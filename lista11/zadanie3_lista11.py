#Damian Szmulik 331899 zadanie 3
import re

tekst = input("Podaj tekst do wyszukania adresów url: ")

adresy = re.findall('https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+', tekst) #szukamy adresow w tekscie
print("Znalezione adresy: {}".format(adresy))