class Car:
    """
    Klasa samochód
    """

    def __init__(self, model, year):
        self.model = model
        self.year = year
        self.__predkosc = 0  # pole prywatne
        # nie ma możliwości bezpośredniego odczytywania i zapisywania tego pola

    def gaz(self):
        self.__predkosc += 10
        self.__zmien_bieg()

    def hamuj(self):
        self.__predkosc -= 10

    def licznik(self):
        print(f"Prędkość wynosi", self.__predkosc, "km/h")

    def __zmien_bieg(self):  # funkcja prywatna
        print("Zmiana biegu")


car = Car("Dacia", 2023)
car.gaz()
car.gaz()
car.gaz()
car.gaz()
car.gaz()
# print(car.__predkosc)  # 50  AttributeError:
# 'Car' object has no attribute '__predkosc'. Did you mean: '_Car__predkosc'?
car.licznik()  # Prędkość wynosi 50 km/h
# car.__predkosc = 0
car.hamuj()
car.hamuj()
car.hamuj()
car.hamuj()
car.hamuj()
# print(car.__predkosc)  # 0
car.licznik()
