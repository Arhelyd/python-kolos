import os

lista=os.listdir('.')

print('lista wszystkich plikow:')
print(lista)

def gen_py():
    for f in os.listdir('.'):
        if f.endswith('.py'):
            yield f

for f in gen_py():
    print(f)

