n = int(input('Введите число: '))
if (abs(n) // 100 == 0) and (abs(n) // 10 != 0):
    print('OK')
else:
    print('Error')