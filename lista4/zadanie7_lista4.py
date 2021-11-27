from math import factorial
def wypisz_trojkat(n):
    for i in range(n):
        for j in range(n-i+1):
            print(end=" ")
        for j in range(i+1):
            print(factorial(i)//(factorial(j)*factorial(i-j)), end=" ") #kolejne wyrazy sa obliczane za pomoca symbolu dwumiany newtona gdzie n to numer wiersza trojkata poczawszy od 0 a k to pozycja w rzedzie poczawszy od 0
        print()

n = int(input("Podaj ilosc wierszy trojkata pascala: "))
wypisz_trojkat(n)