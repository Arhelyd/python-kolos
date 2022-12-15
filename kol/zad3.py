def gen_napisow(napis):
    for x in napis:
        yield x


for a in gen_napisow('test'):
    print(a)

