l = int(input('Введите общую длину колонтитула: '))
z = int(input('Введите количество восклицательных знаков: '))
s = ''
for i in range((l - z) // 2):
    s += '~'
for i in range(z):
    s += '!'
for i in range(l - z - (l - z) // 2):
    s += '~'
print(s)
