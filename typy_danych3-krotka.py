# krotka (tuple)- niezmienialne dane
# zmienna, niezmienna

tupla = 'radek'
print(type(tupla))  # <class 'str'>
tpl2 = "radek",
print(type(tpl2))  # <class 'tuple'>
temp = 37, 5
print(type(temp))  # <class 'tuple'>
tupla2 = ("Tomek", "Radek", "Marek")
print(type(tupla2))
print(tupla2)  # ('Tomek', 'Radek', 'Marek')

tupla3 = 43, 55, 22.34, 11, 200
print(type(tupla3))  # <class 'tuple'>
print(tupla3)  # (43, 55, 22.34, 11, 200)

print(tupla2.index("Tomek"))  # 0
print(tupla2.count("Tomek"))  # 1

a, b = 1, 2
print(a)
print(b)
a, *b = 1, 2, 3

imie1, *imie2 = tupla2  # * worek na pozostałe dane
print(imie2)  # ['Radek', 'Marek']
print(imie1)

a, *b, c = 1, 2, 3, 4
print(a)
print(b)  # [2, 3]
print(c)
# rozpakowanie tupli

lista = list(tupla3)  # zamiana krotki na liste
print(lista)  # [43, 55, 22.34, 11, 200]
print(type(lista))