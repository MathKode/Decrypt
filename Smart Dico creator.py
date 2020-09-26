from larousse_api import larousse
from verbecc import Conjugator
import os
import time
global point
point = [",","?",";",".",":","/",")","(","[","]"]
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
def app(motbrut) :
    print(motbrut)
    if motbrut == '' :
        print('ERREUR avoid HERE --------------------------------')
    else :
        if motbrut[-1] in point and len(motbrut) > 1 :
            #print('Suppresion derriere')
            motbrut = supp(motbrut,2)
        if motbrut[0] in point and len(motbrut) > 1 :
            #print('Suppression devant')
            motbrut = supp(motbrut,1)
        mot = motbrut.lower()
        #print(mot)
        file = open("dicoFR1.txt", 'r')
        c = file.read().split('\n')
        file.close()
        position = 0
        for space in c :
            if space == '' :
                del c[position]
            position = position + 1
        if mot in c :
            lo = 0
            #print('Existe deja')
        else :
            c.append(mot)
        tour = 0
        file = open("dicoFR1.txt",'w')
        for word in c :
            if tour == 0 :
                file.write(word)
            else :
                file.write('\n' + word)
            tour = tour + 1
        file.close()

f = os.listdir()
if "dicoFR1.txt" in f :
  print('Doc ok')
else :
  print('Création du doc')
  file = open("dicoFR1.txt","w")
  file.close()
choix = input('Quele est ton choix(1:ajout de mot/2:conjugaison) : ')
if int(choix) == 1 :
    mot = input('Mot : ')
    app(mot)
else :
    file = open("dicoFR1.txt", 'r')
    c = file.read().split('\n')
    file.close()
    cg = Conjugator(lang='fr')
    d = []
    for x in c :
        d.append(x)
    for verbe in d :
        try:
            result = cg.conjugate(verbe)
            print(result)
            ls = []
            temps = result['moods']['indicatif'].keys()
            #print(temps)
            for t in temps:
                conjugaison = result['moods']['indicatif'][str(t)]
                #print(conjugaison)
                ls = ls + conjugaison
            print(ls)
            for h in ls :
                c.append(h)
        except:
            print(verbe + " n'est pas un verbe")
    f = list(set(c))
    tour = 0
    file = open("dicoFR1.txt", 'w')
    for word in f :
        if tour == 0:
            file.write(word)
        else:
            file.write('\n' + word)
        tour = tour + 1
    file.close()
    print('FIN de la conjugaison')
i = True
diuze = input("Ou voulez vous reprendre(Première fois, mettre 0) : ")
p = int(diuze)
while i :
    file = open("dicoFR1.txt", 'r')
    c = file.read().split('\n')
    file.close()
    mot = c[p]
    print("Le mot _>" + mot + " " + str(p))
    deff = larousse.get_definitions(str(mot))
    if deff == [] :
        print('Pas de définition')
    else :
        ldef = deff[0].split(' ')
        print(ldef)
        for w in ldef :
            #print(w)
            app(w)
    p = p + 1
    if p > 50000 :
        i = False