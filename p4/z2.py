

def func(nazwa_pliku,zmienna):
    try:
       # print(nazwa_pliku)
        f=open(nazwa_pliku,'r')
        #print(f.readline())
    except:
        print('nie mozna otworzyc pliku')
    else:
        z=f.readline().split(' ')
        while(True):
            
        
        
            for x in z:
               # count+=1
                print(x.strip().center(zmienna))
                #if(count==zmienna):
                  #  print('')
                  #  count=0
            #if(count==0):
            z=f.readline()
            if(z==''):
                break
            z=z.split(' ')       # print('')

func('plik_zad2.txt',5)
        
# nie rozdziela wyrazów a powinien - mój, ten spokoo
