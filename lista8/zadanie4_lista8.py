#Damian Szmulik zadanie 4
while(True):
    path = input("Podaj sciezke do pliku tekstowego PESEL: ")
    try:
        txt = open(path, "r")
        break
    except FileNotFoundError:
        print("Niepoprawna sciezka do pliku.")
lines = txt.readlines()
txt = open("PESEL_wyniki.txt", "w")
for line in lines:
    line = line.strip()
    if(int(line[-1]) in range(1,10)):
        miesiacurodzenia = line[2:4]
        rokurodzenia = line[0:2]
        if(int(miesiacurodzenia) in range(1,13)):
            rokurodzenia = 1900 + int(rokurodzenia)
            miesiacurodzenia = line[2:4]
        elif(int(miesiacurodzenia) in range(81,93)):
            rokurodzenia = 1800 + int(rokurodzenia)
            miesiacurodzenia = str(int(line[2:4])-80)
        else:
            rokurodzenia = 2000 + int(rokurodzenia)
            miesiacurodzenia = str(int(line[2:4])-20)
        dzienurodzenia = line[4:6]
        if(int(line[-2]) % 2 == 0):
            plec = "kobieta"
        else:
            plec = "mezczyzna"
        txt.write("nr PESEL:{}\n data urodzenia {}-{}-{};\t plec: {} \n".format(line, dzienurodzenia, miesiacurodzenia, rokurodzenia, plec))
txt.close()