N = int(input('Введите число учеников: '))
k3 = 0
k4 = 0

for i in range(N):
    a = int(input())
    if a == 3:
        k3 += 1
    elif a == 4:
        k4 += 1

print('3 -', k3)
print('4 -', k4)
print('5 -', N - k3 - k4)