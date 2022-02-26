a, b, c = int(input()), int(input()), int(input())
if a == b and a == c:
    print(3)
elif (a == b and a != c) or (a == c and b != c) or (b == c and a != c):
    print(2)
else:
    print(0)