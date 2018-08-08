import requests
from bs4 import BeautifulSoup

class BugdayFiyat():
    def AnadoluKirmiziSert(self):
        url = "https://borsa.tobb.org.tr/fiyat_urun3.php?ana_kod=1&alt_kod=808"
        result = requests.get(url)
        soup =  BeautifulSoup(result.content, "lxml")
        liste = soup.findAll("table")[0]
        listetr = liste.findAll("tr")[1]
        listetd = listetr.findAll("td")[0]
        listecenter = listetd.findAll("center")[1]
        listetable = listecenter.findAll("table")[0].findAll("tr")
        print("HUBUBAT - BUĞDAY ANADOLU KIRMIZI SERT (1.DERECE) - KG")
        print("_______________________________________________________")

        for i in listetable:
            print(i.findAll("td")[0].text," - ",i.findAll("td")[3].text )


    def AnadoluBeyazSert(self):
        url = "https://borsa.tobb.org.tr/fiyat_urun3.php?ana_kod=1&alt_kod=835"
        result = requests.get(url)
        soup =  BeautifulSoup(result.content, "lxml")
        liste = soup.findAll("table")[0]
        listetr = liste.findAll("tr")[1]
        listetd = listetr.findAll("td")[0]
        listecenter = listetd.findAll("center")[1]
        listetable = listecenter.findAll("table")[0].findAll("tr")
        print("HUBUBAT - BUĞDAY ANADOLU BEYAZ SERT (1.DERECE) - KG")
        print("_______________________________________________________")

        for i in listetable:
            print(i.findAll("td")[0].text," - ",i.findAll("td")[3].text )

    def Arpa(self):
        url = "https://borsa.tobb.org.tr/fiyat_urun3.php?ana_kod=1&alt_kod=802"
        result = requests.get(url)
        soup =  BeautifulSoup(result.content, "lxml")
        liste = soup.findAll("table")[0]
        listetr = liste.findAll("tr")[1]
        listetd = listetr.findAll("td")[0]
        listecenter = listetd.findAll("center")[1]
        listetable = listecenter.findAll("table")[0].findAll("tr")
        print("HUBUBAT - ARPA BEYAZ (1. GRUP) - KG")
        print("_______________________________________________________")

        for i in listetable:
            print(i.findAll("td")[0].text," - ",i.findAll("td")[3].text )

    def AnadoluBeyazYumsak(self):
            url = "https://borsa.tobb.org.tr/fiyat_urun3.php?ana_kod=1&alt_kod=823"
            result = requests.get(url)
            soup =  BeautifulSoup(result.content, "lxml")
            liste = soup.findAll("table")[0]
            listetr = liste.findAll("tr")[1]
            listetd = listetr.findAll("td")[0]
            listecenter = listetd.findAll("center")[1]
            listetable = listecenter.findAll("table")[0].findAll("tr")
            print("HUBUBAT - BUĞDAY EKMEKLİK BEYAZ YUMUŞAK (1.DERECE) - KG")
            print("_______________________________________________________")

            for i in listetable:
                print(i.findAll("td")[0].text," - ",i.findAll("td")[3].text )
