#Damian Szmulik 331899 zadanie 2
def encrypt(sentence, key):
    encrypted = [] #tablica na zaszyfrowane zdanie
    for char in sentence: #iteruje po kazdej literze w zdaniu
        if(ord(char) in range(97,123)): #jezeli litera ma kod od 97 do 123
            code_of_char = ord(char) #przypisuje tej zmiennej jej kod
            code_of_char += key #przesuwam kod o klucz
            if(code_of_char >= 97 and code_of_char <=122):
                encrypted.append(chr(code_of_char)) #dodaje zakodowany znak do tablicy z nowym zdaniem
            elif(code_of_char > 122): #jezeli po dodaniu klucza wyjdziemy poza zakres znakow
                temporary = code_of_char - 122 #odejmuje koniec zakresu tak aby przejsc na jego poczatek
                code_of_char = 96 + temporary
                encrypted.append(chr(code_of_char))
        else:
            encrypted.append(char) #dodaje spacje i znaki nie znajdujace sie w zakresie kodu 97-123
    return "".join(encrypted) #zwracam tablice polaczona

#Ponizej proces odwrotny, klucz przesuwamy teraz w lewa strone
def decrypt(sentence, key):
    decrypted = []
    for char in sentence:
        if(ord(char) in range(97,123)):
            code_of_char = ord(char)
            code_of_char -= key
            if(code_of_char >= 97 and code_of_char <=122):
                decrypted.append(chr(code_of_char))
            elif(code_of_char < 97):
                temporary = 97 - code_of_char
                code_of_char = 123 - temporary
                decrypted.append(chr(code_of_char))
        else:
            decrypted.append(char)
    return "".join(decrypted)
