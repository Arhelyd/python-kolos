def infinite_sequence():
    num = 0
    while True:
        print("test")
        yield num
        print("wartosc "+str(num))
        num += 1
        print("test2")

gen = infinite_sequence()
next(gen)
print('-----')
next(gen)
print('-----')
#next(gen)
#next(gen)