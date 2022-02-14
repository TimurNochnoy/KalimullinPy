mileage = int(input('Введите пробег: '))
date = int(input('Введите сегодняшнее число: '))
sum = mileage % 10 + (mileage // 10) % 10 + mileage // 100
if sum > date:
    print('Сброс.')
    mileage = 0
else:
    print('Сегодня не сломался.')
print('Пробег:', mileage)