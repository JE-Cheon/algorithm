n, m = map(int, input().split(' '))
m = min(n-m, m)
comb = 0
cnt = 0

if m == 0:
    comb = 1
else:
    num = 1
    den = 1
    for i in range(m):
        num = num * (n-i)
        den = den * (i+1)
    comb = num//den

while (comb % 10) == 0:
    comb = comb//10
    cnt += 1
print(cnt)