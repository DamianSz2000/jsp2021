import random
import time
def bubble_sort(lista):
    for i in range(len(lista)-1):
        for j in range(len(lista)-1):
            if(lista[j] > lista[j+1]):
                temp = lista[j]
                lista[j] = lista[j+1]
                lista[j+1] = temp
    return lista

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
bubble_sort(lista1)
#print(lista1)
time2 = time.time_ns()
print("Sortowanie list 100 elementowej zajelo (w ms): ", (time2-time1)/1000000)
time1 = time.time_ns()
bubble_sort(lista2)
#print(lista2)
time2 = time.time_ns()
print("Sortowanie list 200 elementowej zajelo (w ms): ", (time2-time1)/1000000)
time1 = time.time_ns()
bubble_sort(lista3)
#print(lista3)
time2 = time.time_ns()
print("Sortowanie list 300 elementowej zajelo (w ms): ", (time2-time1)/1000000)