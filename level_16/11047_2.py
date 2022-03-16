n, k = map(int, input().split(' '))
money = 1
cash = []
cnt = 0

for _ in range(n):
    cash.append(int(input()))

if n == 1:
    print(k)
else:
    for i in range(n):
        while k >= cash[n-1-i]:
            k = k - cash[n-1-i]
            cnt += 1
    print(cnt)