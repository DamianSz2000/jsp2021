import cmath
z = complex(input("Podaj liczbe zespolona z: "))
modul = cmath.sqrt(z.real**2 + z.imag**2) #obliczam modul liczby zespolonej uzywajac jej czesci rzeczywistej real i urojonej imag

argmain = cmath.phase(z) #wyznaczam argument liczby zespolonej za pomoca funkcji phase

print("Liczba zespolona: ", z)
print("Modul liczby zespolonej: ", modul)
print("Liczba sprzezona z: ", z.conjugate()) #conjugate zwraca sprzezenie liczby zespolonej

print("Argumentem glownym liczby zespolonej jest: ", argmain)