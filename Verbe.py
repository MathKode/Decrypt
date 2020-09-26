###A N4EXECUTER QU4UNEFOIS
file = open("verbe.txt",'r')
c = file.read().split('\n')
file.close()
d = []
for el in c :
    ls = el.split(' - ')
    for j in ls :
        d.append(j)
print(d)
file = open("dicoFR1.txt", 'r')
c = file.read().split('\n')
file.close()
for i in d :
    if i == ' ' :
        sp = 'l'
    else :
        c.append(i)
        print(i)
tour = 0
file = open("dicoFR1.txt", 'w')
for word in c:
    if tour == 0:
        file.write(word)
    else:
        file.write('\n' + word)
    tour = tour + 1
file.close()
print('FIN de lajout des verbes')

