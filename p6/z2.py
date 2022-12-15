import json
import os
with open("persons.json", "r") as file:
    persons= json.load(file)
   # print(persons)
   # print(type(persons))
   # print(type(persons[1]))

    #print("\n\n")

#print(persons)

konwert=json.dumps(persons)

#print(konwert)
while True:
    polecenie = input("d - dodanie\nu - usuwanie\nz - zakoncz dzialanie\nw - wyswietl profile")
    if polecenie == "d":
        profil = input(r'podaj profil w takiej postaci: {"l_name": "", "f_name": "", "age": , "mynums": [0, 0]}')
        konwert=konwert[:-1]
        konwert += ', '+profil+']'
    if polecenie == "w":
        print(konwert)
    if polecenie == "u":
        profil = input("podaj profil, który ma być usunięty (cała kopia profilu {...})")
        if(konwert[konwert.find(profil)+len(profil)]==','):
            konwert=konwert[:konwert.find(profil)]+konwert[konwert.find(profil)+len(profil)+2:]
        else:
            konwert=konwert[:konwert.find(profil)]+konwert[konwert.find(profil)+len(profil):]
                
    if polecenie == "z":
        break




#print(konwert)
#print(type(konwert))
#res = json.loads(konwert)

konwert=konwert[1:-1]
persons=list(konwert.split(', {'))
dozapisu=[]
for x in persons:
    if(x[0] != '{'):
        x='{'+x

    dozapisu.append(json.loads(x))
    
os.unlink('persons.json')
with open('persons.json', 'w') as json_file:
    json.dump(dozapisu, json_file)




