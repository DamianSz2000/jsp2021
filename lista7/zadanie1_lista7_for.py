import time
fibonacci = []
time1 = time.time_ns()
for i in range(100):
    if(i == 0):
        fibonacci.append(0)
        element1 = 0
    elif(i == 1):
        fibonacci.append(1)
        element2 = 1
    else:
        fibonacci.append(element1+element2)
        temporary = element2
        element2 += element1
        element1 = temporary
time2 = time.time_ns()
print(fibonacci)
print("Czas dzialania programu w milisekundach: ", (time2-time1)/1000000)

