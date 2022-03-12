N = int(input('Кол-во человек: '))
K = int(input('Какое число в считалке? '))
print('Значит, выбывает каждый', K, 'человек\n')
lst_round = [i+1 for i in range(N)]
start = 0
while len(lst_round) > 1:
    print('Текущий круг людей:', lst_round)
    print('Начало счёта с номера', start + 1)
    index = (start + K - 1) % len(lst_round)
    print('Выбывает человек под номером', lst_round[index], '\n')
    start = index % len(lst_round)
    lst_round.pop(index)
print('Остался человек под номером', lst_round[0])
