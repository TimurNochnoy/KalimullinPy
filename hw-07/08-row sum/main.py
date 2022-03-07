N = int(input('Введите натуральное число N: '))
s = 0
for i in range(N + 1):
    s += ((-1) ** (i)) * 1 / (2 ** i)
print(s)