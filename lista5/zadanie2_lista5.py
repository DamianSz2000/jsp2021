def convert_to_words(x):
    ones = ['One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine']
    tens = ['Ten', 'Eleven', 'Twelve', 'Thirteen', 'Fourteen', 'Fifteen', 'Sixteen', 'Seventeen', 'Eighteen', 'Nineteen']
    tens2 = ['Twenty', 'Thirty', 'Forty', 'Fifty', 'Sixty', 'Seventy', 'Eighty', 'Ninety']
    if x < 10:
        return ones[x-1]
    elif x >= 10 and x < 20:
        return tens[x-10]
    elif x >= 20 and x < 100:
        t = (x % 100) // 10
        o = x % 10
        if o == 0:
            return tens2[t-2]
        elif o > 0:
            return tens2[t-2] + "-" + ones[o-1]
    elif x >= 100 and x < 1000:
        h = (x % 1000) // 100
        t = (x % 100) // 10
        o = x % 10
        if t == 0 and o == 0:
            return ones[h-1] + "-Hundred"
        elif t != 0 and o == 0 and t == 1:
            return ones[h-1] + "-Hundred-" + tens[t-1]
        elif t != 0 and o == 0:
            return ones[h-1] + "-Hundred-" + tens2[t-2]
        elif t != 0 and o != 0 and (x % 100 > 10 and x % 100 < 20):
            return ones[h-1] + "-Hundred-" + tens[(x % 100)-10]
        elif t != 0 and o != 0:
            return ones[h-1] + "-Hundred-" + tens2[t-2] + "-" + ones[o-1]
        elif t == 0 and o != 0:
            return ones[h-1] + "-Hundred-" + ones[o-1]
    elif x >= 1000 and x < 2000:
        h = (x % 1000) // 100
        t = (x % 100) // 10
        o = x % 10
        if h == 0 and t == 0 and o == 0:
            return "One-Thousand"
        elif h == 0 and t == 0 and o != 0:
            return "One-Thousand-" + ones[o-1]
        elif h == 0 and t == 1 and o == 0:
            return "One-Thousand-" + tens[t-1]
        elif h == 0 and t != 0 and o != 0 and (x % 100 > 10 and x % 100 < 20):
            return "One-Thousand-" + tens[(x % 100)-10]
        elif h == 0 and t != 0 and o == 0:
            return "One-Thousand-" + tens2[t-2]
        elif h == 0 and t != 0 and o != 0:
            return "One-Thousand-" + tens2[t-2] + "-" + ones[o-1]
        elif h != 0 and t == 0 and o == 0:
            return "One-Thousand-" + ones[h-1] + "-Hundred"
        elif h != 0 and t != 0 and o == 0 and t == 1:
            return "One-Thousand-" + ones[h-1] + "-Hundred-" + tens[t-1]
        elif h != 0 and t != 0 and o == 0:
            return "One-Thousand-" + ones[h-1] + "-Hundred-" + tens2[t-2]
        elif h != 0 and t != 0 and o != 0 and (x % 100 > 10 and x % 100 < 20):
            return "One-Thousand-" + ones[h-1] + "-Hundred-" + tens[(x % 100)-10]
        elif h != 0 and t != 0 and o != 0:
            return "One-Thousand-" + ones[h-1] + "-Hundred-" + tens2[t-2] + "-" + ones[o-1]
        elif h != 0 and t == 0 and o != 0:
            return "One-Thousand-" + ones[h-1] + "-Hundred-" + ones[o-1]
while 1==1:
    x = int(input("Podaj liczbe od 1 do 1999 aby wyswietlic te liczbe slownie: "))
    print("Liczba: ", convert_to_words(x))

