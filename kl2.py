class Human:
    """
    Klasa Human opisująca człowieka w Pythonie
    """

    def __init__(self, imie, wiek, wzrost, plec='k'):  # init - konstruktor
        self.imie = imie
        self.wiek = wiek
        self.wzrost = wzrost
        self.plec = plec

    def powitanie(self):
        print(f"MAm na imię {self.imie}")

    def moj_wiek(self):
        print(f"Mam {self.wiek} lat")

    def moj_wzrost(self):
        print(f"Mam {self.wzrost} cm wzrostu.")

    def ruszaj(self):
        if self.plec.lower() == 'm':
            print("Ruszyłem w drogę")
        else:
            print("Ruszyłam w drogę")


cz1 = Human("Ania", 34, 170)
cz1.ruszaj()  # Ruszyłam w drogę
print(cz1.imie)  # Ania
# trzy funkcje - powitanie,moj_wiek,moj_wzrost
# stworzyc drugi obiekt płci innej niz dotychczas
cz2 = Human("Radek", 78, 189, "m")
cz2.powitanie()
cz2.moj_wzrost()
cz2.moj_wiek()
cz2.ruszaj()
# MAm na imię Radek
# Mam 189 cm wzrostu.
# Mam 78 lat
# 13:30