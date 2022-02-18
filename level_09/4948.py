cnt = []

while True:
    n = int(input())

    if n == 0:
        break

    a = [True] * (2*n+1)
    a[1] = False

    for i in range(2, int((2*n)**0.5+1)):
        if a[i] == True:
            for j in range(i+i, 2*n+1, i):
                a[j] = False
    b = a[n+1:]
    cnt.append(b.count(True))

for i in cnt:
    print(i)