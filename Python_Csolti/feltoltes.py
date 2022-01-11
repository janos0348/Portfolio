import random
def feltolt(sourceList1,sourceList2,sourceList3,szamokTomb):
    while not(len(szamokTomb) == 0):
        randomIndex = random.randint(0,len(szamokTomb)-1)
        if len(sourceList1) < 3:
            sourceList1.append(szamokTomb[randomIndex])
        elif len(sourceList2) <3:
            sourceList2.append(szamokTomb[randomIndex])
        elif len(sourceList3) <3:
            sourceList3.append(szamokTomb[randomIndex])
        szamokTomb.remove(szamokTomb[randomIndex])
    return sourceList1,sourceList3,sourceList2