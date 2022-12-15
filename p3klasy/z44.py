class A( object ):
     def funkcja ( self ):
         print("Wywolanie A")

class C( object ):
     def funkcja ( self ):
         print("Wywolanie C")
         
class B(C,A):
    def funkcja ( self ):
        print("Wywolanie B")
        super(B,self).funkcja() #wywołanie metody z klasy nadrzędnej
        #potrzebuje self i tej klasy z ktorej jest wywolywany

kb=B()
kb.funkcja()

