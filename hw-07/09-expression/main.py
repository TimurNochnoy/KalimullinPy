x = float(input())
num = 1
denom = 1
for i in range(1, 7):
    num *= x - (2 ** i - 1)
    denom *= x - (2 ** i)
res = num / denom
print(res)
