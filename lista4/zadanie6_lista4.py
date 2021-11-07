def rgb_na_hsv(r, g, b):
    rprim = r/255
    gprim = g/255
    bprim = b/255
    Cmax = max(rprim, gprim, bprim)
    Cmin = min(rprim, gprim, bprim)
    delta = Cmax - Cmin
    if delta == 0:
        h = 0
    elif Cmax == rprim:
        h = 60 * (((gprim - bprim)/delta)%6)
    elif Cmax == gprim:
        h = 60 * (((bprim - rprim)/delta)+2)
    elif Cmax == bprim:
        h = 60 * (((rprim - gprim)/delta)+4)
    if Cmax == 0:
        s = 0
    else:
        s = (delta/Cmax)*100
    v = Cmax*100
    return h, s, v

print("Podawaj wartosci RGB: ")
r = float(input("R: "))
g = float(input("G: "))
b = float(input("B: "))
wynik = rgb_na_hsv(r, g, b)
print("Po konwersji na HSV: ",wynik[0], "°,", wynik[1], "%,", wynik[2], "%,", sep = "")