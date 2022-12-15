import subprocess


kat = '.\\scripts'
# kat = '.\\asdf'   #generuje błąd

try:
    out = subprocess.run(["dir", kat], shell=True, check=True,
                         stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    print(out.stdout.decode('cp852'))
except (subprocess.CalledProcessError) as ex:
    print(ex)
