s = input()
maxim = 0
k = 0
for letter in s:
    if letter == 's':
        k += 1
    elif k > maxim:
        maxim = k
        k = 0
print(maxim)
