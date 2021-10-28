def zamien_na_liczbe(x):
    liczby = {
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
        wyrazy = x.split("-")
        return liczby[wyrazy[0]] + liczby[wyrazy[1]]
    elif x.__contains__("Thirty") and len(x) > 6:
        wyrazy = x.split("-")
        return liczby[wyrazy[0]] + liczby[wyrazy[1]]
    elif x.__contains__("Forty") and len(x) > 5:
        wyrazy = x.split("-")
        return liczby[wyrazy[0]] + liczby[wyrazy[1]]
    elif x.__contains__("Fifty") and len(x) > 5:
        wyrazy = x.split("-")
        return liczby[wyrazy[0]] + liczby[wyrazy[1]]
    return liczby[x]


x = input("Podaj slownie liczbe od 1 do 59 aby zamienic ja na liczbe np(One albo Twenty-Five): ")
print("Liczba zamieniona na tekst: ", zamien_na_liczbe(x))
