class silnik:
    '''silnik'''
    def __init__(self, rodzaj_paliwa='----', pojemnosc_silnika = '----', **kwargs):
        super(silnik, self).__init__(**kwargs)            #wywołanie __init__ z klasy nadrzednej,
        self.__pojemnosc_silnika=pojemnosc_silnika        #dzięki **kwargs można przekazywać różną liczbe argumentów 
        self.__rodzaj_paliwa=rodzaj_paliwa 
    def set_pojemnosc_silnika(self, pojemnosc_silnika = '----'): #set_ - metody do ustawiania atrybutów prywatnych
        self.__pojemnosc_silnika=pojemnosc_silnika
    def set_rodzaj_paliwa(self,rodzaj_paliwa = '----'):
        self.__rodzaj_paliwa=rodzaj_paliwa     
    def get_info(self):                                  #metoda zwraca słownik z atrybutami prywatnymi tej klasy i ew. klasy nadrzędnej 
        silnik_details={"pojemnosc silnika":self.__pojemnosc_silnika,"rodzaj paliwa":self.__rodzaj_paliwa}
        if hasattr(super(), 'get_info'):                 #sprawdzenie czy klasa nadrzędna ma atrybut/metodę get_info()
           silnik_details.update(super().get_info())     #wywolanie get_info() z klasy nadrzednej - pobranie jej atrybutów prywatnych
        return silnik_details
           
class kolo:
    '''kolo'''
    def __init__(self,rozmiar_kola='----',rodzaj_felgi='----', **kwargs):
        super().__init__(**kwargs)
        self.__rozmiar_kola=rozmiar_kola
        self.__rodzaj_felgi=rodzaj_felgi
    def set_rozmiar_kola(self,rozmiar_kola='----'):
        self.__rozmiar_kola=rozmiar_kola
    def set_rodzaj_felgi(self,rodzaj_felgi='----'):
        self.__rodzaj_felgi=rodzaj_felgi 
    def get_info(self):
        kolo_details={"rozmiar_kola":self.__rozmiar_kola,"rodzaj felgi":self.__rodzaj_felgi}
        if hasattr(super(), 'get_info'):
            kolo_details.update(super().get_info())
        return kolo_details

class skrzynia:
    '''skrzynia'''
    def __init__(self,typ_skrzyni='----',biegi_skrzyni='----', **kwargs):
        super().__init__()
        self.__typ_skrzyni=typ_skrzyni
        self.__biegi_skrzyni=biegi_skrzyni 
    def set_typ_skrzyni(self,typ_sprzegla='----'):
        self.__typ_sprzegla=typ_sprzegla 
    def set_biegi_skrzyni(self,biegi_skrzyni='----'):
        self.__biegi_skrzyni=biegi_skrzyni   
    def get_info(self):
        skrzynia_details={"typ skrzyni":self.__typ_skrzyni,"biegi skrzyni":self.__biegi_skrzyni}
        if hasattr(super(), 'get_info'):                   
           skrzynia_details.update(super().get_info())     
        return skrzynia_details    

class samochod(silnik,kolo,skrzynia):      #kolejność nadrzędnych klas określa kolejność wywoływania metod za pomocą funkcji super(), tzw. MRO       
    '''samochod osobowy'''                 #kolejność wywołań funkcji __init__() z hierarchii klas: osobowy->silnik->kolo->skrzynia->object
    def __init__(self, marka_samochodu='----', typ_nadwozia='----', **kwargs):
        super().__init__(**kwargs)
        self.__marka_samochodu=marka_samochodu
        self.__typ_nadwozia=typ_nadwozia
    def set_marka(self,marka_samochodu='----', typ_nadwozia='----'):
        self.__marka_samochodu=marka_samochodu
    def set_typ_nadwozia(self,typ_nadwozia='----'):
        self.__typ_nadwozia=typ_nadwozia       
    def get_info(self):                  #metoda zwraca wszystkie atrybuty prywatne z hierarchii klas w formie słownika - konieczne
                                         #wywołanie metod get_info z klas nadrzędnych
        detail_info={"marka samochodu":self.__marka_samochodu, "typ nadwozia":self.__typ_nadwozia}
        if hasattr(super(), 'get_info'):
           detail_info.update(super().get_info())
        detail_info.update(super().get_info())    
        return detail_info    
    def __str__(self):
        l=[]
        for k,v in self.get_info().items():
           l.append(str(k)+ ': ' + str(v))           
        return '\n'.join(l)   
     
#----------------------        
print('\nPrzykład 1:\n')
sam1=samochod("Fiat","sedan")
print(sam1)
print(sam1.get_info(),'\n')

print('\nPrzykład 2:\n')
sam2=samochod(
marka_samochodu='Ford',
typ_nadwozia='sedan',
pojemnosc_silnika=1600,
rodzaj_paliwa="benzyna", 
rozmiar_kola=17,
rodzaj_felgi='alu', 
typ_skrzyni="manual",
biegi_skrzyni=6
)
print(sam2)
print(sam2.get_info(),'\n')

#zmiana atrybutów prywatnych        
sam2.set_rodzaj_paliwa("kombii")
sam2.set_rozmiar_kola(16)

print(sam2)
print(sam2.get_info(),'\n')

#MRO:
print("\nMRO - Method Resolution Order:")
print(samochod.mro())

