import random

lst_1 = [round(random.uniform(5, 10), 2)for i in range(20)]
lst_2 = [round(random.uniform(5, 10), 2)for i in range(20)]
print('Первая команда:', lst_1)
print('Вторая команда:', lst_2)
res = [max(lst_1[i], lst_2[i]) for i in range(20)]
print('Победители тура:', res)
