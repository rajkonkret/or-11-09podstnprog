class Pracownik:
    def __init__(self, imie, nazwisko, pensja):
        self.imie = imie
        self.nazwisko = nazwisko
        self.pensja = pensja

    def przedstaw_sie(self):
        print(f"Cześć, jestem {self.imie} {self.nazwisko}")

    def oblicz_pensje(self):
        return self.pensja


class Manager(Pracownik):
    def __init__(self, imie, nazwisko, pensja, premia):
        super().__init__(imie, nazwisko, pensja)
        self.premia = premia

    def oblicz_pensje(self):
        return self.pensja + self.premia


pracownik = Pracownik("Jan", "Kowalski", 7500)
pracownik.przedstaw_sie()
wyn_prac = pracownik.oblicz_pensje()
print(
    f"Wynagrodzenie dla pracownika {pracownik.imie} {pracownik.nazwisko}: {wyn_prac}"
)

menago = Manager("Anna", "Nowak", 9000, 2000)
menago.przedstaw_sie()
wyn_men = menago.oblicz_pensje()
print(
    f"Wynagrodzenie dla menadżera {menago.imie} {menago.nazwisko}: {wyn_men}"
)

# Cześć, jestem Anna Nowak
# Wynagrodzenie dla menadżera Anna Nowak: 11000