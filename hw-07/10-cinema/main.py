X = int(input('Введите количество мальчиков: '))
Y = int(input('Введите количество девочек: '))
s = ''
if (X > 2 * Y) or (Y > 2 * X):
    print('Нет решения')
elif X >= Y:
    r = X - Y
    for i in range(Y - r):
        s += 'BG'
    for i in range(r):
        s += 'BGB'
else:
    r = Y - X
    for i in range(X - r):
        s += 'GB'
    for i in range(r):
        s += 'GBG'
print(s)
