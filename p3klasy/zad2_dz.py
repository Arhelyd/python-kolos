class A:
    def info(self):
        print("Klasa A")
        super().info()

class B:
    def info(self):
        print("Klasa B")
        #super().info()
        
class C:
    def info(self):
        print("Klasa C")
        super().info()
        
class D(A,C,B):
    def info(self):
        print("Klasa D")
        super().info()
        
D_obj=D()
D_obj.info()

#print(D.mro())

        
