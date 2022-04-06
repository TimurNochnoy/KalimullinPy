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

for kid, parent in pedigree.items():
    root = parent
    depth = 1
    while root not in res:
        root = pedigree[root]
        depth += 1
    res[kid] = res[root] + depth

print('“Высота” каждого члена семьи:')
for key in sorted(res):
    print(key, res[key])
