H, M = map(int, input().split( ))

if H==0:
    if (M-45)<0:
        H = 23
        M = 60+M-45
    else:
        H = 0
        M = M-45
else:
    if (M-45)<0:
        H = H-1
        M = 60+M-45
    else:
        M = M-45

print(H,M)