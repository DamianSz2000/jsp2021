from statistics import mean
a = list(range(3, 100, 3))
print("Tablica poczatkowa: ", a)
del a[4::3] #nie wiedzialem czy od 5 piatego wlacznie czy nie wiec zaczalem od 5 elementu WLACZNIE
print('Tablica po usunieciu co trzeciego elementu zaczynajac od piatego: ', a)
suma = sum(a)
dl = len(a)
print('Srednia arytmetyczna: ', suma/dl)