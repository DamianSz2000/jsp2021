import numpy as np
import sys
dane2 = []
if(".txt" in sys.argv[1]):
    plik1 = open(sys.argv[1], encoding="utf-16")
    dane = plik1.read().splitlines()
    for line in dane:
        dane2.append(int(line))
    plik1.close()
else:
    dane2 = []
    for i in range(1, len(sys.argv)):
        dane2.append(int(sys.argv[i]))
dane2 = np.array(dane2)
print("Wartosc srednia: ", np.average(dane2))
print("Wariancja: ", np.var(dane2))
print("Odchylenie standardowe: ", np.std(dane2))



