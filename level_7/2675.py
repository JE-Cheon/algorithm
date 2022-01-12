t = int(input())

for i in range(t):
    a = list(input().split( ))
    for j in a[1]:
        print(j*int(a[0]), end="")
    print(sep="\n")
