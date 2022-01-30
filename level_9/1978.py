n = int(input())
arr = list(map(int, input().split( )))
cnt = 0

def is_prime_number(x):
    for i in range(2, x):
        if x % i == 0:
            return False
    return True

for i in arr:
    if i == 1:
        cnt += 0
    else:
        if is_prime_number(i) == True:
            cnt += 1
        else:
            cnt += 0

print(cnt)