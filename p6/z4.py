import json
import yaml
with open("netplan.yaml", "r") as file:
    persons= yaml.load(file)
   # print(persons['network'])
   # print(type(persons))
    
#print([persons['network']]['adresses'])
persons['network'].pop('addresses')
persons['network'].update()
#print(persons['network'])

persons['network']['addresses'] = ['1.1.1.1', '8.8.8.8', '4.4.4.4.3']
persons['network'].update()
#print(persons['network'])

with open('netplan.yaml', 'w') as yml:
    yaml.dump(persons, yml)




