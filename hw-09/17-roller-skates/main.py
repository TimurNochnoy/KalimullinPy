N = int(input('Кол-во коньков: '))
lst_roller = []
for i in range(N):
    print('Размер', i + 1, 'пары:', end=' ')
    n = int(input())
    lst_roller.append(n)
lst_roller.sort()
K = int(input('Кол-во людей: '))
lst_skater = []
for i in range(K):
    print('Размер ноги', i + 1, 'человека:', end=' ')
    n = int(input())
    lst_skater.append(n)
lst_skater.sort()
lst_size = []
for elem in lst_roller:
    if elem >= min(lst_skater):
        lst_size.append(elem)
k = 0
for foot in lst_roller:
    f = 0
    for size in lst_size:
        if foot <= size and f == 0:
            lst_size.remove(size)
            f = 1
            k += 1
print('Наибольшее кол-во людей, которые могут взять ролики:', k)
