def solve(a):
    ans = 0
    for i in a:
        ans += i
    return ans

A = list(map(int, input().split( )))
print(solve(A))