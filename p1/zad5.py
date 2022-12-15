#wywołanie 1: py zad4.py plik5.txt hello
#wywołanie 2: py zad5.py - hello

import sys

szukaj=sys.argv[2]
napis=''
lines=[]

if sys.argv[1] == '-':
    #input() 
    #   - pobier i zwraca jedną linię
    #sys.stdin.readlines() - pobiera wiele linii i zwraca listę 
    #   - koniec wczytywanie po napotkaniu znaku EOF z klawiatury
    #   - 'CTRL-D' (linux) 'CTRL-Z + ENTER' (win)  
    lines=sys.stdin.readlines()
else:
    plik=sys.argv[1]    
    f = open(plik,'rt',encoding='utf8')
    lines=f.readlines()
    f.close();
    
print("\nwejscie:\n%s \n" %(''.join(lines)))
    
print("ROZW. I:")
robtab=[]
for line in lines:
    robtab=line.split()
    for wyraz in robtab:
        if wyraz == szukaj:
            print(line)

print("ROZW. II:")
for line in lines:
    if line.split().count(szukaj):
        print(line)

