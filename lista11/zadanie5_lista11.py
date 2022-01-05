#Damian Szmulik 331899 zadanie 5
import re

tekst = input("Podaj jakis tekst: ")
tekst = re.findall('[A-Z][a-z]*', tekst) #Dzielimy tekst na pojedyncze slowa

print(" ".join(tekst)) #Laczymy tablice za pomoca spacji