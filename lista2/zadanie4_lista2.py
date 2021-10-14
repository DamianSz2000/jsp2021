napis = input("Podaj jakis napis: ")
znak = napis[0]
napisBez1 = napis[1:]
print(znak + napisBez1.replace(znak, "$"))
