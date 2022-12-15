class Punkt2d():
    def __init__(self,x1_=0,x2_=0):
        self.point=[x1_,x2_]
        self.distance=self.countdistance()
    #def __call__(self,x1_,x2_):
       # self.__init(x1_,x2_)    
    def countdistance(self):
        xrob=0
        for xi in self.point:
            xrob+=xi*xi
        return xrob**0.5
    def countnewco(self,other):
        return [self.point[i]-other.point[i] for i in range(len(self.point))]    
    def __sub__(self, other):
        return Punkt2d(*self.countnewco(other)) 
    def __str__(self):
        return "({},{}), dystans={} ".format(self.point[0], self.point[1], self.distance)    
    
class Punkt3d(Punkt2d):
    def __init__(self,x1_=0,x2_=0,x3_=0):
        self.point=[x1_,x2_,x3_]
        self.distance=self.countdistance()
    def __call__(self,x1_,x2_,x3_):
        self.__init__(x1_,x2_,x3_)
    def __sub__(self, other):
       # print(self.__str__())
        return Punkt3d(*self.countnewco(other))      
    def __str__(self):
        #print("dopisany teksy",format(self.point[0],self.point[1],self.point[2],self.distance))
        return "({},{},{}), dystans={} ".format(self.point[0],self.point[1],self.point[2],self.distance)    
               
               
print("--2D--")
pa=Punkt2d(-2,0)
pb=Punkt2d(2,0)
print('lll')
print(pa)
print('llll')
print("pa=%s" %pa)
print("pb=%s" %pb)
print("distance pa-pb = %s" %(pa-pb))
print("distance pb-pa = %s" %(pb-pa))


print()
print("--3D--")
pa=Punkt3d(2,2,2)
pb=Punkt3d()
pb(-2,-2,-2)
print("pa=%s" %pa)
print("pb=%s" %pb)
print("distance pa-pb = %s" %(pa-pb))
print("distance pb-pa = %s" %(pb-pa))

	   
