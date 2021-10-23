import cmath
z = complex(input("Podaj liczbe zespolona z: "))
modul = cmath.sqrt(z.real**2 + z.imag**2)

argmain = cmath.phase(z)

print("Liczba zespolona: ", z)
print("Modul liczby zespolonej: ", modul)
print("Liczba sprzezona z: ", z.conjugate())

print("Argumentem glownym liczby zespolonej jest: ", argmain)