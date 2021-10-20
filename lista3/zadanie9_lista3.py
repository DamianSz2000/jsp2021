m = int(input("Podaj liczbe wierszy: "))
n = int(input("Podaj liczbe kolumn: "))
tablica = [ [0] * n for i in range(m) ] #tworze tablice dwumwymiarowa
for i in range(m):
    for j in range(n):
        tablica[i][j] = i*j

print(tablica)