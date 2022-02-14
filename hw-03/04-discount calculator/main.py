a = int(input('Введите стоимость товара: '))
b = int(input('Введите стоимость товара: '))
c = int(input('Введите стоимость товара: '))
if a + b + c > 10000:
    print((a + b + c) * 0.1)
else:
    print(a + b + c)