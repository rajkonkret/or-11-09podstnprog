# 14:42
# funkcja zagnieżdzona
def fun1():  # definicja fun1 - zapamietuje adres
    print("To jest fun1")

    def fun2():  # to jest tylko deklaracja funkcji
        print("To jest funkcja fun2")

    return fun2  # nazwa bez nawiasów bo zwracamy tylko adres a nie chemy by tu się fun2 wykonało


fun1()  # To jest fun1
xFun = fun1()
print(xFun)  # <function fun1.<locals>.fun2 at 0x0000020C1896E0C0>
print(type(xFun))  # <class 'function'>
xFun()  # To jest funkcja fun2
