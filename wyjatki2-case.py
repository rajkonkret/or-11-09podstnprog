while True:
    try:
        z = input("Podaj działanie + - * /")
        a = int(input("Podaj pierwszą liczbę"))
        b = int(input("Podaj drugą liczbę"))

        match z:
            case "+":
                print(f"Wynik dodawania {a} + {b} = {a + b}")
            case "-":
                print(f"Wynik odejmowania {a} - {b} = {a - b}")
            case "*":
                print(f"Wynik mnożenia {a} * {b} = {a * b}")
            case "/":
                print(f"Wynik dzielenia {a} / {b} = {a / b}")
            case _:
                break
    except ZeroDivisionError:
        print("Nie dziel przez zero")
    except TypeError:
        print("Bład typu")
    except ValueError:
        print("Błąd wartości")
    except Exception as e:
        print("Bład", e)
    else:
        print("Nie ma błedu")
    finally:
        print("Zawsze")