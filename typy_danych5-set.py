# set (zbiór)  - kolekcja, ktora nie zawiera zduplikowanych elementów
# 1,1,1 -> 1
# set nie pamięta kolejności dodawania, w zasadzie nie zawiera indeksu

lista = [44, 55, 66, 777, 33, 22, 11, 33, 11]
# ctrl alt l
print(lista)  # [44, 55, 66, 777, 33, 22, 11, 33, 11]
zbior = set(lista)
print(type(zbior))  # <class 'set'>
print(zbior)  # {33, 66, 777, 11, 44, 22, 55}

pusta_lista = []
pusty_set = set()  # tworzenie pustego seta
print(pusta_lista)  # []
print(pusty_set)  # set()
pusty_slownik = dict()
print(pusty_slownik)  # {} - pusty słownik

pusty_set.add(33)
pusty_set.add(18)
pusty_set.add(18)
pusty_set.add(18)
print(pusty_set)  # {33, 18}
zbior.add(33)
zbior.add(18)
zbior.add(18)
print(zbior)  # {33, 66, 777, 11, 44, 18, 22, 55}

zbior.remove(55)  # usuniecie elemntu ze zbioru
print(zbior)  # {33, 66, 777, 11, 44, 18, 22}
print(sorted(zbior))  # [11, 18, 22, 33, 44, 66, 777]
print(zbior)

print(zbior.pop())  # usuniecie pierwszego elementu ze zbioru  33
print(zbior)  # {66, 777, 11, 44, 18, 22}
zbior.pop()
zbior.pop()
print(zbior)  # {11, 44, 18, 22}

lista2 = list(zbior)  # list() - zaiana na liste
print(lista2)  # [11, 44, 18, 22]

zbior2 = {66, 11, 44, 18, 52, 62, 999, 999}
print(zbior2)  # {66, 18, 52, 999, 11, 44, 62}

print(len(zbior))  # 4

print(zbior | zbior2)  # suma {66, 999, 11, 44, 18, 52, 22, 62}
print(zbior & zbior2)  # częśc wspolna {18, 11, 44}
print(zbior - zbior2)  # różnica {22}

print(zbior.difference(zbior2))  # {22}
print(zbior2.difference(zbior))  # {66, 52, 62, 999}

# print(zbior + zbior2)  # TypeError: unsupported operand type(s) for +: 'set' and 'set'
zbior.update(zbior2)
print(zbior)  # {66, 999, 11, 44, 18, 52, 22, 62}

first, second, third = "ABC"
print(first, second, third)  # A B C
a, b, c = 1, 2, 3
_, value, _ = [1, 2, 3]
print(value)  # 2
