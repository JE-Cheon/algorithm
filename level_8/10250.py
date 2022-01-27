t = int(input())

for i in range(t):
    h, w, n = map(int, input().split( ))
    room_h = 1
    room_w = 1
    cnt = 0
    for j in range(1,w+1):
        for k in range(1,h+1):
            if k <= h:
                cnt += 1
            room_h += 1
        room_w += 1
    if cnt == n:
        print(room_h,room_w)