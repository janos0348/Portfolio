def elemel(lista,mozgattSzam,uress):
    szam = mozgattSzam
    for i in range(len(lista) - 1, -1, -1):
        if not (lista[i] == uress) and szam == 0:
            szam = lista[i]
            lista[i] = uress
    return szam
def beilleszt(lista,megjatszott):
    for i in range(0, len(lista)):
        if lista[i] == " " and not (megjatszott == 0):
            lista[i] = megjatszott
            if lista[i] == megjatszott:
                megjatszott = 0
            else:
                print(megjatszott)
    if not (megjatszott == 0):
        print(f"! ! ! |Még nem helyezte el a {megjatszott} számot| ! ! !")
    return megjatszott