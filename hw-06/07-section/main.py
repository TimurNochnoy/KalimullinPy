a = int(input())
b = int(input())
summa = 0
k = 0

for i in range(a, b+1):
    if i % 3 == 0:
        summa += i
        k += 1

print(summa / k)