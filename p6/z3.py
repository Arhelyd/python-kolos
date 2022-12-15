import json
import pickle

polecenie = input("Podaj J- odczyt JSON\ P- odczyt PICKLE")
    
if polecenie == "J" or polecenie == "j":
    with open("persons.json", "r") as file:
        persons= json.load(file)

if polecenie == "P" or polecenie == "p":
    with open('persons.pickle', 'rb') as file:
        persons= pickle.load(file)
        

#print(persons)
#print(type(persons))
#print(type(persons[1]))

polecenie = input("Podaj J- zapis JSON\ P- zapis PICKLE")
    
if polecenie == "J" or polecenie == "j":
    with open('persons.json', 'w') as json_file:
        json.dump(persons, json_file)
        
        
if polecenie == "P" or polecenie == "p":
    with open('persons.pickle', 'wb') as pickle_file:
        pickle.dump(persons, pickle_file)
        
    




