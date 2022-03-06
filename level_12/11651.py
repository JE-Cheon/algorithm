n = int(input())
point = []

for i in range(n):
    x, y = map(int, input().split( ))
    point.append((y, x))

point.sort()

for i in point:
    print(i[1], i[0], sep=' ')
