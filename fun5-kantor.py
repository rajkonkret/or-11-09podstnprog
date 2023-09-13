# funkcja kantor, ma posiadac dwie funkcje eur, usd

def kantor(waluta):
    print("Urucomienie kantoru")

    def eur(kwota):
        print(f"{kwota} euro = {kwota * 4.6} zł")

    def usd(kwota):
        print(f"{kwota} dol = {kwota * 4.1} zł")

    if waluta == 'eur':
        return eur
    else:
        return usd


kantor_eur = kantor('eur')
print(kantor_eur)
print(type(kantor_eur))  # <function kantor.<locals>.eur at 0x00000253F265E0C0>
kantor_eur(1000)  # 1000 euro = 4600.0 zł
