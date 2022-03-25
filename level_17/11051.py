n, k = map(int, input().split(' '))

def factorial(n):
    lst = list(range(1,n+1))
    return lst

k = factorial(k) + factorial(n-k)
n = factorial(n)

while True:
    for i in n:
        if i in k:
            n.remove(i)
            k.remove(i)
            break
    else:
        break

result = 1
for i in n:
    result *= i
for i in k:
    result //= i

print(result%10007)