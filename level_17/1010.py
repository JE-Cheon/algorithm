t = int(input())

for _ in range(t):
    a, b = map(int, input().split(' '))
    num = 1
    den = 1
    for i in range(a):
        num = num * (b - i)
        den = den * (i + 1)
    print(int(num / den))