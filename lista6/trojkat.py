import math
def perimeter(a, b, c):
    return a+b+c
def area(a, b, c):
    p = (a+b+c)/2
    square_area = (p*(p-a)*(p-b)*(p-c))**(1/2)
    return square_area
def type_of_triangle(a, b, c):
    if a == b and b == c and c == a:
        return "trojkat rownoboczny"
    elif a != b and b !=c and c != a:
        return "trojkat roznoboczny"
    elif a == b or b == c or c == a:
        return "trojkat rownoramienny"
def type_of_triangle_by_angle(a, b, c):
    maximum = max(a, b, c)
    if maximum == c:
        if a**2 + b**2 == c**2:
            return "trojkat prostokatny"
        elif a**2 + b**2 < c**2:
            return "trojkat rozwartokatny"
        elif a**2 + b**2 > c**2:
            return "trojkat ostrokatny"
    elif maximum == a:
        if c**2 + b**2 == a**2:
            return "trojkat prostokatny"
        elif c**2 + b**2 < a**2:
            return "trojkat rozwartokatny"
        elif c**2 + b**2 > a**2:
            return "trojkat ostrokatny"
    elif maximum == b:
        if a**2 + c**2 == b**2:
            return "trojkat prostokatny"
        elif a**2 + c**2 < b**2:
            return "trojkat rozwartokatny"
        elif a**2 + c**2 > b**2:
            return "trojkat ostrokatny"