class AddMul:
    def __init__(self,_liczba):
        self.liczba=_liczba
    def __mul__(self, _other):
        return AddMul(_other.liczba * self.liczba)
    def __add__(self, _other):
        return AddMul(_other.liczba + self.liczba)    
    def __str__(self):
        return str(self.liczba)
        
a=AddMul(5)
b=AddMul(5)
c=a*b
print(c, type(c))
print(a+b, type(a+b))



        