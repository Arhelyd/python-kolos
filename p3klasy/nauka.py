class A( object ):
     def funkcja ( self ):
         print("Wywolanie A")
class B(A):
    def funkcja ( self ):
        print("Wywolanie B")
        super(B,self).funkcja() #wywołanie metody z klasy nadrzędnej

kb=B()
kb.funkcja()
