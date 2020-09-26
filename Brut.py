import Crypteur as cr
from larousse_api import larousse
"""
def verif(ph,mp) :
    phrase = cr.decryptage(str(ph),str(mp))
    liste_mot = phrase.split(' ')
    #print(liste_mot)
    oui = 0
    for i in liste_mot :
        deff = larousse.get_definitions(str(i))
        #print(deff)
        if deff == []:
            #print('Non')
            ko = 0
        else:
            #print('Oui')
            oui = oui + 1
    inter = oui * 100
    total = inter / len(liste_mot)
    #print(total)
    if total > 30 :
        print('Possibilité de Phrase :\n' + str(phrase) + '   <---- Avec la clef ' + str(mp) )
"""
global ls
global imp
global point
point = [",","?",";",".",":","/",")","(","[","]"]
file = open("dicoFR1.txt",'r')
ls = file.read().split('\n')
file.close()
def supp(motbrut,position) : #Position 1 = devant Position 2 = derriere
    compmot = []
    for lettre in motbrut:
        compmot.append(lettre)
    if int(position) == 1 :
        del compmot[0]
    else :
        del compmot[-1]
    mfinal = ''.join(compmot)
    #print(mfinal)
    return mfinal
def verif(ph,mp) :
    phrase = cr.decryptage(str(ph),str(mp))
    liste_mot = phrase.split(' ')
    #print(liste_mot)
    oui = 0
    for i in liste_mot :

        #print(deff)
        k = i.lower()
        if k[-1] in point and len(k) > 1:
            #print('Suppresion derriere')
            k = supp(k, 2)
        if k[0] in point and len(k) > 1:
            #print('Suppression devant')
            k = supp(k, 1)
        #print(k)
        if k in ls :
            oui = oui + 1
    inter = oui * 100
    total = inter / len(liste_mot)
    #print(total)
    if total > 70 :
        print('Possibilité de Phrase :\n' + str(phrase) + '   <---- Avec la clef ' + str(mp) )
        if total > 99 :
            print('FIN')
            imp = False
Ms = input('Message a crypter : ')
l = input('Clef : ')
result = cr.cryptage(str(Ms),str(l))
print(result)
Message = input('Message a casser : ')


lettre = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
nombre = [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]

imp = True
while imp:
    nb = nombre[0]
    nombre[0] = nb + 1
    for i in nombre:
        if len(lettre) in nombre:
            tour = 0
            for n in nombre:
                if int(n) == int(len(lettre)):
                    changement = tour
                tour = tour + 1
            nombre[changement] = 0
            target = changement + 1
            nb = nombre[target]
            nombre[target] = int(nb) + 1
    position = 0
    total = len(nombre) - 1
    final = []
    while position < total:
        if int(nombre[position]) != -1:
            po = int(nombre[position])
            lf = lettre[po]
            final.append(str(lf))
        position = position + 1
    mot = ''.join(final)
    verif(Message,mot)





