# hackerrank
# w3wschool
# spoj
# słownik - klucz - wartosc
# {"name":"Radek"} - {"klucz" : "wartość"}

dictionary = {}  # pusty słownik
print(type(dictionary))  # <class 'dict'>

dictionary['imie'] = "Radek"
print(dictionary)  # {'imie': 'Radek'}

dictionary['wiek'] = 39
print(dictionary)  # {'imie': 'Radek', 'wiek': 39}

print(dictionary.keys())
print(dictionary.values())
print(dictionary.items())
# dict_keys(['imie', 'wiek'])
# dict_values(['Radek', 39])
# dict_items([('imie', 'Radek'), ('wiek', 39)])

dictionary.update({'date': '12-12-2023'})
print(dictionary)  # {'imie': 'Radek', 'wiek': 39, 'date': '12-12-2023'}

dictionary2 = {'x': 2}  # tworzenie ssłownika w miejscu deklaracji
dictionary2.update([('y', 3), ('z', 0)])
print(dictionary2)  # {'x': 2, 'y': 3, 'z': 0}

dict2 = {'imie': 'name', 'kot': 'cat'}
print(dict2['imie'])  # name
# wypiszemy słowa polskie jakie mamy w słowniku
# pobierzemy od użytkownika słówko do przetłumaczenia
# wypiszemy tłumaczenie słowa

# print("Mamy w słowniku", dict2.keys())
# key = input("Podaj słówko do przetłumaczenia")  # str() - input - pobiera dane np.: z klawiatury
# print(dict2[key.replace(" ", "").lower()])  # cat

# napisac kalkulator, pobieracie a i b, wypisujecie wynik dodawania
a = int(input("Podaj pierwszą liczbę"))
b = input("Podaj pierwszą liczbę")  # input zwraca str
print(a + int(b))  # int - rzutowanie na int
c = 6.5
print(type(c))  # <class 'float'>
print(int(c))  # 6
c = 6.9
print(type(c))  # <class 'float'>
print(int(c))  # 6
print(round(c))  # 7
print(type(round(c)))  # <class 'int'>
