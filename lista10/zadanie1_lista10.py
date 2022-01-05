#Damian Szmulik 331899 zadanie 1
import math
class Koło:
    def __init__(self, r): #inicjalizujemy zmienne klasy
        self.r = r
    def pole(self): #metoda odpowiadajaca za pole
        self.p = math.pi * self.r**2
        return self.p
    def obwod(self): #metoda odpowiadajaca za obwod
        self.obw = 2 * math.pi * self.r
        return self.obw

obiekt = Koło(5)
print(obiekt.pole())
print(obiekt.obwod())
