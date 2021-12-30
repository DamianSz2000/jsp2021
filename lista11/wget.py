import urllib.request


x = input("Podaj adres strony: ")
nazwa = ""
if(x[-1] == "/"):
    nazwa = "index.html"
else:
    nazwa = x.split("/")
    print(nazwa)
    nazwa = nazwa[-1]

urllib.request.urlretrieve(x, nazwa)



