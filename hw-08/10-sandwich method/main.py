s = input('Введите зашифрованное сообщение: ')
a = ''
if len(s) % 2 == 0:
    for i in range(1, len(s) + 1, 2):
        a += s[i - 1]
    for i in range(len(s), 0, -2):
        a += s[i - 1]
if len(s) % 2 == 1:
    for i in range(1, len(s) + 1, 2):
        a += s[i - 1]
    for i in range(len(s) - 1, 0, -2):
        a += s[i - 1]
print('Расшифрованное сообщение:', a)
