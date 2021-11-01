def convert_to_number(x):
    numbers = {
        "One": 1,
        "Two": 2,
        "Three": 3,
        "Four": 4,
        "Five": 5,
        "Six": 6,
        "Seven": 7,
        "Eight": 8,
        "Nine": 9,
        "Ten": 10,
        "Eleven": 11,
        "Twelve": 12,
        "Thirteen": 13,
        "Fourteen": 14,
        "Fiveteen": 15,
        "Sixteen": 16,
        "Seventeen": 17,
        "Eighteen": 18,
        "Nineteen": 19,
        "Twenty": 20,
        "Thirty": 30,
        "Forty": 40,
        "Fifty": 50,
    }
    if x.__contains__("Twenty") and len(x) > 6:
        words = x.split("-")
        return numbers[words[0]] + numbers[words[1]]
    elif x.__contains__("Thirty") and len(x) > 6:
        words = x.split("-")
        return numbers[words[0]] + numbers[words[1]]
    elif x.__contains__("Forty") and len(x) > 5:
        words = x.split("-")
        return numbers[words[0]] + numbers[words[1]]
    elif x.__contains__("Fifty") and len(x) > 5:
        words = x.split("-")
        return numbers[words[0]] + numbers[words[1]]
    return numbers[x]


x = input("Podaj slownie liczbe od 1 do 59 aby zamienic ja na liczbe np(One albo Twenty-Five): ")
print("Liczba zamieniona na tekst: ", convert_to_number(x))
