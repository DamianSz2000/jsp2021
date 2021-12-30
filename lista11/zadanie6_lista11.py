class CiagArytmetyczny:
    def __init__(self, a1, r, n):
        self.a1 = a1
        self.r = r
        self.n = n
    def __iter__(self):
        return self
    def __next__(self):
        if self.n > 0: 
            an = self.a1
            self.a1 += self.r
            self.n -= 1
            return an
        else:
            raise StopIteration
obiekt = CiagArytmetyczny(1, 2, 10)
obiektiter = iter(obiekt)

for x in obiektiter:
    print(x)
        

