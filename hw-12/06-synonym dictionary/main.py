N = int(input('Введите количество пар слов: '))
vocabulary = dict()
for i in range(N):
    print(i + 1, 'пара: ', end='')
    s = input().lower().split(' - ')
    vocabulary[s[0]] = s[1]
    vocabulary[s[1]] = s[0]

s = input('Введите слово: ').lower()
while s != 'стоп':
    if s in vocabulary.keys():
        print('Синоним:', vocabulary[s])
    else:
        print('Такого слова в словаре нет.')
    s = input('Введите слово: ').lower()
