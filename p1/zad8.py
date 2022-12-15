print("podaj ciak znakow:")
wyraz=input()

#lub:
#wyraz='xyz'
#print(wyraz)

#przesunięcie:
n=13
#print(wyraz)
#print(list(wyraz))
rob_tab=[]
for znak in list(wyraz):
    if ord(znak) >= 97 and ord(znak) <= 123:
        rob_tab.append(chr(97+(ord(znak)-97+n)%26))
    else:    
        rob_tab.append(znak)
        
print(''.join(rob_tab))
print((rob_tab))
