t = int(input())

for _ in range(t):
    k = int(input())
    n = int(input())
    n_people = 0
    cnt = list(range(1,n+1))

    if k == 0:
        n_people = n

    if k == 1:
        n_people = sum(cnt)

    else:
        for b in range(1,k):
            new_cnt = []
            for j in range(1,n+1):
                c = 0
                for a in range(j):
                    c += cnt[a]
                new_cnt.append(c)
            cnt = new_cnt
        n_people = sum(cnt)
    print(n_people)