import os
from larousse_api import larousse
i = True
while i :
    mot = input('Mot : ')
    deff = larousse.get_definitions(str(mot))
    print(deff)
    if deff == [] :
        print('Non')
    else :
        print('Oui')