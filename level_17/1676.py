n = int(input())
cnt = 0

def fac(i):
    if i == 0:
        return 1
    else:
        return i*fac(i-1)

result = fac(n)
while (result % 10) == 0:
    result = result//10
    cnt += 1
print(cnt)