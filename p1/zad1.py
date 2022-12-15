#wywołanie np: py zad1.py 3
import sys

x=int(sys.argv[1])

if (x % 2) == 0:
   print("%d to liczba parzysta" %x)
else:
   print("%d to liczba nieparzysta" %x)
