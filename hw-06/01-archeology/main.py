for i in range(0, 6):
    n = int(input())
    if (n % 2 == 0) and (n % 3 != 0):
        print('Число подходит')
    else:
        print('Число не подходит')