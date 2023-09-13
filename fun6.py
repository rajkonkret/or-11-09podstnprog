# funkcje, która oblicza średnią

lista = [1, 2, 3, 4, 5]


def liczby(numer, lista):
    print(lista)
    suma = 0
    for l in lista:
        suma += l
    count = len(lista)
    print(numer, suma / count)


def liczby2(i=0, *cyfry):  # argumenty funkcji zostana zapakowane w krotkę
    try:
        print(cyfry)  # (1, 2, 3, 4, 5, 6)
        suma = 0
        for l in cyfry:
            suma += l
        count = len(cyfry)
        print(count)
        print(i, suma / count)
    except Exception as e:
        print('Bład', e)


liczby("1", lista)
liczby2(1, 2, 3, 4, 5, 6)
liczby2(1, 2, 3, 4, 5, 6, 8, 9, 10, 11)
liczby2()  # Bład division by zero
liczby2(1, "2")  # Bład unsupported operand type(s) for +=: 'int' and 'str', ('2',)
