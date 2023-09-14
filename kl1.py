# klasy - szablon opisujacy obiekt
# moze posiadac pola i funkcje

class Human:
    """
    Klasa opisująca człowieka  w Pythonie
    """
    imie = ""
    wiek = None
    plec = "k"

    def powitanie(self):
        print(f"Nazywam się {self.imie}.")

    def test(self):
        pass

    def podaj_wiek(self):
        print("Mam", self.wiek, "lat")


cz1 = Human()  # stworzeie obiektu klasy Human
# wyswietlenie dokumentacji

print(cz1.__doc__)  # Klasa opisująca człowieka  w Pythonie
print(print.__doc__)
print(cz1.wiek)  # None
cz1.imie = "Ania"
cz1.wiek = 30
cz1.powitanie()  # Nazywam się Ania.
print(cz1.imie)  # Ania
print(cz1.test)  # <bound method Human.test of <__main__.Human object at 0x000001F43E009050>>
cz1.podaj_wiek()  # Mam 30 lat

cz2 = Human()
cz2.wiek = 40
cz2.imie = "Radek"
cz2.plec = "m"
print(cz2.imie)
cz2.powitanie()  # Nazywam się Radek.
