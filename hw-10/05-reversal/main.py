s = input()
finish = 0
for i in range(len(s)):
    if s[i] == 'h':
        finish = i
start = 0
for i in range(len(s)-1, -1, -1):
    if s[i] == 'h':
        start = i
print(s[finish-1:start:-1])
