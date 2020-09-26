file = open('dicoFR1.txt','r')
c = file.read().split('\n')
file.close()

while True :
    s = input('-> ')
    if s in c :
        t = 0
        for i in c :
            if i == s :
                t = t + 1
        print('Ce mot ext dans la liste se nombre de fois -> ' + str(t))
    else :
        print('NON')