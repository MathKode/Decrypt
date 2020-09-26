global caractère
caractère = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z",
             "A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z",
             " ", #Attention, cette case n'est pas vide, elle représente l'espace
             "1","2","3","4","5","6","7","8","9","0",
             "@","#","&","é",'"',"'","(","§","è","!","ç",")","-","_","°","^","¨","$","*","€","ù","%","`","£",
             ",","?",";",".",":","/","=","+",
             "â","ê","î","ô","û",
             "ä","ë","ï","ö","ü",
             "à",    "ì","ò",
             "<",">"]

def cryptage(ms,cl) :
  if True :
    """
    Ce code va permettre de crypter les messages en fonction de la clef
    """
    #Transformer en chiffre le message
    message = str(ms)
    if message == "" :
        print("L,utilisateur doit remplir la case message")
    else :
        liste_message = list(message)
        #print(liste_message)
        i=0
        total = len(liste_message)
        while i < total :
            lettre = liste_message[i]
            position = caractère.index(str(lettre))
            liste_message[i] = position
            i = i + 1
        #print(liste_message)
    # Transformer en chiffre la clef
    clef = str(cl)
    if clef == '' :
        print('l utilisateur doit remplir la case clef')
    else :
        liste_clef = list(clef)
        #print(liste_clef)
        i = 0
        total = len(liste_clef)
        while i < total:
            lettre = liste_clef[i]
            position = caractère.index(str(lettre))
            liste_clef[i] = position
            i = i + 1
        #print(liste_clef)


    #Mettre la clef a la longueur de message
    i = 0
    tour = 0
    clef_liste_final = []
    longueur = len(liste_message)
    while tour < longueur :
        if i > len(liste_clef) - 1 :
            i = 0
        clef_liste_final.append(liste_clef[i])
        i = i + 1
        tour = tour + 1
    #print(clef_liste_final)

    #Additionner les deux listes
    final_liste = []
    i = 0
    #print(len(caractère))
    while i < len(liste_message) :
        nombre1 = liste_message[i]
        nombre2 = clef_liste_final[i]
        nombre3 = nombre1 + nombre2

        if nombre3 > len(caractère) - 1 :
            #print(nombre3)
            nombre4 = len(caractère)
            nombre3 = nombre3 - int(nombre4)
            #print(nombre3)
        final_liste.append(nombre3)
        i = i + 1
    #print(final_liste)

    #Convertir en lettre
    i = 0
    while i < len(final_liste) :
        final_liste[i] = caractère[int(final_liste[i])]
        #print(final_liste)
        i = i + 1

    final = "".join(final_liste)

    return final

def decryptage(ms,cl) :
  if True :
    """
        Ce code va permettre de décrypter les messages en fonction de la clef
    """
    # Transformer en chiffre le message
    message = str(ms)
    if message == "":
        print("L,utilisateur doit remplir la case message")
    else:
        liste_message = list(message)
        #print(liste_message)
        i = 0
        total = len(liste_message)
        while i < total:
            lettre = liste_message[i]
            position = caractère.index(str(lettre))
            liste_message[i] = position
            i = i + 1
        #print(liste_message)
    # Transformer en chiffre la clef
    clef = str(cl)
    if clef == '':
        print('l utilisateur doit remplir la case clef')
    else:
        liste_clef = list(clef)
        #print(liste_clef)
        i = 0
        total = len(liste_clef)
        while i < total:
            lettre = liste_clef[i]
            position = caractère.index(str(lettre))
            liste_clef[i] = position
            i = i + 1
        #print(liste_clef)

    # Mettre la clef a la longueur de message
    i = 0
    tour = 0
    clef_liste_final = []
    longueur = len(liste_message)
    while tour < longueur:
        if i > len(liste_clef) - 1:
            i = 0
        clef_liste_final.append(liste_clef[i])
        i = i + 1
        tour = tour + 1
    #print(clef_liste_final)

    # ASoustraire les deux listes
    final_liste = []
    i = 0
    #print(len(caractère))
    while i < len(liste_message):
        nombre1 = liste_message[i]
        nombre2 = clef_liste_final[i]
        nombre3 = nombre1 - nombre2

        if nombre3 < 0 :
            #print(nombre3)
            nombre4 = len(caractère)
            nombre3 = nombre3 + int(nombre4)
            #print(nombre3)
        final_liste.append(nombre3)
        i = i + 1
    #print(final_liste)

    # Convertir en lettre
    i = 0
    while i < len(final_liste):
        final_liste[i] = caractère[int(final_liste[i])]
        #print(final_liste)
        i = i + 1

    final = "".join(final_liste)

    return final