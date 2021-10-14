import cmath
z = cmath.sqrt(-1)

print("Czesc rzeczywista sin(z): ", cmath.sin(z).real)
print("Czesc urojona sin(z): ", cmath.sin(z).imag)
print("Czesc rzeczywista cos(z): ", cmath.cos(z).real)
print("Czesc urojona cos(z): ", cmath.cos(z).imag)

#czesc rzeczywista wynosi 0
print("Jedynka trygonometryczna: ", cmath.sin(z)**2+cmath.cos(z)**2)
#Zaleznosc sin(z)^2+cos(z)^2 = 1 jest spelniona