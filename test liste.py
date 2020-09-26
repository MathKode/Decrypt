import io

print(file.read())
file.close()
i = True
while i :
    mot = input('Mot : ')
    if mot in z :
        print('Non')
    else :
        print('Oui')