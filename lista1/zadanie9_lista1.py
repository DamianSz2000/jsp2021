import math
z = complex(input("Podaj liczbe zespolona z: "))
modul = math.sqrt(z.real**2 + z.imag**2)

arg1 = z.real/modul
arg2 = z.imag/modul
if arg1 >= 0 and arg1 < 2*math.pi:
    argmain = arg1
else:
    argmain = arg2

print("Liczba zespolona: ", z)
print("Modul liczby zespolonej: ", modul)
print("Liczba sprzezona z: ", z.conjugate())

print("Argumentem 1 liczby zespolonej jest: ", arg1)
print("Argumentem 2 liczby zespolonej jest: ", arg2)
print("Argumentem glownym liczby zespolonej jest: ", argmain)