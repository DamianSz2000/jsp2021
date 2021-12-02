import SzyfrCezara
import datetime

choice = int(input("Jezeli chcesz zaszyfrowac wyraz podaj 1, jezeli odszyfrowac podaj 2: "))
path = input("Podaj sciezke do pliku tekstowego ktory chcesz zaszyfrowac lub deszyfrowac: ")
txt = open(path, "r")
check = 0
if(choice == 1):
    while(check == 0):
        key = int(input("Podaj klucz do szyfru cezara(1-10): "))
        if(key > 0 and key < 11):
            check = 1
        else:
            print("Klucz musi miec wartosc od 1 do 10! ")
    sentence = txt.read()
    sentence2 = SzyfrCezara.encrypt(sentence, key)
elif(choice == 2):
    while(check == 0):
        key = int(input("Podaj klucz do szyfru cezara(1-10): "))
        if(key > 0 and key < 11):
            check = 1
        else:
            print("Klucz musi miec wartosc od 1 do 10! ")
    sentence = txt.read()
    sentence2 = SzyfrCezara.decrypt(sentence, key)
txt.close()
path = input("Gdzie zapisac plik z wynikiem? ")
x = datetime.datetime.now()
path += "/plik_zaszyfrowany" + str(key) + "_" + x.strftime("%Y") + "-" + x.strftime("%m") + "-" + x.strftime("%d") + ".txt"
txt = open(path, "w")
txt.write(sentence2)
txt.close()