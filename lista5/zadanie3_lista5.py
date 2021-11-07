def roman_to_arab(roman):
    roman_signs = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }
    converted_number = 0
    length = len(roman)
    i = 0
    while i < length-1:
        if roman_signs[roman[i]] >= roman_signs[roman[i+1]]:
            converted_number += roman_signs[roman[i]]
            i += 1
        elif roman_signs[roman[i]] < roman_signs[roman[i+1]]:
            converted_number += roman_signs[roman[i+1]] - roman_signs[roman[i]]
            i += 2
    if roman_signs[roman[length-1]] <= roman_signs[roman[length-2]]:
        converted_number += roman_signs[roman[length-1]]
        return converted_number
    else:
        return converted_number
roman = input("Podaj liczbe rzymska aby zmienic ja na arabska: ")
if (roman.count("L") > 1 or roman.count("V") > 1 or roman.count("D") > 1) or (roman.count("XXXX") == 1 or roman.count("IIII") == 1 or roman.count("CCCC") == 1 or roman.count("MMMM") == 1):
    print("Litery L, V oraz D nie moga sie powtarzac! Litery M, C, X oraz I nie moga byc obok siebie wiecej niz 3 razy np XXXX jest zapisem blednym!")
else:
    print("Liczba",roman,"w systemie arabskim to",roman_to_arab(roman))