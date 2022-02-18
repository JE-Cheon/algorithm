m = int(input())
n = int(input())
prime_sum = 0
prime = []

def is_prime_number(x):
    for i in range(2, x):
        if x % i == 0:
            return False
    return True

for i in range(m,n+1):
    if i == 1:
        continue
    else:
        if is_prime_number(i) == True:
            prime.append(i)
        else:
            continue

if len(prime) != 0:
    print(sum(prime))
    print(min(prime))
else:
    print(-1)