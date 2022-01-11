def ellenorzo(vege,source1,source2,source3,helper):
    def veglegesnyeres(lista):
        egyezik = False
        szamlalo = 0
        for i in range(len(lista)):

            if lista[i] == lista[0]:
                szamlalo +=1

            if szamlalo == len(lista):
                egyezik = True
        return egyezik
    lista1 = veglegesnyeres(source1)
    lista2 = veglegesnyeres(source2)
    lista3 = veglegesnyeres(source3)
    lista4 = veglegesnyeres(helper)
    if lista1 == True and lista2 == True and lista3 == True and lista4 == True:
        vege = True
    return vege