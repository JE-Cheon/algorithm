n, k = map(int, input().split(' '))

if k == 0:
    print(1)
else:
    num = 1
    den = 1
    for i in range(k):
        num = num * (n-i)
        den = den * (i+1)
    print(int(num/den))
