import math
class Koło:
    def __init__(self, r):
        self.r = r
    def pole(self):
        self.p = math.pi * self.r**2
        return self.p
    def obwod(self):
        self.obw = 2 * math.pi * self.r
        return self.obw

obiekt = Koło(5)
print(obiekt.pole())
print(obiekt.obwod())
