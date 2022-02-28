n = int(input('Введите число: '))
k = 1

if n == 0:
    print(1)
else:
    for i in range(1, n):
        i += 1
        k *= i
    print(k)