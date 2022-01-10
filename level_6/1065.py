def han(n):
    cnt = 0
    for i in range(1, n+1):
        if len(str(i)) == 1:
            cnt += 1
        if len(str(i)) == 2:
            cnt += 1
        if len(str(i)) == 3:
            a = str(i)
            if (int(a[0])-int(a[1])) == (int(a[1])-int(a[2])):
                cnt += 1
            else:
                cnt += 0
        if len(str(i)) == 4:
            a = str(i)
            if ((int(a[0])-int(a[1])) == (int(a[1])-int(a[2]))) and ((int(a[1])-int(a[2])) == (int(a[2])-int(a[3]))):
                cnt += 1
            else:
                cnt += 0

    return cnt

N = int(input())
print(han(N))