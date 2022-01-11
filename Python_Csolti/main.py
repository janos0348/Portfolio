import random
import feltoltes
import ellenorzes
import atTesz
uress = " "
megjatszottt = 0
szamok = [1,1,1,2,2,2,3,3,3]
source1 = []
source2 = []
source3 = []
helper = [uress,uress,uress]
vege = False
def kiiratas(sourceList1,sourceList2,sourceList3,helperList):
    for i in range(2,-1,-1):
        print("|{}| |{}| |{}| |{}|".format(source1[i],source2[i],source3[i],helper[i]))
def jatekmenet(sourceList1,sourceList2,sourceList3,helperList,megjatszott,vege):
    kiiratas(sourceList1, sourceList2, sourceList3, helperList)
    while not vege:

        if megjatszott == 0:
            honnan = int(input("Meik oszlopból: "))
        hova = int(input("Meik oszlopba: "))

        if honnan == 1:
            megjatszott = atTesz.elemel(sourceList1,megjatszott," ")

        elif honnan == 2:
            megjatszott = atTesz.elemel(sourceList2,megjatszott," ")
        elif honnan == 3:
            megjatszott =atTesz.elemel(sourceList3,megjatszott," ")
        elif honnan == 4:
            megjatszott =atTesz.elemel(helperList,megjatszott," ")

        if hova == 1:
            megjatszott =atTesz.beilleszt(sourceList1,megjatszott)
        elif hova == 2:
            megjatszott =atTesz.beilleszt(sourceList2, megjatszott)
        elif hova == 3:
            megjatszott =atTesz.beilleszt(sourceList3, megjatszott)
        elif hova == 4:
            megjatszott =atTesz.beilleszt(helperList,megjatszott)
        vege = ellenorzes.ellenorzo(vege,sourceList1,sourceList2,sourceList3,helperList)
        kiiratas(sourceList1,sourceList2,sourceList3,helperList)
        if vege == True:
            print("!!!! WINNER !!!!")
def nyert(lista1,lista2,lista3,helper):
    pass
feltoltes.feltolt(source1,source2,source3,szamok)
jatekmenet(source1,source2,source3,helper,megjatszottt,vege)