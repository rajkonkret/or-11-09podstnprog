user = "Tomek"  # str
wiek = 39  # int
wersja = 3.900001  # liczby zmiennoprzecinkowe - float
liczba = 134567456234  # int

print("Witaj %s masz teraz %d lat" % (user, wiek))
# print("Witaj %d masz teraz %s lat" % (user, wiek))  TypeError: %d format: a real number is required, not str
# %s str
# % d digit

print("Witaj %(user)s, masz teraz %(age)d lat" % {'user': user, "age": wiek})
# Witaj Tomek, masz teraz 39 lat
# ctrl / (?) - automatyczny komentarz

print("Witaj {}, masz teraz {} lat".format(user, wiek))  # Witaj Tomek masz teraz 39 lat
print("Witaj {}, masz teraz {} lat".format(wiek, user))  # Witaj 39, masz teraz Tomek lat

print(f"Witaj {user}, masz teraz {wiek} lat.")  # Witaj Tomek, masz teraz 39 lat.
# f - fstring - sformatowany tekst, zmienne umieszczone w klamerkach

print("Używamy wersji Python %i" % 3)  # Używamy wersji Python 3
print("Używamy wersji Python %f" % 3.9)  # Używamy wersji Python 3.900000
print("Używamy wersji Python %f" % 3.9)  # Używamy wersji Python 3.900000
# .1f z dokłądnośćia do jednego miejsca po przecinku
print("Używamy wersji Python %.2f" % 3.9)  # Używamy wersji Python 3.90
print("Używamy wersji Python %.0f" % 3.9)  # Używamy wersji Python 4
print("Używamy wersji Python %.f" % 3.9)  # Używamy wersji Python 4
# 0f - zero miejsc po przecinku, zaokrągla
x = 3.14
print("Zero miejsc po przecinku %.f" % x)
print("Oryginalny x =", x)
# Zero miejsc po przecinku 3
# Oryginalny x = 3.14
y = round(x)  # zwraca zaokrągloną liczbę
print(y)  # 3

print(f"Używa wersji Pythona {wersja}")  # Używa wersji Pythona 3.900001
print(f"Używa wersji Pythona {wersja:.1f}")  # Używa wersji Pythona 3.9
print(f"Używa wersji Pythona {wersja:.0f}")  # Używa wersji Pythona 4
# print(f"Używa wersji Pythona {wersja:.f}")  # ValueError: Format specifier missing precision

print(f"{user:>10}")  # "     Tomek"  - dopełnia spacjami do długości zadanej tekstu
print(f"{user:>20}")  # "               Tomek
print(f"{user:<30}")  # "Tomek                         "
print(f"{user:^10}")  # "  Tomek   "  - wyśrodkowany

print(liczba)  # 134567456234
print("Nasza duża liczba {:,}".format(liczba))  # Nasza duża liczba 134,567,456,234
print("Nasza duża liczba {:,}".format(liczba).replace(",", "."))  # Nasza duża liczba 134.567.456.234
print("Nasza duża liczba {:,}".format(liczba).replace(",", " "))  # Nasza duża liczba 134 567 456 234
print(f"Nasza duża liczba {liczba:,}")  # Nasza duża liczba 134,567,456,234
print(f"Nasza duża liczba {liczba:,}".replace(",", " "))  # Nasza duża liczba 134 567 456 234

a = 8
b = 7

print(f"Porównanie {a} > {b}", a > b)  # Porównanie 8 > 7 True
print(f"Porównanie {a} < {b}", a < b)  # Porównanie 8 < 7 False
print(f"Porównanie {a} == {b}", a == b)  # Porównanie 8 == 7 False == przy porównaniu wartośc
print(f"Porównanie {a} != {b}", a != b)  # różne  Porównanie 8 != 7 True
print(f"Porównanie {a} >= {b}", a >= b)  # Porównanie 8 >= 7 True
print(f"Porównanie {a} <= {b}", a <= b)  # Porównanie 8 <= 7 False
