while True:
    lst = list(map(int, input().split( )))
    c = max(lst)
    lst.remove(c)

    if sum(lst) == 0:
        break
    if lst[0]**2 + lst[1]**2 == c**2:
        print("right")
    else:
        print("wrong")