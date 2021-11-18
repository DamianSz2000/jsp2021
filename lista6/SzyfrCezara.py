def encrypt(sentence, key):
    encrypted = []
    for char in sentence:
        if(ord(char) in range(97,123)):
            code_of_char = ord(char)
            code_of_char += key
            if(code_of_char >= 97 and code_of_char <=122):
                encrypted.append(chr(code_of_char))
            elif(code_of_char > 122):
                temporary = code_of_char - 122
                code_of_char = 96 + temporary
                encrypted.append(chr(code_of_char))
        else:
            encrypted.append(char)
    return "".join(encrypted)
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
