#wywołanie: py zad4.py k1
import sys

try:
    mykey=sys.argv[1]
except:
    print('Problem z parametrem!')
    exit()    
    
try:
    f = open('plik4.txt')
    nap=f.read()
    f.close()
except:
    print('Problem z plikiem!')
    exit()

def str3dict(nap):
    l=nap.split('\n')
    d={}
    for kv in l:
        kr=kv.split(':')
        d[kr[0]]=kr[1]
    return d    
        
mydict=str3dict(nap)
print(mydict)

try:
    print("%s = %s"  %(mykey,mydict[mykey]))
except:
    print('Problem z kluczem!')    
    
print("%s = %s"  %(mykey,mydict.get(mykey, 'Problem z kluczem!')))
