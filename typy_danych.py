wiek = 47
rok = 2023
temp = 36.6  # float
wiek2 = 45.5  # float

print(temp)
print(type(temp))  # <class 'float'>

print(wiek + rok)
print(wiek * rok)
print(wiek - rok)
print(wiek / rok)  # 0.023232822540781017 float
print(wiek // rok)  # 0 - częśc całkowita z dzielenia (int)
print(wiek ** rok)  # potęgowanie
print(wiek % rok)  # modulo - reszta z dzielenia
print(5 % 2)  # 1 bo 2 * 2 =4 - 5 = 1
print(54 - 5 * 43 + 4 / 2 + 4 / 2)  # -157.0
print(54 - (5 * 43) + (4 / 2 + 4) / 2)  # -158.0

print(0.2 + 0.8)  # 1.0 - float
print(0.2 + 0.7)  # 0.8999999999999999
# we float wystepuje błąd zaokrąglenia
print(0.1 + 0.1)

# typ logiczny
# prawda fałsz
# True False
czy_znasz_pythona = False
print(czy_znasz_pythona)  # False
print(type(czy_znasz_pythona))  # <class 'bool'>
print(int(czy_znasz_pythona))  # 0

czy_znasz_pythona = True
print(type(czy_znasz_pythona))  # <class 'bool'>
print(int(czy_znasz_pythona))  # 1  - zammiana na int
# 0 False 1 True

x = 1
print(bool(x))  # zamiana na bool - True

x = 100
print(bool(x))  # True
x = -10
print(bool(x))  # True

x = 0
print(bool(x))  # False

x = "Radek"
print(bool(x))  # True
x = None  # null - czyli nic
print(bool(x))  # False

x = ''
print(bool(x))  # False

# działania logiczne
# and - i
print(True and True)
print(True and False)
print(False and True)
print(False and False)
# True
# False
# False
# False


# or - lub
print(True or True)
print(True or False)
print(False or True)
print(False or False)
# True
# True
# True
# False

# not - negacja
print(not True)  # False
print(not False)  # True

x = 0
print(not x == 1)  # not False -> True
# 14:17
