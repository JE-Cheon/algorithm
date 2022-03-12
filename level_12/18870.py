n = int(input())
x = list(map(int, input().split(' ')))
x_set = list(set(x))
x_set.sort()
lst = {}

for i, v in enumerate(x_set):
    lst[v] = i

for j in x:
    print(lst[j], end=' ')