t = int(input())

for _ in range(t):
    n = int(input())
    a = [True] * (n + 1)
    a[1] = False
    lst = list(range(n + 1))

    for i in range(2, int((n + 1) ** 0.5) + 1):
        if a[i] == True:
            for j in range(i + i, n + 1, i):
                a[j] = False
    prime = [lst[i] for i in range(1,len(lst)) if a[i] == True]
    low = n//2
    while True:
        if low in prime and n-low in prime:
            print(low, n-low, sep=' ')
            break
        else:
            low -= 1