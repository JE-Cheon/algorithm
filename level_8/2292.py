n = int(input())

i = 1
cnt = 1
a = 1+6*(i-1)

while True:
    if a < n:
        a = a+6*i
        i += 1
        cnt += 1
    else:
        print(cnt)
        break