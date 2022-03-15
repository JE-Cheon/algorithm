n, k = map(int, input().split(' '))
money = 1
cash = []
cnt = 0

for i in range(1, n+1):
    if i == 1:
        cash.append(money)
    elif i % 2 == 0:
        money = money * 5
        cash.append(money)
    else:
        money = money * 2
        cash.append(money)

for i in range(n):
    if k == 0:
        print(cnt)
    else:
        while k > 0:
            if k - cash[n-i-1] <0:
                pass
            else:
                k = k - cash[n-i-1]
                cnt += 1