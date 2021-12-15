#Damian Szmulik zadanie 1 rekurencja
import time

def fibonacci(n): #algorytm rekurencyjny obliczjacy wyrazy ciagu fib
    if n in {0, 1}:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

n = int(input("Podaj ilosc wyrazow ciagu fibonnaciego: "))
time1 = time.time()
fibonacci_e = [fibonacci(n) for n in range(n)] #tworze liste zlozona z kolejnych wyrazow ciagu
time2 = time.time()
print(fibonacci_e)
print("Czas dzialania programu: ", (time2-time1)) #podaje czas dzialania programu