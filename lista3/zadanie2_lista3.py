liczba = int(input("Podaj jakas liczbe: "))
if liczba % 2 == 0:
    print("Liczba", liczba, "jest parzysta10", sep=" ")
else:
    print("Liczba", liczba, "jest nieparzysta", sep=" ")

# Ponizej program bez uzycia if

tablica = ['parzysta', 'nieparzysta']
print("Liczba", liczba, "jest", tablica[liczba % 2], sep=" ")
