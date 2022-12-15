class LZ():
    def __init__(self,a_=0,b_=0):
        self.a,self.b=(a_,b_)
    def __call__(self,a_=0,b_=0):
        self.a,self.b=(a_,b_)        
    def __add__(self, other):
        return LZ(self.a+other.a, self.b+other.b)
    def __sub__(self, other):
        return LZ(self.a-other.a, self.b-other.b)
    def __eq__(self, other):
       if self.a == other.a and self.b == other.b:
           return True
       else:
           return False
    def __mul__(self, other):
        return LZ(self.a*other.a-self.b*other.b, self.a*other.b +self.b*other.a)
    def __truediv__(self, other):
        mianownik=other.a**2+other.b**2
        return LZ((self.a*other.a+self.b*other.b)/mianownik, 
        (self.b*other.a-self.a*other.b)/mianownik)
    def modul(self):
        return (self.a*self.a+self.b*self.b)**0.5
    def __str__(self):
        return "(%.2f,%.2f)" %(self.a, self.b)   
    def __repr__(self):
        return "LZ(%f,%f)" %(self.a, self.b) 	   


za=LZ(1,1)
zb=LZ(2,2)	  

print("za=%s" %za)
print("zb=%s" %zb)
print("%s+%s=%s" %(za,zb,(za+zb)))
print("%s-%s=%s" %(za,zb,(za-zb)))
print("%s*%s=%s" %(za,zb,(za*zb)))
print("modul(za) = %s" %(za.modul()))
print("modul(zb) = %s" %(zb.modul()))
print("%s/%s=%s" %(za,zb,(za/zb)))

print('\n __repr__ example:')
zc_repr=repr(za+zb)
print(zc_repr)
zc=eval(zc_repr)
print("zc=%s" %zc)
print(type(zc)) 

	   
