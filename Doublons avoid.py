file = open('dicoFR1.txt','r')
c = file.read().split('\n')
file.close()
f = []
for i in c :
    j = i.split(' ')
    for hy in j :
        f.append(hy)
print(f)
d = list(set(f))
print(d)
tour = 0
file = open("dicoFR1.txt", 'w')
for word in d :
    if tour == 0:
        file.write(word)
    else:
        file.write('\n' + word)
    tour = tour + 1
file.close()
print('FIN de la suppression des Doublons')