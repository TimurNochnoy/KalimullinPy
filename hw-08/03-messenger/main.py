s = input('Введите текст: ')
for i in range(len(s)):
    if s[i] == '*':
        print('Символ ‘*’ стоит на позиции', i + 1)
