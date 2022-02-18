m, n = map(int, input().split( ))
a = [True] * (n+1)
a[1] = False
lst = list(range(m,n+1))

for i in range(2, int(n**0.5)+1):
    if a[i] == True:
        for j in range(i+i,n+1,i):
            a[j] = False

b = a[m:]

prime = [lst[i] for i in range(len(lst)) if b[i] == True]

for i in prime:
    print(i)