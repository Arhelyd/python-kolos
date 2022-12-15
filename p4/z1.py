

def func(nazwa_pliku,zmienna):
    try:
       # print(nazwa_pliku)
        f=open(nazwa_pliku,'r')
        #print(f.readline())
    except:
        print('nie mozna otworzyc pliku')
    else:
        z=f.readline()
        while(z):
            count=0
            for x in z:
                count+=1
                print(x, sep='', end='')
                if(count==zmienna):
                    print('')
                    count=0
            if(count==0):
                print('')
            z=f.readline()

func('plik_zad1.txt',10)
        
