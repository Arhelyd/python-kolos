def func(napis):
   lista=[]
   for x in napis:
      if x == '-':
         lista.append('_')
      else:
         lista.append(x)
   wyraz=''.join(lista)
   return wyraz


print(func('P-y-t-h-o-n'))
         
      
