"""
a = input()
b = input()

suma = a + b
print(suma)
"""

#Przy podaniu liczb 5 i 5 powyzszy program wskaze ze wynik to 55. Dzieje sie tak dlatego ze input() pobiera od uzytkownika string (ciąg znaków) a nie liczbę
#W takim wypadku nalezy rzutowac typ zmiennej i powinno wygladac to tak
a = int(input("Podaj a: "))
b = int(input("Podaj b: "))

suma = a + b
print("Suma wynosi: ")
print(suma)