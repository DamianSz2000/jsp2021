liczba = int(input("Podaj jakas liczbe: "))
if liczba % 2 == 0:
    print("Liczba", liczba, "jest parzysta10", sep=" ")
else:
    print("Liczba", liczba, "jest nieparzysta", sep=" ")

# Ponizej program bez uzycia if
print("#"*30,end='\n')

tablica = ['parzysta', 'nieparzysta']
print("Liczba", liczba, "jest", tablica[liczba % 2], sep=" ") #wynikiem %2 zawsze jest 0 lub 1 dzieki czemu iteruje po tablicy parzysta lub nieparzysta
