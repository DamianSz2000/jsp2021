"""
a = input()
b = input()

suma = a + b
print(suma)
"""

#Przy podaniu liczb 5 i 5 powyzszy program wskaze ze wynik to 55. Dzieje sie tak dlatego ze input() pobiera od uzytkownika string (ciąg znaków) a nie liczbę
#W takim wypadku nalezy rzutowac typ zmiennej i powinno wygladac to tak
print("Podaj a: ")
a = int(input())
print("Podaj b: ")
b = int(input())

suma = a + b
print("Suma wynosi: ")
print(suma)