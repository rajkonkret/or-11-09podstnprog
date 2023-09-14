class Dom:
    """
    klasa opisująca Dom
    """

    def __init__(self, metraz, kolor, liczba_okien):  # konstruktor
        self.__metraz = metraz
        self.__kolor = kolor
        self.__liczba_okien = liczba_okien

    # zmienic pola na prywatne
    # dodac funkcje odczytujące wartośc pol
    # mam_kolor, mam_metraz, mam_liczba_okien

    def mam_kolor(self):
        print(f"Kolor: {self.__kolor}")

    def mam_metraz(self):
        print(f"Metraż: {self.__metraz}")

    def mam_liczba_okien(self):
        print(f"Liczba okien: {self.__liczba_okien}")

    def zmien_metraz(self):
        wybor = int(input("Podaj metraż"))
        self.__metraz = wybor
        self.mam_metraz()

    def zmien_kolor(self, kolor):
        self.__kolor = kolor
        self.mam_kolor()

    def zmien_okna(self):
        wybor = int(input("Podaj liczbę okien"))
        self.__liczba_okien = wybor
        self.mam_liczba_okien()


dom1 = Dom(500, "Bialy", 14)
dom1.mam_metraz()  # Metraż: 500
dom1.mam_kolor()  # Kolor: Bialy
dom1.mam_liczba_okien()  # Liczba okien: 14
dom1.zmien_metraz()
dom1.zmien_kolor("Czerwony")  # Kolor: Czerwony
dom1.zmien_okna()
