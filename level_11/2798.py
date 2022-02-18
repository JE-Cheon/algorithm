n, m = map(int, input().split( ))
lst = list(map(int, input().split( )))
plus_list = []
a = 0

for i in range(n):
    for j in range(i+1,n):
        for k in range(j+1,n):
            a = lst[i]+lst[j]+lst[k]
            if a <= m:
                plus_list.append(a)
            a = 0

print(max(plus_list))