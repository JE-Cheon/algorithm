n = int(input())
cnt = 0

while True:
    if n % 5 == 0:
        print(cnt+n//5)
        break
    else:
        n -= 3
        cnt += 1

    if n == 0:
        print(cnt)
        break

    if n < 0:
        print(-1)
        break