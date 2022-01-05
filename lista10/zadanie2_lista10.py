#Damian Szmulik 331899 zadanie 2
import itertools
class podlisty:
    def __init__(self, lista1):
        self.lista1 = lista1
    def zwrotpodlist(self):
        self.lista2 = []
        for r in range(0, len(self.lista1)+1):
            for podlista in itertools.combinations(self.lista1, r):
                self.lista2.append(list(podlista))
        return self.lista2

obiekt = podlisty([1,2,3])
print(obiekt.zwrotpodlist())


