
def funkcja():    
    x=int(input('podaj liczbe'))
    #x=input('podaj liczbe')
    try:
        wynik=x**0.5
        #wynik/0
    #except ZeroDivisionError as ex:
    #    print(f'Wyjatek1 {ex}')
    except TypeError as ex:
        print(f'Wyjatek1 {ex}')
    except NameError as ex:
        print(f'Wyjatek2 {ex}')
    except OverflowError as ex:
        print(f'Wyjatek3 {ex}')
    #except FloatingPointError as ex:
     #   print(f'Wyjatek4 {ex}')
        
    else: print('bez wyjatkow')
        
funkcja()
