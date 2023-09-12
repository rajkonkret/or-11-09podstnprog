# petle wykonują dany blok kodu wielokrotnie
# for - petla iterująca
import random
from itertools import zip_longest

for i in range(10):  # 0..9
    print(i)

for i in range(10):
    pass  # nic nie rób

for _ in range(10):
    pass
lista = []
for i in range(100):
    lista.append(i)

print(lista)

for i in range(10):
    print(i * 2)

# przerobic totolotka na petle
# trzeba zaimportowac random
# trzeba wygenerowac liste 1..49
# trzeba wylosowac z listy element i usunać go
# wypisac wylosowane listy(od razu, łapac w nową liste i wyswietlic liste)

lotto = list(range(1, 50))
wynik = []
for i in range(6):  # 0..5
    wyn = random.choice(lotto)
    lotto.remove(wyn)
    wynik.append(wyn)

print(wynik)

for i in range(20):  # 0..19
    if i % 2 == 0:  # reszta z dzielenia (modulo)
        print(i, "parzysta")

for i in range(1, 20):  # 1..19
    if i % 2 == 0:  # reszta z dzielenia (modulo)
        print(i, "parzysta")

lista3 = []
for j in range(10):
    if j % 2 == 0:
        lista3.append(j)

lista4 = [j for j in range(10) if j % 2 == 0]
print(lista3)
print(lista4)  # [0, 2, 4, 6, 8]

for c in lista4:
    if c == 2:
        c += 1  # c = c + 1
        # print(c) - wyswietli tylko 3
    print(c)  # to wyswietli za każdym przejsciem pętli

print(c)  # wyswietli 8

a = 1
a += 1  # a = a + 2
print(a)  # 2
a *= 3  # a = a * 3
print(a)  # 6
a -= 1  # a = a - 1
print(a)  # 5
a %= 2  # a = a % 2
print(a)  # 1
a /= 2  # a = a / 2
print(a)  # 0.5  float

imiona = ['Radek', 'Asia', 'Zbyszek', 'Marcin']
for p in imiona:
    print(p)  # Radek

# wypisac imiona z listy i indeks
# 0 Radek
# 1 Asia

for p in imiona:
    print(imiona.index(p), p)

for p in range(len(imiona)):  # len() - dlugosc listy = 4 -> range(4)  -> generuje liczby 0..3 i podstawia pod p
    print(p, imiona[p])  # wypisanie numeru i elemntu z listy o danym indeksie

# enumerate() - zwraca ponumerowaną kolekcje
for p in enumerate(imiona):
    print(p)  # (0, 'Radek') krotka z numerem indeksu i elementem kolekcji

a, b = (0, 'Radek')
print(a)
print(b)

for p, w in enumerate(imiona):
    print(p, w, sep=";", end="")  # 0 Radek
    # print(f"{p} {w}")
# sep - znak oddzielający elementy (domyślnie spacja)
# end - znak końca lini (domyslnie \n - nowa linia)
print()

ludzie = ['Radek', 'Zenek', 'Asia', 'Marcin', 'Franek']
# wiek = [47, 67, 34, 32, 63]
wiek = [47, 67, 34, 32]

# for p, o in enumerate(ludzie):
#     print(p, o, wiek[p])  # IndexError: list index out of range

# zip - łącenie kolekcji w jedna - zwraca krotke
for k in zip(ludzie, wiek):
    print(k)  # ('Marcin', 32)

for o, w in zip(ludzie, wiek):
    print(o, w)  # Marcin 32

for p in enumerate(zip(ludzie, wiek)):
    print(p)  # (3, ('Marcin', 32))

a, b = (3, ('Marcin', 32))
print(a)
print(b)  # ('Marcin', 32)
b, c = ('Marcin', 32)
print(b)
print(c)
a, (b, c) = (3, ('Marcin', 32))
print(a)
print(b)
print(c)

for i, o in enumerate(zip(ludzie, wiek)):
    print(i, o)  # 0 ('Radek', 47)

for i, (o, w) in enumerate(zip(ludzie, wiek)):
    print(o, w, i)  # Radek 47 0

jezyk = ['java', 'python']
for i, (o, w, j) in enumerate(zip(ludzie, wiek, jezyk)):
    print(i, o, w, j)
# 0 Radek 47 java
# 1 Zenek 67 python
# łaczy w pary mozliwe elemnety

zipped = zip_longest(ludzie, wiek, jezyk, fillvalue='Nan')
print(zipped)  # iterator
zipped_list = list(zipped)
print(type(zipped))  # <class 'itertools.zip_longest'>
# for item in zipped:
#     print(item)  # ('Asia', 34, 'Nan') ('Franek', 'Nan', 'Nan')

for item in zipped_list:
    print(item)  # ('Franek', 'Nan', 'Nan')

for o1, w1, j1 in zipped_list:
    print(o1, w1, j1)
# Radek 47 java
# Zenek 67 python
# Asia 34 Nan
# Marcin 32 Nan
# Franek Nan Nan