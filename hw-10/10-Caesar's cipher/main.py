alphabet = ['а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у',
            'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']
s = input('Введите сообщение: ')
k = int(input('Введите сдвиг: '))
index = 0
s = list(s)
for i in range(len(s)):
    f = 0
    for j in range(33):
        if s[i] == alphabet[j]:
            index = j
            f = 1
    if f == 1:
        s[i] = alphabet[(index + 3) % 33]
res = ''
for i in range(len(s)):
    res += str(s[i])
print('Зашифрованное сообщение:', res)
