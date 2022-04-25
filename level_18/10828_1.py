import sys
n = int(sys.stdin.readline())
stack = []

for _ in range(n):
    order = input()
    val = "push" in order
    if val:
        a = int(order[5:])
        stack.append(a)
    elif order == "pop":
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])
            stack = stack[:-1]
    elif order == "size":
        print(len(stack))
    elif order == "empty":
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    elif order == "top":
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])