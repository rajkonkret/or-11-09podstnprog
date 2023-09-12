# match case

lista = []
lang = input("Podaj znany Ci język progrmowania")

match lang.lower().replace(" ", ""):
    case "python":
        lista.append(lang)
    case "java":
        lista.append(lang)
    case "basic":
        lista.append(lang)
    case "c++":
        lista.append(lang)
    case _:  # default (taki ala else)
        print("Nie znam takiego języka")

print(lista)
