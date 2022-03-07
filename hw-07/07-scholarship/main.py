educational_grant = float(input('Введите стипендию: '))
expenses = float(input('Введите расходы на проживание: '))
s = expenses
for i in range(9):
    expenses *= 1.03
    s += expenses
print('У родителей необходимо попросить', round(s - 10 * educational_grant, 2))
