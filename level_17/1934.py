t = int(input())

def gcd(a, b):
    mod = a % b
    while mod > 0:
        a = b
        b = mod
        mod = a % b
    return b

def lcm(a, b):
    return int(a * b / gcd(a, b))

for i in range(t):
    a, b = map(int, input().split(' '))
    print(lcm(a, b))