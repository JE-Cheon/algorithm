n = int(input())
weight = []
height = []
rank = []

for i in range(n):
    x, y = map(int, input().split( ))
    weight.append(x)
    height.append(y)

for i in range(n):
    cnt = 1
    for j in range(n):
        if (weight[i] < weight[j]) and (height[i] < height[j]):
            cnt += 1
    rank.append(cnt)

for i in rank:
    print(i, end=' ')