a = int(input())
b = int(input())
c = int(input())
s = 0
k = 0
for i in range(a, b + 1):
    if i % c == 0 :
        s += i
        k += 1
print(s / k)
