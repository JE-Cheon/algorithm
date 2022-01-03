t = int(input())

for i in range(t):
    A, B = map(int, input().split( ))
    print("Case #{}: {} + {} = {}".format(i+1, A, B, A+B))