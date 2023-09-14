# dziedziczenie

class Pojazd:
    def __init__(self, kolor):
        self.kolor = kolor

    def info(self):
        print(f"Kolor: {self.kolor}")


class Samochod(Pojazd):  # Samochod dziedziczy po Pojazd
    """
    Samochód
    """

    def __init__(self, kolor, marka):
        super().__init__(kolor)
        self.marka = marka

    def info(self):
        super().info()
        print(f"Marka: {self.marka}")


poj = Pojazd("Czerwony")
poj.info()
car1 = Samochod("Zielony", "Dacia")
car1.info()
# Kolor: Zielony
# Marka: Dacia
poj2 = Pojazd("Niebieski")
poj2.info()

car2 = Samochod("Czerwony", "Tico")
car2.info()
# Kolor: Czerwony
# Marka: Tico
