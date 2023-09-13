# funkcje - wydzielony program, mozna wywołąc go wielokrotnie

a = 6
b = 7

print(a)


# funkcje niezwracające wyniku
# oddzielona dwoma pustymi linijkami
# definicja funkcji
def dodaj():  # funkcja bezargumentowa
    print(a + b)


def dodaj2(a, b):  # funkcja z dwoma argumentami a i b
    print(a + b)


def odejmij(a, b, c=0):  # funkcja z argumentem c o wartości domyslnej
    print(a - b - c)


def odejmij2(liczba1, liczba2):
    print(liczba1 - liczba2)


# wywołanie funkcji
dodaj()  # nazwa funkcji i nawiasy  # 13
dodaj2(5, 7)  # 12
odejmij(9, 4)  # wywołąnie z dwoma argumentami
odejmij(9, 5, 1)  # 3  przekazywanie przez pozycję
odejmij(c=6, a=8, b=8)  # -6  argumenty przekazane po nazwie
odejmij2(4, 5)
odejmij2(liczba1=4, liczba2=5)
print(dodaj())  # None funkcja nic nie zwraca
# print(dodaj() + dodaj2(4, 5))  # TypeError: unsupported operand type(s) for +: 'NoneType' and 'NoneType'
