# funkcje zwracające wynik

def dodaj(a, b):
    return a + b  # return wraca wynik


def oblicz_vat(cena, vat=23):
    return cena * (100 + vat) / 100


print(dodaj(5, 6))  # 11
print(dodaj(6, 7) + dodaj(7, 2))  # 22
print(type(dodaj(6, 7) + dodaj(7, 2)))  # <class 'int'>

print(oblicz_vat(1000))  # 1230.0
print(oblicz_vat(1000, 7))  # 1070.0
print(oblicz_vat(vat=15, cena=1000))  # 1150.0

zm = oblicz_vat(1000)
print(zm)  # 1230.0
print(type(zm))  # <class 'float'>

if zm == 1230:
    print("Działa")

print(1230.0 > 1000)  # True
print(1230.0 > 1230)  # False
x = 3.1485
a = x * 100
print(a)  # 314.84999999999997

a = int(a)
print(a)  # 314
