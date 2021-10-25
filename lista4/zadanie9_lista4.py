def silnia_oblicz(n):
    silnia = 1
    for _ in range(1,n+1):
        silnia = silnia*_
    return silnia
n = -1
while n <= 0:
    n = int(input("Podaj liczbe dodatnia aby obliczyc silnie: "))
print("Silnia wynosi: ", silnia_oblicz(n))