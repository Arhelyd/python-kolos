import subprocess

srcdir = ".\\scripts\\"

lista_skryptow = []
lista_skryptow_ok = []
lista_skryptow_bad = []

try:
    out = subprocess.run(["dir", '/B', srcdir + '\\*.py'],
                         shell=True, check=True,
                         stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    lista_skryptow = out.stdout.decode('cp852').split()
except (subprocess.CalledProcessError) as ex:
    print(ex)


for skrypt in lista_skryptow:
    try:
        out = subprocess.run(["py", srcdir + skrypt], shell=True, check=True,
                             stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        lista_skryptow_ok.append(skrypt)
    except subprocess.CalledProcessError:
        lista_skryptow_bad.append(skrypt)

print('srcdir: ', srcdir, '\n')
print('ALL: ', lista_skryptow)
print('OK: ', lista_skryptow_ok)
print('BAD: ', lista_skryptow_bad)
