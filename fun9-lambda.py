# lambda to jest skrócony zapis funkcji, funkcja zwraca wynik
from functools import reduce


def odejmij(a, b):
    return a - b


print(odejmij(6, 7))
odejmij2 = lambda a, b: a - b
print(odejmij2(6, 7))
# -1
# -1

print((lambda cena, vat=23: cena * (100 + vat) / 100)(1000))  # 1230.0
oblicz_vat = lambda cena, vat=23: cena * (100 + vat) / 100
print(oblicz_vat(1000))
print(oblicz_vat(1000, 7))
print(oblicz_vat(vat=15, cena=1000))  # 1150.0

wiek = lambda x: "dziecko" if x < 10 else ("nastolatek" if x < 18 else "dorosły")

print(wiek(8))
print(wiek(17))
print(wiek(25))

lista = [1, 2, 3, 4, 5, 6, 7, 8, 10, 23, 50]


def zmien(x):
    return x * 2


# map() - pozwala zmienic wszystkie elementy kolekcji wg zadanej funkcji
print(f"Zastosowanie map(): {list(map(zmien, lista))}")
# Zastosowanie map(): [2, 4, 6, 8, 10, 12, 14, 16, 20, 46, 100]
print(f"Zastosowanine map() i lambda: {list(map(lambda x: x * 2, lista))}")
# Zastosowanine map() i lambda: [2, 4, 6, 8, 10, 12, 14, 16, 20, 46, 100]

# filter() - filtruje kolekcje i zwraca elemnt spełniające warunek
print(f"Zastosowanie filter(): {list(filter(lambda x: x < 3, lista))}")
# wyfiltrowac wieksze od 8
print(f"Zastosowanie filter(): {list(filter(lambda x: x > 8, lista))}")
# wieksze od 3 mniejsze od 20
print(f"Zastosowanie filter(): {list(filter(lambda x: 3 < x < 20, lista))}")
# Zastosowanie filter(): [4, 5, 6, 7, 8, 10]
# x > 3 and x < 20 -> 3 < x <20
# lista = [1, 2, 3, 4, 5, 6, 7, 8, 10, 23, 50]
# ciekawostka wygenerowana za pomoca Tabnine
# reduce() - zwraca zredukowany zsumowany element kolekcji wg zadanej funkcji
print(f"Zastosowanie reduce(): {reduce(lambda x, y: x + y, lista)}")
# reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]) calculates
#     ((((1+2)+3)+4)+5)
print(f"Zastosowanie reduce(): {reduce(lambda x, y: x * y, lista)}")
# 11:20
result = 0
for i in [1, 2, 3, 4, 5]:  # 1+2+3+4+5=15
    result += i
print(result)
print(reduce(lambda x, y: x + y, [1, 2, 3, 4, 5]))
# 15
# 15
list_str = ['a', 'b', 'c']
print(reduce(lambda x, y: x + y, list_str))  # abc
