N = int(input('Кол-во палок: '))
K = int(input('Кол-во бросков: '))
lst = [1 for i in range(N)]
for i in range(K):
    L_i = int(input('Бросок ' + str(i + 1) + '. Сбиты палки с номера '))
    R_i = int(input('по номер '))
    for j in range(L_i - 1, R_i):
        lst[j] = 0
print('Результат: ', end='')
for elem in lst:
    if elem == 1:
        print('|', end='')
    if elem == 0:
        print('.', end='')
print()
