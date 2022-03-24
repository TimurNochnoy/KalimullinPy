N = int(input('Введите количество человек: '))
pedigree = dict()
for i in range(N - 1):
    print(i + 1, 'пара:', end=' ')
    kid, parent = input().split()
    pedigree[kid] = parent

res = dict()
for name_v in pedigree.values():
    if name_v not in pedigree.keys():
        res[name_v] = 0
for name_k in pedigree.keys():
    res[name_k] = res[pedigree[name_k]] + 1

print('“Высота” каждого члена семьи:')
for key in sorted(res):
    print(key, res[key])
