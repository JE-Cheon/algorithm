import sys

n = int(sys.stdin.readline())

for _ in range(n):
    a = sys.stdin.readline()
    right_cnt = 0
    left_cnt = 0
    for i in a:
        if i == "(":
            left_cnt += 1
        elif i == ")":
            right_cnt += 1
    if right_cnt == left_cnt:
        print("YES")
    else:
        print("NO")