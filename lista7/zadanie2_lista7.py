import random
import time
def sortowanie(lista1):
    for i in range(100):
        temp = lista1[i]
        j = i - 1
        while(j >= 0 and lista1[j] > temp):
            lista1[j+1] = lista1[j]
            j = j - 1
        lista1[j+1] = temp
    return lista1
lista1 = []
lista2 = []
lista3 = []
for i in range(100):
    lista1.append(random.randint(0,20))
for i in range(200):
    lista2.append(random.randint(0,20))
for i in range(300):
    lista3.append(random.randint(0,20))
time1 = time.time_ns()
sortowanie(lista1)
time2 = time.time_ns()
print("Sortowanie list 100 elementowej zajelo (w ms): ", (time2-time1)/1000000)
time1 = time.time_ns()
sortowanie(lista2)
time2 = time.time_ns()
print("Sortowanie list 200 elementowej zajelo (w ms): ", (time2-time1)/1000000)
time1 = time.time_ns()
sortowanie(lista3)
time2 = time.time_ns()
print("Sortowanie list 300 elementowej zajelo (w ms): ", (time2-time1)/1000000)
