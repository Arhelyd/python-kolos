import re
class Wyjatek(Exception):
    print("no nie wyszlo")
class klasa:
    email=''
    def __init__(self,em):
        wzor = r"[a-z]@gmail.com"
   
        if re.match(r".*"+wzor,em): 
            self.email=em
            print(em)
        else:
            raise Wyjatek()
            return



adres=klasa(r'abdc@gmail.com')
adres=klasa(r'j.kowalski.@gmail.com')



