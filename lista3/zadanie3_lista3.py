import math

a = int(input("Podaj a: "))
b = int(input("Podaj b: "))
c = int(input("Podaj c: "))
if a == 0: #sprawdzam czy rownanie jest kwadratowe
    print("Podane rownanie nie jest kwadratowe!")
else: #jezeli jest kwadratowe
    print("Twoje rownanie ma postac: ", a, "x^2+", b, "x+", c, "=0", sep="") #wyswietlam postac rownania
    delta = (b**2) - (4*a*c)
    print(delta)
    if delta > 0: #dla delty > 0
        x1 = (-b+math.sqrt(delta))/2*a
        x2 = (-b-math.sqrt(delta))/2*a
        print("Pierwiastki rownania to: ", x1, x2, sep=" ")
    elif delta == 0: #delta 0
        x1 = -b/(2*a)
        print("Pierwiastek rownania to: ", x1, sep=" ")
    elif delta < 0: #delta < 0, w tresci nie ma mowy o liczbach zespolonych dlatego przyjmuje dotychczas znana przezemnie definicje funkcji kwadratowej
        print("Pierwiastki rownania dla liczb rzeczywistych nie istnieja")