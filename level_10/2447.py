def paint_start(LEN):
    DIV3 = LEN//3
    if LEN == 3:
        g[1] = ['*', ' ', '*']
        g[0][:3] = g[2][:3] = ['*'] * 3
        return

    paint_start(DIV3)

    for i in range(0, LEN, DIV3):
        for j in range(0, LEN, DIV3):
            if i != DIV3 or j !=DIV3:
                for k in range(DIV3):
                    g[i+k][j:j+DIV3] = g[k][:DIV3]

n = int(input())
g = [[' ' for _ in range(n)] for _ in range(n)]

paint_start(n)

for i in range(n):
    for j in range(n):
        print(g[i][j], end='')
    print()