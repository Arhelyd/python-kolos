def map(fun, list):
    return [fun(item) for item in list]

def add100(x):
    return x+100

lista_0_9=list(range(10))

map(add100, lista_0_9)

map(lambda x: x+100, range(10))