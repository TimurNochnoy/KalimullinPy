n = int(input('Введите количество минут: '))
h = n // 60
n -= h * 60
print(h, n)