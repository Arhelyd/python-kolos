def podzielne_przez_3_7(x):
    if x%3==0 and x%7==0:
        return True
    else:    
        return False	   
    
def filter(funkcja, lista):
    return [x for x in lista if funkcja(x)]
    
liczby=[1,10,30,21,81,48,42]
print("wejście:")
print(liczby)
print("wyjście:")
print(filter(podzielne_przez_3_7,liczby))

    