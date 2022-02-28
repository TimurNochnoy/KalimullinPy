past = 0
f = 0

for i in range(10):
    n = int(input())
    if n < past:
        f = 1
    past = n

if f == 1:
    print('Не упорядочены по возрастанию.')
else:
    print('Упорядочены по возрастанию.')