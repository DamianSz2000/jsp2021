import matplotlib.pyplot as plt
import numpy as np
import math

v0 = float(input("Podaj predkosc poczatkowa: "))
kat = float(input("Podaj kat: "))

v0x = v0 * math.cos(math.radians((kat)))
v0y = v0 * math.sin(math.radians((kat)))

g = 9.81

hmax = (v0y**2)/(2*g)
zasieg = (2*(v0**2)*math.sin(math.radians((kat)))*math.cos(math.radians((kat))))/g
czaslotu = (2*v0y)/g
print("Maksymalna wysokosc na jaka wzniesie sie cialo wynosi: {}".format(hmax))
print("Zasieg rzutu: {}".format(zasieg))
print("Czas lotu: {}".format(czaslotu))

x = np.linspace(0, zasieg, 100)
t = np.linspace(0, czaslotu, 100)
y = []

for i in t:
    y.append((v0y*i)-(g/2)*i**2)

y = np.array(y)
vy = v0 * math.sin(math.radians(kat)) - g * t
vy = np.array(vy)
vx = np.linspace(v0x, v0x, 100)

plt.subplot(4, 1, 1)
plt.plot(x, y)

plt.title("Wykres toru rzutu ukosnego")
plt.xlabel("Dystans")
plt.ylabel("Wysokosc")

plt.subplot(4, 1, 2)
plt.plot(t, x)

plt.title("Polozenie w funkcji czasu")
plt.xlabel("Czas")
plt.ylabel("Polozenie")

plt.subplot(4, 1, 3)
plt.plot(t, vx)

plt.title("Vx po czasie")
plt.xlabel("Czas")
plt.ylabel("Vx")

plt.subplot(4, 1, 4)
plt.plot(t, vy)

plt.title("Vy po czasie")
plt.xlabel("Czas")
plt.ylabel("Vy")



plt.show()
