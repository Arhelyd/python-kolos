#zm=int(input())
zm=11

def fibo(n):
    a,b=0,1
    
    while n:
       # print(a,b)
        a,b=b,a+b
        #print(a,b)
        n-=1
    return a    

l=[fibo(n) for n in range(zm)]

print(l)     
