n = int(input('Введите сумму: '))
if n >= 50000:
    print((n - 50000) * 0.3 + (50000 - 10000) * 0.2 + 10000 * 0.13)
elif (n >= 10000) and (n < 50000):
    print((n - 10000) * 0.2 + 10000 * 0.13)
else:
    print(n * 0.13)