# warunki - instrukcje sterowania przepływem programu
# if - instrukcja warunkawa sterowana warunkiem True False (wyażenie)
# if warunek:
# (wciecie 4 spacje)instrukcje do wykonania jeśli warunek jest True

odp = False

if odp:
    print("Brawo!!!")
else:  # w przeciwnym przypadku
    print("Ucz się dalej")

print("Działam dalej")

# podatek = 0.0
# zarobki = float(input("Podaj dochód"))  # str -> float
# if zarobki < 10000:  # jezeli warunek spełniony
#     podatek = 0.0
# elif zarobki < 30000:
#     podatek = 0.2
# elif zarobki < 100000:  # ale jeżeli ten warunek spełniony
#     podatek = 0.4
# else:
#     podatek = 0.6
# # kolejnosc warunków ma znaczenie
# # natrafienie pierwszego True oznacza wyjście z drabini. nie sprawdza kolejnych warunków
#
# print(f"Zapłacisz {podatek * zarobki} zł")  # f -stringformat - oznacza, ze jak napotka {zminna} i nzawe zmiennej
# # to wstawi wartośc tej zmiennej w tym miejscu

summa_zam = 150
if summa_zam > 100:
    rabacik = 25
else:
    rabacik = 0

print("Rabat wynosi", rabacik)  # Rabat wynosi 25

rabat = 25 if summa_zam > 100 else 0  # True if False
print("Rabat wynosi", rabat)  # Rabat wynosi 25

lista_bledow = []
alert_system = 'email'
error = 'cokolwiek'
error_message = 'Stało się coś strasznego'

if alert_system == 'console':  # == porównanie
    print(error_message)
elif alert_system == 'email':
    if error == 'medium':
        lista_bledow.append("ostrzeżenie")
    elif error == 'critical':
        lista_bledow.append("Bład krytyczny")
    else:
        lista_bledow.append("Bład inny")
print(lista_bledow)

# napisac test z historii, geografii, czegokolwiek
# wypisac pytanie i pobrac odpowiedz input
# sprawdzic wynik if
# wyswietlic wynik print

odp = input("Podaj datę Chrztu Polski")
if odp.lower().replace(" ", "") == '966':
    print("Odpowieź prawidłowa")
else:
    print("Masz w książce na stronie 23")
# 13:30 