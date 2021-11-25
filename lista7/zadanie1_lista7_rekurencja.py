import time
time1 = time.time_ns()
def fibonacci(n):
    if n in {0, 1}:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

n = int(input("Podaj ilosc wyrazow ciagu fibonnaciego: "))
fibonacci_e = [fibonacci(n) for n in range(n)]
time2 = time.time_ns()
print(fibonacci_e)
print("Czas dzialania programu w milisekundach: ", (time2-time1)/1000000)