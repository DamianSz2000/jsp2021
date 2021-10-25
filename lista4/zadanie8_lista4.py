def szereg(n):
    if n == 1:
        return n
    else:
        return 1/n

N = int(input("Podaj ilosc wyrazow szeregu: "))
szeregh = []
x = 1
while x <= N:
    szeregh.append(szereg(x))
    x = x+1
print("Suma szeregu pierwszych",N,"wyrazow wynosi: ", sum(szeregh))
