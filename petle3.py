# petla while
# petla sterowana warunkiem

licznik = 0
while True:  # petla nieskonczona
    licznik += 1  # licznik = licznik + 1
    print(licznik, "Komunikat!!!")
    if licznik > 10:
        break  # przerwij pętle

licznik = 0
while licznik < 10:
    print("Komunika!")
    licznik += 1

lista = []
lista2 = []
while True:
    wej = input("Podaj liczbę")  # str
    if not wej.isnumeric():  # sprawdza znaki z łancucha czy sa cyfrą,
        # kropka(np.: we float) spowoduje uznanie za nie numeric
        break
    lista.append(wej)  # str
    lista2.append(int(wej))  # rzutujemy na int

print(lista)
print(lista2)
