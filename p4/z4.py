import re

def plec(x):
    if x%2==1:
        return 'mezczyzna'
    else:
        return 'kobieta'

    

def walidator(pesel):
    if(len(pesel)!=11):
        print('niepoprawna dlugosc peselu')
        return
    try:
        int(pesel)
    except:
        print('pesel nie sklada sie z samych cyfr')
    else:
        
        value=pesel+'0'
        result=re.findall("\d\d", value)
        suma=0
        suma=(9*int(result[0][0])+7*int(result[0][1])+3*int(result[1][0])+1*int(result[1][1])+9*int(result[2][0])+7*int(result[2][1])+3*int(result[3][0])+1*int(result[3][1])+9*int(result[4][0])+7*int(result[4][1]))
       # print(suma)      
        kontrolna=suma%10
        #print(kontrolna)
        if str(kontrolna)!=result[5][0]:
           print('niepoprawna suma kontrolna')
           return
        if int(result[1][0])-2 >= 0 :
            
            zamiana=str((int(result[1][0])-2))
            
            print(result[2],'-',zamiana+result[1][1],'-','20'+result[0],plec(int(result[4][1])))
        else:    
            print(result[2],'-',result[1],'-','19'+result[0],plec(int(result[4][1])))





print('0 przerywa wpisywanie peseli')    
while True:
    x = input()
    if(x=='0'):
        break
    walidator(x)
    
