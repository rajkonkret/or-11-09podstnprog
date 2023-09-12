# lista - kolekcja przechowuje dowolną ilość danych
# przechowuje w jednej kolekcji różne type
# zachowuje kolejność dodawania

lista = []
print(bool(lista))  # False

lista.append("Radek")  # append() - dodawanie elemntów na końcu listy
print(lista)  # ['Radek']
lista.append("Maciek")
lista.append("Jaśko")
lista.append("Zenek")

print(lista)
# ['Radek', 'Maciek', 'Jaśko', 'Zenek'] - indeksowanie 0,1,2,3
# -4, -3,-2,-1
print(lista[0])
print(lista[1])
print(lista[2])
print(lista[3])

# print(lista[10])  # IndexError: list index out of range

print(lista[-1])  # Zenek
print(lista[-2])  # Jaśko
print(lista[0:3])  # ['Radek', 'Maciek', 'Jaśko'] 0,1,2
print(lista[2:])  # ['Jaśko', 'Zenek'] - włacznie z 2 i ostatnim
print(lista[:3])  # ['Radek', 'Maciek', 'Jaśko'] 0,1,2 bez 3
print(lista[7:9])  # []
print(lista[1:3])  # ['Maciek', 'Jaśko'] indeksy 1 , 2

# nadpisywanie elemntu w liście
lista[2] = "Mikołaj"
print(lista)  # ['Radek', 'Maciek', 'Mikołaj', 'Zenek']

# rozszerzenie listy, wstawienie elemntu w konkretne miejsce
lista.insert(1, "Marcin")
print(lista)  # ['Radek', 'Marcin', 'Maciek', 'Mikołaj', 'Zenek']

# usunięcie po indeksie
index = lista.index("Zenek")
element = lista.pop(index)  # pop() - zwraca usunięty element
print(lista)  # ['Radek', 'Marcin', 'Maciek', 'Mikołaj']
print(element)  # Zenek

# usniecie po elmencie
lista.remove("Maciek")
print(lista)  # ['Radek', 'Marcin', 'Mikołaj']

# lista.remove("Tadek")  # ValueError: list.remove(x): x not in list

lista.append("Radek")
print(lista)  # ['Radek', 'Marcin', 'Mikołaj', 'Radek']
lista.remove("Radek")
print(lista)  # ['Marcin', 'Mikołaj', 'Radek']
# usunie tylko pierwsze wystąpienie

a = 1
b = 3
a = b
print(b)  # 3
a = 7
print(b)  # 3

lista2 = lista  # kopiowanie referencji (tylko adres w pamięci)
lista3 = lista.copy()  # prawidłowa kopia listy
print(lista2)  # ['Marcin', 'Mikołaj', 'Radek']
lista.clear()
print(lista)
print(lista2)
print(lista3)  # ['Marcin', 'Mikołaj', 'Radek']

# liczby = [54, 999, 34, 22, 13.34, 687, "A"]  # TypeError: '<' not supported between instances of 'str' and 'int'
liczby = [54, 999, 34, 22, 13.34, 687]
print(liczby)
print(type(liczby))  # <class 'list'>
liczby.sort()  # sortowanie
print(liczby)  # [13.34, 22, 34, 54, 687, 999]

lista_osoby = ['radek', 'ola']
lista_osoby.sort(reverse=True)  # ['radek', 'ola'] posortuje
lista_osoby.sort()
print(lista_osoby)  # ['ola', 'radek']

lista_osoby.reverse()  # odwrócenie listy
print(lista_osoby)  # ['radek', 'ola']

liczby[3] = 6666
print(liczby)  # [13.34, 22, 34, 6666, 687, 999]

print(liczby[0:3])
print(liczby[-2])
print(liczby[0:-2])  # [13.34, 22, 34, 6666]
print(liczby[-3:])  # [6666, 687, 999]

liczby.remove(34)
print(liczby)  # [13.34, 22, 6666, 687, 999]

print(liczby.pop(3))  # 687 bo na indeksie 3

print(len(liczby))  # 4

krotka = tuple(liczby)
print(krotka)  # (13.34, 22, 6666, 999)  () - krotka

tekst = "Python"
lista_1 = list(tekst)  # rozpakowanie sekwencji
print(lista_1)  # ['P', 'y', 't', 'h', 'o', 'n'] - [] lista
# rozpakowanie sekwencji
lista_2 = [tekst]  # stworzenie listy o jednym elemncie podanym w zmiennej
print(lista_2)  # ['Python']

print(lista_1 + lista_2)  # ['P', 'y', 't', 'h', 'o', 'n', 'Python']
