rows = int(input('Введите кол-во рядов: '))
seat = int(input('Введите кол-во сидений в ряде: '))
meter = int(input('Введите кол-во метров между рядами: '))
print('\nСцена\n')
row = ''
for i in range(seat):
    row += '='
row += ' '
for i in range(meter):
    row += '*'
row += ' '
for i in range(seat):
    row += '='
for i in range(rows):
    print(row)
