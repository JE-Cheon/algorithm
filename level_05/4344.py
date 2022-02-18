n = int(input())
a = []
for i in range(n):
    a.append(list(map(int, input().split( ))))

for i in a:
    num = i[0]
    del i[0]
    avg = sum(i)/num
    cnt = 0
    for j in i:
        if j > avg:
            cnt += 1
    per = cnt/len(i)*100
    print(f"{per:.3f}%")