def dni_tygodnia(*daty1, **daty2):
    def dzien_tygodnia(rok, miesiac, dzien):
        c,z=0,0
        if miesiac < 3:
            z=rok-1
            c=0
        else:
            z=rok
            c=2
        dt = ((23*miesiac)//9 + dzien + 4 + rok + z//4 + z//100 + z//400 - c) % 7
        dtw=('wtorek','sroda','czwartek','piatek','sobota','niedziela','poniedzialek')
        return dtw[dt]
    data_dzien={}
    for data in daty1:
        data_dzien[(data)]=dzien_tygodnia(*data)
    for nazwa,data in daty2.items():
        data_dzien[(data)]=dzien_tygodnia(*data)    
    return data_dzien    

print(dni_tygodnia((2020,3,11),(2021,3,17),data1=(2023,3,10),data2=(2024,3,11)))
        