import trojkat

print("Podaj kolejno 3 boki trojkata (zatwierdzaj bok enterem): ")
a = float(input())
b = float(input())
c = float(input())
if a+b>c and a+c>b and b+c>a:
    print("Obwod trojkata: ", trojkat.perimeter(a, b, c))
    print("Pole trojkata: ", trojkat.area(a, b, c))
    print("Rodzaj trojkata: ", trojkat.type_of_triangle(a, b, c))
    print("Rodzaj katow trojkata: ", trojkat.type_of_triangle_by_angle(a, b, c))
else:
    print("A, B oraz C w polaczeniu nie moga stworzyc trojkata!")