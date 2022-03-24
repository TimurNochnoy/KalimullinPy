s = input('Введите текст: ')
original = dict()
for symbol in s:
    if symbol in original:
        original[symbol] += 1
    else:
        original[symbol] = 1
print('Оригинальный словарь частот:')
for key in sorted(original):
    print(key, ':', original[key])
invert = dict()
for symbol in original:
    if original[symbol] in invert:
        invert[original[symbol]].append(symbol)
    else:
        invert[original[symbol]] = [symbol]
print('Инвертированный словарь частот:')
for key in sorted(invert):
    print(key, ':', invert[key])
