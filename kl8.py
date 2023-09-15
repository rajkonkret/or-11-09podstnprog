# wielodziedziczenie

class A:
    def method(self):
        print("Metoda z klasy A")


class B:
    """"""

    def method(self):
        print("Metoda z kalsy B")


class C(B, A):  # dziedziczy z klasy A i z klasy B, kolejnosc ma znaczenie
    """
    klasa C
    """

    def method(self):
        print("Metoda z klasy C")  # Metoda z klasy C
        super().method()  # wykorzystanie z klasy nadrzednej C(B, A)  z klasy B
        A.method(self)  # Metoda z klasy A


a = A()
a.method()

b = B()
b.method()
# Metoda z klasy A
# Metoda z kalsy B

c = C()
c.method()  # Metoda z klasy A
print(C.__mro__)
# (<class '__main__.C'>, <class '__main__.A'>, <class '__main__.B'>, <class 'object'>)
# (<class '__main__.C'>, <class '__main__.B'>, <class '__main__.A'>, <class 'object'>)
