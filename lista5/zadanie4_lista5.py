#Zadanie 4 lista 5 Damian Szmulik
#Skorzystalem z wbudowanych funkcji translate maketrans dzieki ktorej zreplacowalem konkretne znaki
def encrypt(sentence):
    sentence = sentence.translate(str.maketrans("aeioy","yioae"))
    return sentence
def decrypt(sentence):
    sentence = sentence.translate(str.maketrans("yioae","aeioy"))
    return sentence

mode = int(input("Wybierz czy chcesz szyfrowac(1) czy deszyfrowac(0): "))
if mode == 1:
    sentence = input("Podaj tekst do zakodowania: ")
    print("Tekst po zakodowaniu: ", encrypt(sentence))
elif mode == 0:
    sentence = input("Podaj tekst do odkodowania: ")
    print("Tekst po zakodowaniu: ", decrypt(sentence))
