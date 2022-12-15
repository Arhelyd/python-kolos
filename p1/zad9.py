def cezar(wyraz,n):
    rob_tab=[]
    for znak in list(wyraz):
        if ord(znak) >= 97 and ord(znak) <= 123:
            rob_tab.append(chr(97+(ord(znak)-97+n)%26))
        else:    
            rob_tab.append(znak)     
    return ''.join(rob_tab)
    
f1=open('plik1',"rt")
f2=open('plik2',"wt")
for line in f1:
    line_tab=[]
    for wyraz in line.split():
        line_tab.append(cezar(wyraz,3))
    f2.write(' '.join(line_tab))
    f2.write('\n')
f1.close()
f2.close()

