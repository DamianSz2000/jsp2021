a = list(range(3, 100, 3))
del a[4::3] #nie wiedzialem czy od 5 piatego wlacznie czy nie wiec zaczalem od 5 elementu WLACZNIE
suma = sum(a)
dl = len(a)
print('Tablica po usunieciu co trzeciego elementu zaczynajac od piatego: ', a)
print('Srednia arytmetyczna: ', suma/dl)