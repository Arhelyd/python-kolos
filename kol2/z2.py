
f = open("kol2/demofile.txt", "r")

print(f.readlines())
f = open("kol2/demofile.txt", "r")
for x in f.readlines():
    print(x)
    #print(x.split())