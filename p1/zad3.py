nap='''k1:v1
k2:v2
k3:v3'''

def str3dict(nap):
    l=nap.split()
    print(l)
    d={}
    for kv in l:
        kr=kv.split(':')
        d[kr[0]]=kr[1]
    return d

print(str3dict(nap))
#{'k1': 'v1', 'k2': 'v2', 'k3': 'v3'}

my_dict=str3dict(nap)

print(my_dict)
#{'k1': 'v1', 'k2': 'v2', 'k3': 'v3'}

print(type(my_dict))
#dict
