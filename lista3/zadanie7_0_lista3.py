def fibonacci(n):
    if n in {0, 1}:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

N = int(input("Podaj koniec ciagu Fibonacci: "))
x = 0
while fibonacci(x) <= N:
    print(fibonacci(x))
    x = x+1

#Do zadania mozna podejsc na dwojaki sposob. Moj program wypisuje wszystkie elementy ciagu fib. ktore so rowne lub mniejsze wartosci wpisanej przez uzytkownika
#Mozna rowniez brac wartosc uzytkownika jako numer danego elementu i wypisywac N pierwszych elementow ciagu (plik zadanie7_1_lista3.py)