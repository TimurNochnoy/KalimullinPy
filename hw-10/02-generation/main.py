N = int(input('Введите длину списка: '))
res = []
for i in range(N):
    if i % 2 == 0:
        res.append(1)
    if i % 2 == 1:
        res.append(i % 5)
print(res)
