print("podaj liczbe:")
n=int(input())
#n=3

for z in range(65,91,n):
    print(chr(z+32),chr(z), sep='', end='')