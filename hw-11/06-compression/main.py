s = input('Введите строку: ')
res = ''
k = 0
f = 0
for i in range(1, len(s)):
    k += 1
    if s[i - 1] != s[i]:
        res += str(s[i - 1])
        res += str(k)
        k = 0
        f = i
res += str(s[f])
res += str(len(s) - f)
print('Закодированная строка:', res)
