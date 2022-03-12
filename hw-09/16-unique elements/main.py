print('Введите числа через пробел:')
lst_1 = input().split()
lst_1 = [int(elem) for elem in lst_1]
lst_2 = input().split()
lst_2 = [int(elem) for elem in lst_2]
print('Первый список:', lst_1)
print('Второй список:', lst_2)
result = lst_1 + lst_2
result = list(set(result))
print(result)
