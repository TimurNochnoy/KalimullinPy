p = int(input('Введите цену квартиры в млн: '))
s = int(input('Введите площадь квартиры: '))
if s >= 100 and p <= 10:
    print('OK')
elif s >= 80 and p <= 7:
    print('OK')
else:
    print('NOT OK')