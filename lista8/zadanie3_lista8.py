#Damian Szmulik zadanie 3
import random
txt = open("PESEL.txt", "w")
for i in range(10):
    rokurodzenia = str(random.randint(1800,2099))
    miesiacurodzenia = str(random.randint(1,12))
    if(int(miesiacurodzenia) in [1,3,5,7,8,10,12]):
        dzienurodzenia = str(random.randint(1,31))
    if(int(miesiacurodzenia) in [4,6,9,11]):
        dzienurodzenia = str(random.randint(1,31))
    if(int(miesiacurodzenia) == 2):
        dzienurodzenia = str(random.randint(1,28))
    plec = str(random.randint(0,9))
    pesel = []
    pesel.append(rokurodzenia[-2:])
    if(len(miesiacurodzenia) == 1):
        miesiacurodzenia = "0" + miesiacurodzenia
    if(int(rokurodzenia) in range(1800,1900)):
        miesiacurodzenia = int(miesiacurodzenia) + 80
        miesiacurodzenia = str(miesiacurodzenia)
    if(int(rokurodzenia) in range(2000,2100)):
        miesiacurodzenia = int(miesiacurodzenia) + 20
        miesiacurodzenia = str(miesiacurodzenia)
    pesel.append(miesiacurodzenia)
    if(len(dzienurodzenia) == 1):
        dzienurodzenia = "0" + dzienurodzenia
    pesel.append(dzienurodzenia)
    nrporzadkowy = str(random.randint(100,999))
    if(len(nrporzadkowy) == 1):
        nrporzadkowy = "0" + nrporzadkowy
    pesel.append(nrporzadkowy)
    pesel.append(plec)
    kontrolna = str(random.randint(0,9))
    pesel.append(kontrolna)
    pesel = "".join(pesel)
    txt.write(pesel + "\n")
txt.close()

