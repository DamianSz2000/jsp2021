import re

tekst = input("Podaj jakis tekst: ")
tekst = re.findall('[A-Z][a-z]*', tekst)

print(" ".join(tekst))