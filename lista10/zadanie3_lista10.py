#Damian Szmulik 331899 zadanie 3
class liczbyrzeczywiste:
    def __init__(self, lista):
        self.lista = lista
        self.lista.sort()
    def suma3(self):
        lista3 = []
        for i in range(0, len(self.lista)-2): #Za pomoca zagniezdzonych petli przechodze wszystkie kombinacje elementow zeby zwrocic tylko odpowiednie trójki
            for j in range(i+1, len(self.lista)-1):
                for k in range(j+1, len(self.lista)):
                    if(self.lista[i] + self.lista[j] + self.lista[k] == 0):
                        lista3.append([self.lista[i], self.lista[j], self.lista[k]])
        return [list(i) for i in set(map(tuple, lista3))]
        


obiekt = liczbyrzeczywiste([-1, 1, 0, 2, 0, -2, 3, 4, 5])
print(obiekt.suma3())

        