n = int(input())
x = list(map(int, input().split(' ')))
x_set = list(set(x))
x_set.sort()
lst = []

for i in x:
    lst.append(x_set.index(i))

print(*lst, sep=' ')