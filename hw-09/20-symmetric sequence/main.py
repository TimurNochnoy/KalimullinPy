N = int(input('Кол-во чисел: '))
lst_in = []
for i in range(N):
    x = int(input('Число: '))
    lst_in.append(x)
print('Последовательность:', end=' ')
for elem in lst_in:
    print(elem, end=' ')
print()
f = -1
for i in range(len(lst_in)):
    if lst_in[i:len(lst_in) - 1] == lst_in[len(lst_in) - 1:i:-1] and f == -1:
        f = i
print('Нужно приписать чисел:', f)
print('Сами числа:', end=' ')
for i in range(f - 1, -1, -1):
    print(lst_in[i], end=' ')
print()
