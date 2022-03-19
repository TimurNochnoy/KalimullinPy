import random

N = int(input())
lst = [random.randint(-5,5) for i in range(N)]
print(lst)
for elem in lst:
    if elem == 0:
        lst.remove(elem)
        lst.append(elem)
print(lst)
for elem in lst[::-1]:
    if elem == 0:
        lst.remove(elem)
print(lst)
