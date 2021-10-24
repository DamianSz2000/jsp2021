import cmath
z = cmath.sqrt(-1) #pierwsiastek z i^2 czyli pierwiastek z -1

print("Czesc rzeczywista sin(z): ", cmath.sin(z).real) #real wyciaga rzecz rzeczywista liczby zespolonej
print("Czesc urojona sin(z): ", cmath.sin(z).imag) #a imag czesc urojona
print("Czesc rzeczywista cos(z): ", cmath.cos(z).real)
print("Czesc urojona cos(z): ", cmath.cos(z).imag)

print("Jedynka trygonometryczna: ", cmath.sin(z)**2+cmath.cos(z)**2)
#Zaleznosc sin(z)^2+cos(z)^2 = 1 jest spelniona