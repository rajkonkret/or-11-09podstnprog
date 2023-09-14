# klasa abstrakcyjna
from abc import ABC, abstractmethod


class Ptak(ABC):
    """
    Klasa opisująca ptaka w pythonie
    """

    def __init__(self, gatunek, szybkosc):
        self.gatunek = gatunek
        self.szybkosc = szybkosc

    def latam(self):
        print("Tu", self.gatunek, "lecę z prędkością", self.szybkosc)

    @abstractmethod  # dekoraator metoda abstrakcyjna
    def wydaj_odglos(self):
        pass


class Kura(Ptak):
    """
    Kura
    """

    def __init__(self, gatunek):
        super().__init__(gatunek, 0)

    def latam(self):
        print("Tu", self.gatunek, "Ja nie latam")

    def wydaj_odglos(self):
        print("Kokokokokoko")

    def dziobanie(self):
        print("Tu", self.gatunek, "Idę sobie podziobać")


class Orzel(Ptak):

    def wydaj_odglos(self):
        print("piiiiiiii")

    def poluj(self):
        print(f"{self.gatunek}: Rozpoczynam polowanie")


# TypeError: Can't instantiate abstract class Ptak with abstract method wydaj_odglos

# or1 = Ptak("Orzeł", 20)
# or1.latam()  # Tu Orzeł lecę z prędkością 20
#
# kur1 = Ptak("Kura", 0)
# kur1.latam()  # Tu Kura lecę z prędkością 0
# kur1.wydaj_odglos()

kur2 = Kura("Kura")
kur2.latam()  # Tu Kura Ja nie latam
kur2.wydaj_odglos()  # Kokokokokoko
kur2.dziobanie()

or2 = Orzel("Orzeł", 20)
or2.wydaj_odglos()
or2.poluj()
