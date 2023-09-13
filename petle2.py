dictionary = {'imie': 'Radek', 'nazwisko': 'Kowalski'}

print(type(dictionary))  # <class 'dict'>

# wypisze klucze
for k in dictionary:
    print(k)

for k in dictionary.keys():
    print(k)
# imie
# nazwisko


# wypisze wartosci
for v in dictionary.values():
    print(v)
# Radek
# Kowalski

# wypisanie itemów (par klucz-wartość)
for i in dictionary.items():
    print(i)
    # ('imie', 'Radek')
    # ('nazwisko', 'Kowalski')

for k, v in dictionary.items():
    print(k, "=>", v)
# imie => Radek
# nazwisko => Kowalski

dict2 = {'imie': ['Radek', 'Tomek'], 'nazwisko': ['Kowalski', 'Nowak']}
for i in dict2.items():
    print(i)  # ('imie', ['Radek', 'Tomek'])

for k, v in dict2.items():
    print(type(v))
    print(k, '=>', v)
    for a in v:
        print(k, ":", a)

imiona = []
nazwiska = []
for k, v in dict2.items():  # pobranie klucza i wartosci
    if k == 'imie':  # gddy klucz imie to dane wpisujemy do listy imiona
        for a in v:
            imiona.append(a)
    elif k == 'nazwisko':  # gdy klucz nazwisko to dane do listy nazwiska
        for a in v:
            nazwiska.append(a)

lista_dict = list(zip(imiona, nazwiska))  # [('Radek', 'Kowalski'), ('Tomek', 'Nowak')]
print(lista_dict)
print(lista_dict[0])  # 0 pierwszy elemnt z listy
# ('Radek', 'Kowalski')

dictionary3 = {'name': 'imie', 'company': 'Orange'}
print(dictionary3)  # {'name': 'imie', 'company': 'Orange'}

print({value: key for key, value in dictionary3.items()})
# {'imie': 'name', 'Orange': 'company'} - zamiana kluczy z warttościami

d2 = {}
for key, value in dictionary3.items():
    print(key, '=>', value)  # company => Orange
    d2[value] = key  # d2['Orange'] = 'company'
    # d2.update({value:key})

print(d2)  # {'imie': 'name', 'Orange': 'company'}
