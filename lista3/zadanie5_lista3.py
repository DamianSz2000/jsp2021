import re
haslo = input("Wprowadz haslo aby sprawdzic jego sile: ")

literaS = re.search(r"[a-z]", haslo) is None
print(literaS)