s = input('Введите текст: ')
vowels = ['а','у','о','ы','э','я','ю','ё','и','е']
res = []
for letter in s:
    for vowel in vowels:
        if letter == vowel:
            res.append(letter)
print('Список гласных букв:', res)
print('Длина списка:', len(res))
