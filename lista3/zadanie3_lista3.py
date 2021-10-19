import math

a = int(input("Podaj a: "))
b = int(input("Podaj b: "))
c = int(input("Podaj c: "))
if a == 0:
    print("Podane rownanie nie jest kwadratowe!")
else:
    print("Twoje rownanie ma postac: ", a, "x^2+", b, "x+", c, "=0", sep="")
    delta = (b**2) - (4*a*c)
    print(delta)
    if delta > 0:
        x1 = (-b+math.sqrt(delta))/2*a
        x2 = (-b-math.sqrt(delta))/2*a
        print("Pierwiastki rownania to: ", x1, x2, sep=" ")
    elif delta == 0:
        x1 = -b/(2*a)
        print("Pierwiastek rownania to: ", x1, sep=" ")
    elif delta < 0:
        print("Pierwiastki rownania nie istnieja")