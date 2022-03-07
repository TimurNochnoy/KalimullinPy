X = int(input('Введите количество мальчиков: '))
Y = int(input('Введите количество девочек: '))
s = ''
if (X > 2 * Y) or (Y > 2 * X):
    print('Нет решения')
elif X >= Y:
    k = X - Y
    for i in range(Y - k):
        s += 'BG'
    for i in range(k):
        s += 'BGB'
else:
    k = Y - X
    for i in range(X - k):
        s += 'GB'
    for i in range(k):
        s += 'GBG'
print(s)
