def licz2(nap):
    return [(n,len(n)) for n in nap.split()]
    
#tekst=input()    
tekst='jeden dwa trzy cztery piec'
print("licz2:");
print(licz2(tekst))

    