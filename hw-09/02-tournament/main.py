lst_name = ['Артемий', 'Борис', 'Влад', 'Гоша', 'Дима', 'Евгений', 'Женя', 'Захар']
for i in range(0, len(lst_name), 2):
    print(lst_name[i])

'''
print([lst_name[i] for i in range(0, len(lst_name), 2)])

print([lst_name[i] for i, elem in enumerate(lst_name) if i % 2 == 0])

print([elem for i, elem in enumerate(lst_name) if i % 2 == 0])
'''
