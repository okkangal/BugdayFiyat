from Veri import BugdayFiyat
from os import system
from sys import exit

fyt = BugdayFiyat()

menu = """
_______________________________________
BUĞDAY ANADOLU KIRMIZI SERT      [1]
BUĞDAY ANADOLU BEYAZ SERT        [2]
BUĞDAY EKMEKLİK BEYAZ YUMUŞAK    [3]
ARPA BEYAZ                       [4]
ÇIKIŞ                            [X]
_______________________________________
"""
print(menu)

while True :
    secim = input("")
    if secim == "1" :
        system("cls")
        print(menu)
        fyt.AnadoluKirmiziSert()
    elif secim == "2" :
        system("cls")
        print(menu)
        fyt.AnadoluBeyazSert()
    elif secim == "3" :
        system("cls")
        print(menu)
        fyt.AnadoluBeyazYumsak()
    elif secim == "4" :
        system("cls")
        print(menu)
        fyt.Arpa()
    elif secim == "x":
        exit()
    else:
        system("cls")
        print(menu)
        print("Lütfen Geçerli Bir Seçim Yapınız...")
