import subprocess

dirStr = '''
K1
_K2
_K3
__K4
K5
_K6
'''


def parse(dir_str):
    dir_list = dir_str.split()

    prev_path = [dir_list[0]]
    if prev_path[0].startswith('_'):
        return []

    for i in range(1, len(dir_list)):
        # str->list, np.:'__K4' -> ['_','_','K4']
        # ---
        current_path = []
        dirname = dir_list[i]
        n = 0
        while dirname[n] == '_':
            current_path.append(dirname[n])
            n += 1
        current_path.append(dirname[n:])
        # ---
        for j in range(len(current_path)):
            if len(current_path) - len(prev_path) > 1:
                return []
            if current_path[j] == '_':
                current_path[j] = prev_path[j]
        prev_path = current_path
        dir_list[i] = '\\'.join(current_path)
    return dir_list


dl = parse(dirStr)
print(dl)

exit()

for d in dl:
    try:
        out = subprocess.run(["mkdir", d], shell=True, check=True)
    except (subprocess.CalledProcessError) as ex:
        print(ex)
