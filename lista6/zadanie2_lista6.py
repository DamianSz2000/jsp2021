import SzyfrCezara

choice = int(input("Jezeli chcesz zaszyfrowac wyraz podaj 1, jezeli odszyfrowac podaj 2: "))
if(choice == 1):
    key = int(input("Podaj klucz do szyfru cezara(np. 5): "))
    sentence = input("Podaj zdanie do zaszyfrowania: ")
    print("Zaszyfrowane zdanie to: ", SzyfrCezara.encrypt(sentence, key))
elif(choice == 2):
    key = int(input("Podaj klucz do odszyfrowania szyfru cezara(np. 5): "))
    sentence = input("Podaj zdanie do odszyfrowania: ")
    print("Odszyfrowane zdanie to: ", SzyfrCezara.decrypt(sentence, key))