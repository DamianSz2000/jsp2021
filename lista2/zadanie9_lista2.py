from itertools import chain

a = [[2, 4, 3], [1, 5, 6], [9], [7, 9, 0]]
b = list(chain.from_iterable(a))  # obnizam stopien zagniezdzenia
print(b)
