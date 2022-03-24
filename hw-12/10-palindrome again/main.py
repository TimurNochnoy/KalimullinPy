s = input('Введите строку: ')
vocabulary = dict()
for i in range(len(s)):
    if s[i] in vocabulary:
        vocabulary[s[i]] += 1
    else:
        vocabulary[s[i]] = 1
summa = 0
for key in vocabulary:
    vocabulary[key] = vocabulary[key] % 2
    summa += vocabulary[key]
if summa == 0 or summa == 1:
    print('Можно сделать палиндромом')
else:
    print('Нельзя сделать палиндромом')
