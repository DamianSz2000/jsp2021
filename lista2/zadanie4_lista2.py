napis = input("Podaj jakis napis: ")
znak = napis[0] #biore pierwszy znak napisu
napisBez1 = napis[1:] #biore wszystko oprocz 1 znaku napisu
print(znak + napisBez1.replace(znak, "$")) #wyswietlam nowy napis zlozony z pierwszego znaku + reszte napisu z podmienionym znakiem na $
