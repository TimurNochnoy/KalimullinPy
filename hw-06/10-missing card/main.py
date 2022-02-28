N = int(input('Введите число карточек - '))
past = 0
f = 0

for i in range(1, N):
    m = int(input())
    if m != past + 1:
        f = m
    past = m

if f != 0:
    print('Нет карточки с номером -', f)
else:
    print('Все картоки на месте')