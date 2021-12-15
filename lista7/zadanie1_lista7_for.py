#Damian Szmulik zadanie 1 petla for
import time
fibonacci = []
time1 = time.time() #czas przed wykonaniem algorytmu
for i in range(100): #algorytm odpowiadajacy za obliczanie 100 kolejnych wyrazów ciągu fibonnaciego
    if(i == 0):
        fibonacci.append(0)
        element1 = 0
    elif(i == 1):
        fibonacci.append(1)
        element2 = 1
    else:
        fibonacci.append(element1+element2) #dodajemy kolejne elementy to listy
        temporary = element2
        element2 += element1
        element1 = temporary
time2 = time.time() #czas po wykonaniu algorytmu
print(fibonacci)
print("Czas dzialania programu: ", (time2-time1)) #obliczam roznice obu czasow

