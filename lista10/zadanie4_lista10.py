import xml.etree.ElementTree as ET

class Kursy:
    def __init__(self, path):
        self.path = path
    def lista(self):
        tree = ET.parse(self.path)
        root = tree.getroot()
        print("Dostępne waluty: ")
        for x in range(2, len(root)):
            print(root[x][0].text)
    def przeliczzpln(self):
        tree = ET.parse(self.path)
        root = tree.getroot()
        waluta = input("Podaj na jaką walutę chcesz przeliczyć PLN: ")
        ilosc = float(input("Podaj kwotę w PLN: "))
        for x in range(2, len(root)):
            if(root[x][0].text == waluta):
                nazwa = root[x][0].text
                kurs = root[x][3].text.replace(",", ".")
                ilosc2 = ilosc * float(root[x][1].text) / float(kurs)
        print("{} zł to {} {}".format(ilosc, ilosc2, nazwa))
    def przeliczwalute(self):
        tree = ET.parse(self.path)
        root = tree.getroot()
        waluta1 = input("Podaj walute z której chcesz przeliczać: ")
        kwota = float(input("Podaj kwotę: "))
        waluta2 = input("Podaj walute na którą chcesz przeliczać: ")
        for x in range(2, len(root)):
            if(root[x][0].text == waluta1):
                nazwa1 = root[x][0].text
                przelicznik1 = float(root[x][1].text)
                kurs1 = float(root[x][3].text.replace(",", "."))
            if(root[x][0].text == waluta2):
                nazwa2 = root[x][0].text
                przelicznik2 = float(root[x][1].text)
                kurs2 = float(root[x][3].text.replace(",", "."))
        waluta1wpln = kwota / float(przelicznik1) * float(kurs1)
        waluta2wtarget = waluta1wpln * float(przelicznik2) / float(kurs2)
        print("{} {} to {} {}".format(kwota, nazwa1, waluta2wtarget, nazwa2))



kursy = Kursy("kursy.xml")
kursy.lista()
kursy.przeliczzpln()
kursy.przeliczwalute()
