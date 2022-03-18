a, b = map(int, input().split(' '))

def gcd(a, b):
    mod = a % b
    while mod > 0:
        a = b
        b = mod
        mod = a % b
    return b

def lcm(a, b):
    return int(a * b / gcd(a, b))

print(gcd(a, b), lcm (a, b), sep="\n")