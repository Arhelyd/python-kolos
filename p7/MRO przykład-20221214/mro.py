class A():
    def m(self):
        print("A")
        super(A,self).m() # -> Error - object class has no method m()
        
class B():
    def m(self):
        print("B")
        super().m() # -> A
        
class C(B,A):
    def m(self):
        print("C")
        super(C,self).m()
        #super().m() # -> B

print(C.mro())        
c = C()
c.m()
