import math

def sortuj(p1_punkty):
    return sorted(p1_punkty, key=lambda z: math.sqrt(z[0]**2+z[1]**2))
    
punkty=[(1.0,1.1),(10.0,1.0),(3.0,2.0),(2.0,1.0),(8.0,1.0),(4.0,1.0),(2.0,2.0)]             
print('przed sortowaniem:')
print(punkty)
print('po sortowaniu:')
print(sortuj(punkty))
    
