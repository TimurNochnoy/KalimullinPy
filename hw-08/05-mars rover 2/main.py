x = 8
y = 10
print('Марсоход находится на позиции', x, y, 'введите команду:')
s = input()
while s != 'stop':
    if (s == 'W') and (y + 1 <= 20):
        y += 1
    if (s == 'S') and (y - 1 >= 0):
        y -= 1
    if (s == 'A') and (x - 1 >= 0):
        x -= 1
    if (s == 'D') and (x + 1 <= 15):
        x += 1
    print('Марсоход находится на позиции', x, y, 'введите команду:')
    s = input()
