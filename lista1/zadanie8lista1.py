a = float(input('Podaj a: '))
b = float(input('Podaj b: '))
if b < a: #sprawdzam czy b jest mniejsze od a
    Z = b % a #reszta z dzielenia
    Z *= Z + 3
    print(Z)
else: #jezeli b nie jest mniejsze od a wyswietlam stosowny komunikat
    print("B musi byc mniejsze od a!")
