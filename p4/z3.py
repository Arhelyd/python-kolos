import re




def wypiszpoprawne(ip):
    for x in ip:
        x=x.split('.')
        
        
        test=1
        for y in x:
          #  print(y)
            if(int(y) >= 0 and int(y) <= 255):
                pass
            else:
                test=0
        if test==1:
            scal=x[0]+'.'+x[1]+'.'+x[2]+'.'+x[3]
            print(scal)
                
            
                

        
    
   # dopasowanie2=re.match(r'^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$',ip)
    #if dopasowanie2:
    #    print(dopasowanie2)

def func(nazwa_pliku):
    try:
       # print(nazwa_pliku)
        f=open(nazwa_pliku,'r')
        #print(f.readline())
    except:
        print('nie mozna otworzyc pliku')
    else:
        tekst=f.read()
        wzorzec = r' \d\d*\.\d\d*\.\d\d*\.\d\d* '
        #while(True):
        dopasowanie = re.findall(wzorzec, tekst)
        if dopasowanie:
            #print (dopasowanie)
            wypiszpoprawne(dopasowanie)
            #print (dopasowanie)
              
            

        
func('plik_zad3.txt')

    
