n = input()
lst = []

for i in range(1,int(n)+1):
    n_lst = list(map(int, str(i)))
    if int(n) == (sum(n_lst) + i):
        lst.append(i)

if len(lst) == 0:
    print(0)
else:
    print(lst[0])