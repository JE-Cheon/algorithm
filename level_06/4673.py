
def d(n):
    n_list = list(range(1,10001))
    for i in range(10001):
        a = str(i)
        if len(a) == 1:
            pre = int(a)+int(a)
        if len(a) == 2:
            pre = int(a)+int(a[0])+int(a[1])
        if len(a) == 3:
            pre = int(a)+int(a[0])+int(a[1])+int(a[2])
        if len(a) == 4:
            pre = int(a)+int(a[0])+int(a[1])+int(a[2])+int(a[3])
        if len(a) == 5:
            pre = int(a)+int(a[0])+int(a[1])+int(a[2])+int(a[3])+int(a[4])
        if pre in n_list:
            n_list.remove(pre)
    for j in n_list:
        print(j)

d(10000)