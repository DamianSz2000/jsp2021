def dzielnik(a,b):
    if a > b:
        while a > b and b > 0:
            r = a%b
            a = b
            b = r
    else:
        temp = a
        a = b
        b = temp
        while a > b and b > 0:
            r = a%b
            a = b
            b = r
    return a

print("Podaj dwie liczby aby znalezc ich najwiekszy wspolny dzielnik: ")
a = int(input("A: "))
b = int(input("B: "))
print("NWD wynosi: ", dzielnik(a,b))
