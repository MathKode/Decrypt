"""
t = input(":")
tl = t.split('\n')
file = open("liste.txt","r")
c = file.read().split("\n")
file.close()

print(tl)
for i in tl :
    if i in c :
        o = 0
    else :
        c.append(i)
f = open("liste.txt","w")
for i in c :
    f.write(str(i) + "\n")
f.close()
"""


import os
import PyPDF2
chemin = "Pdf/"
listfile = os.listdir("Pdf/")
print(listfile)
for pdf in listfile :
    f = open(str(chemin) + str(pdf),'rb')

    print(PyPDF2.PdfFileReader(f))
