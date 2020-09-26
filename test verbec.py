from verbecc import Conjugator
c = ["vouloir","bonjour","vas"]
cg = Conjugator(lang='fr')
for verbe in c :
    try :
        result = cg.conjugate(verbe)
        print(result)
        ls = []
        temps = result['moods']['indicatif'].keys()
        print(temps)
        for t in temps :
            conjugaison = result['moods']['indicatif'][str(t)]
            print(conjugaison)
            ls = ls + conjugaison
        print(ls)
    except :
        print(verbe + " n'est pas un verbe")

