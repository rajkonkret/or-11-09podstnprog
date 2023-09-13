# print(2 / 0)

# napisanie aplikacji kalkulator
# menu z operacjami
# pobrac typ opercji
# pobrac liczby
# wyswietlic wynik
# w petli while

while True:
    print(f"""
    1. Dodawanie
    2. Odejmowanie
    3. Mnożenie
    4. Dzielenie
    5. Koniec
    """)
    odp = input("Podaj działąnie jakie chcesz wykonać")
    if odp >= '5':
        break
    try:  # spróbuj

        a = float(input("Podaj pierwszą liczbę"))
        b = float(input("Podaj drugą liczbę"))

        if odp == '1':
            print(f"wynik dodawania {a} + {b} = {a + b}")
        elif odp == '2':
            print("Odejmowanie", a - b)
        elif odp == '3':
            print("Mnożenie", a * b)
        elif odp == '4':
            print("Dzielenie", a / b)
        else:
            print("Nie znam takiego działania")
    except ZeroDivisionError:
        print("Nie dziel przez zero")  # Nie dziel przez zero
    except TypeError:
        print("Błąd typu")
    except ValueError:
        print("Bład wartość")
    except Exception as e:  #  przechwytuje wszystkie pozostałe błedy
        print("Bład", e)
    else:  # gdy nie ma błedu
        print("Gdy nie ma błedu")
    finally:  # zawsze
        print("Zawsze")
# dodac mnozenie, dzielenie
# dodac by wyswietlało: wynik dodawania 2 + 5 = 7
# try - except (else - finally)
# 13:10