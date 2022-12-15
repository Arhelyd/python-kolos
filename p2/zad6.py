def dzien_tygodnia(data):
    rok,miesiac,dzien=data
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

print(dzien_tygodnia((2021,3,10)))
        