n = int(input())
lst = []

for _ in range(n):
    lst.append(int(input()))

mean = int(round(sum(lst)/n, 0))

lst.sort()
middle = lst[n//2]

set_lst = list(set(lst))
set_lst.sort()
cnt = []

for i in set_lst:
    cnt.append(lst.count(i))

# freq 값 미완
if cnt.count(max(cnt)) != 1:
    freq_lst = [set_lst[cnt.index(i)] for i in range(n) if cnt[i] == max(cnt)]


rng = lst[-1]-lst[0]
print(mean, middle, rng, sep="\n")
