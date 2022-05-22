import glob
import os
phones = ['a', 'i', 'u', 'oo', 'e', 'ae', 'ia', 'ua', 'ooa', 'o', 'oh', 'eh', 'ai', 'ao', 'N', 'cl', 'pau', 'br', 'vf', 'sil', 'exhale', 'NG', 'M', 'gcl', 'bcl', 'dcl', 'g', 'k', 'n', 'g', 'j', 'sh', 's', 'd', 't', 'th', 'n', 'b', 'p', 'ph', 'f', 'm', 'r', 'y', 'l', 'w', 'h', 'gr', 'gl', 'gw', 'kr', 'kl', 'kw', 'tr', 'tl', 'tw', 'pr', 'pl', 'pw', 'phr', 'phl', 'phw']

for file in glob.glob('*.lab'):
    with open(file) as f:
        i = f.readline()
        line_count = 1
        while i:
            p = i.strip().split()
            i = f.readline()
            if p[-1] not in phones:
                print(f'In {file}: {p[-1]} is not in the list. At line {line_count}')

            if int(p[0]) == int(p[1]):
                print(f'In {file}: {p[-1]} has the same start and end. At line {line_count}')
            line_count += 1

os.system('pause')
