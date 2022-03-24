N = int(input('Введите кол-во заказов: '))
orders = dict()
for i in range(N):
    print(i + 1, 'заказ: ', end='')
    s = input().split()
    if s[0] in orders:
        if s[1] in orders[s[0]]:
            orders[s[0]][s[1]] += int(s[2])
        else:
            orders[s[0]][s[1]] = int(s[2])
    else:
        orders[s[0]] = {s[1]: int(s[2])}

for name in orders:
    print(name + ':')
    for pizza in orders[name]:
        print('\t', pizza + ':', orders[name][pizza])
