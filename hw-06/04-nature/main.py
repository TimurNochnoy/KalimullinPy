k = 0

for i in range(30, 36):
    n = int(input('Людей в ' + str(i) + '-м секторе: '))
    if n > 10:
        k += 1
        print('Нарушение! Слишком много людей в секторе!')
    else:
        print('Всё спокойно.')

print('Количество нарушений:', k)