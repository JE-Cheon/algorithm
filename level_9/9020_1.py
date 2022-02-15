t = int(input())

for _ in range(t):
    n = int(input())
    a = [True] * (n + 1)
    a[1] = False
    lst = list(range(n + 1))

    for i in range(2, int(n ** 0.5) + 1):
        if a[i] == True:
            for j in range(i + i, n + 1, i):
                a[j] = False
    prime = [lst[i] for i in range(1,len(lst)) if a[i] == True]
    part = []
    for k in prime:
        if (n-k) in prime:
            part.append((k,n-k))
    if len(part) % 2 == 0:
        Id = len(part)//2 - 1
    else:
        Id = len(part)//2
    print(part[Id][0],part[Id][1],sep = ' ')
