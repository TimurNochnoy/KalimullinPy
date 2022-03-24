N = int(input('Введите максимальное число: '))
data = dict()
for i in range(N):
    data[i + 1] = 2
s = input('Нужное число есть среди вот этих чисел: ').split()
f = 0
while s != ['Помогите!']:
    a = input('Ответ Артёма: ')
    for elem in s:
        if a == 'Да' and int(elem) in data:
            data[int(elem)] = 1
        if a == 'Нет' and int(elem) in data:
            data[int(elem)] = 0
    if len(s) == 1 and a == 'Да':
        print('Число угадано.')
        s = ['Помогите!']
        f = 1
    else:
        s = input('Нужное число есть среди вот этих чисел: ').split()
if f == 0:
    print('Артём мог загадать следующие числа: ', end='')
    for key in data:
        if data[key] == 1:
            print(key, end=' ')
