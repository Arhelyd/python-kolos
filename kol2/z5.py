def generator(n):
    while n:
        print("zwracam watosc" + str(n))
        yield n
        n-=1


x=generator(5)
generator(5)
print(x)
print(list(x))# czemu trzeba dać ten list ?


generator=((x,2*x) for x in range(10))
for a,b in generator:
    print(a,b)


import time
for x in generator(10):
    time.sleep(0.5)
    print('Wypisuję %d w pętli.' %x)
    time.sleep(0.5)

