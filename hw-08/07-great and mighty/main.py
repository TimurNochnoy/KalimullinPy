s = input('Введите текст: ').split()
maxim = 0
for word in s:
    if len(word) > maxim:
        maxim = len(word)
print('Самое длинное слово, букв:', maxim)
