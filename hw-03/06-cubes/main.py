a = int(input('Кубик Кости: '))
b = int(input('Кубик владельца: '))
if a >= b:
    print('Разность:', a - b)
    print('Костя платит')
else:
    print('Сумма:', a + b)
    print('Владелец платит')
print('Игра окончена')