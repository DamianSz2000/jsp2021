import numpy as np
import sys

dane = []
for element in sys.argv:
    if element.isdigit():
        dane.append(element)
dane = np.array(dane).astype(np.float64)
plik = open(sys.argv[1])
lines = plik.readlines()
print(lines)
