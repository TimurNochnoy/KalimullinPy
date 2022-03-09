s = input()
m = 0
for i in range(len(s)):
    if s[i] == 'b':
        m += (i + 1) * 2
print(m)
