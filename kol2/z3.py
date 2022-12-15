def gen_inc(n):
    def fun(x):
        return n+x
    return fun


inc5=gen_inc(5)
print(inc5(10))
inc5=gen_inc(4)
print(inc5(10))