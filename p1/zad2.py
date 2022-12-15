nap='k1:v1,k2:v2,k3:v3'

def str2dict(nap):
    l=nap.split(',')
    print(l)
    d={}
    ile=0
    for kv in l:
        ile+=1
        print(ile)
        kr=kv.split(':')
        d[kr[0]]=kr[1]
        print(d)
    return d

#print(str2dict(nap))
#{'k1': 'v1', 'k2': 'v2', 'k3': 'v3'}

my_dict=str2dict(nap)

#print(my_dict)
#{'k1': 'v1', 'k2': 'v2', 'k3': 'v3'}

#print(type(my_dict))
#dict
