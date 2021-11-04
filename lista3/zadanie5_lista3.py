import re
haslo = input("Wprowadz haslo aby sprawdzic jego sile: ")

literaS = re.search(r"[a-z]", haslo) is None
literaD = re.search(r"[A-Z]", haslo) is None
literaSp = re.search(r"[#$@]", haslo) is None
literaCyfr = re.search(r"[0-9]", haslo) is None
if literaS == False and literaD == False and literaSp == False and literaCyfr == False and len(haslo) >= 6 and len(haslo) <= 16:
    print("Haslo spelnia wymogi")
else:
    print("Haslo nie spelnia wymogow")