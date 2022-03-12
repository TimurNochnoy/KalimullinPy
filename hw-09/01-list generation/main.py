N = int(input('Введите число: '))
lst_odd = []
for i in range(1, N + 1, 2):
    lst_odd.append(i)
print('Список из нечётных чисел от одного до N:', lst_odd)
