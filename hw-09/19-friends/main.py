N = int(input('Кол-во друзей: '))
K = int(input('Долговых расписок: '))
print()
lst_debt = [0 for i in range(N)]
for i in range(K):
    print(i + 1, 'расписка')
    x = int(input('Кому: '))
    y = int(input('От кого: '))
    s = int(input('Сколько: '))
    lst_debt[x - 1] -= s
    lst_debt[y - 1] += s
print('\nБаланс друзей:')
for i in range(N):
    print(str(i + 1) + ':', lst_debt[i])
