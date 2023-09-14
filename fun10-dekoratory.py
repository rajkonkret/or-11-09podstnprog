# dekoratory

def dekor(funkc):
    def wew():
        result = funkc()
        print("Dekorujemy")
        return result

    return wew


@dekor  # - dekorator
def hej():
    print("Hej")


@dekor
def hej1():
    print("Ja nie jestem hej")


hej()
# wew = dekor(hej())
# wew()
# Dekorujemy
# Hej
hej1()
# Dekorujemy
# Ja nie jestem hej
