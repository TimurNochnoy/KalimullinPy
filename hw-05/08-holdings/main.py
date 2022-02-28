X = int(input())
Y = int(input())
P = int(input())
k = 0

while X < Y:
    X += X * P // 100
    k += 1

print(k)