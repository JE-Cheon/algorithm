n = int(input())

def move(N, start, to):
    print(start, to, sep = ' ')

def hanoi(N, start, to, via):
    if N == 1:
        move(1, start, to)
    else:
        hanoi(N-1, start, via, to)
        move(N, start, to)
        hanoi(N-1, via, to, start)

print(2**n - 1)
hanoi(n, 1, 3, 2)