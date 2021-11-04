roman = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000
}

def roman_to_arabic(x):
    converted_number = 0
    temp = 0
    if (x.count("V") > 1 or x.count("L") > 1 or x.count("D") > 1) or ((x.count("I") > 3 or x.count("X") > 3 or x.count("C") > 3 or x.count("M") > 3)):
        return "Nie mozna powtarzac znakow V L i D! Nie mozna powtarzac znakow I X C i M wiecej niz 3 razy!" 
    else:
        for char in range(len(x)-1, 0, -1):
            if roman[x[char]] <= roman[x[char-1]]:
                converted_number += roman[x[char]]
                print(converted_number)
                if char == 1:
                    converted_number += roman[x[char-1]]
            elif roman[x[char]] >= roman[x[char-1]]:
                converted_number += roman[x[char]] - roman[x[char-1]]
                print(converted_number)
        return converted_number


x = input("Podaj liczbe w formacie rzymskim aby przetworzyc ja na liczbe arabska: ")
print("Liczba po konwersji: ", roman_to_arabic(x))