def fibonacci(n):
    if n in {0, 1}:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

N = int(input("Podaj koniec ciagu Fibonacci: "))

for _ in range(0,N):
    print(fibonacci(_))