t = int(input())

for _ in range(t):
    x_1, y_1, r_1, x_2, y_2, r_2 = map(int, input().split( ))
    dist = ((x_1-x_2)**2 + (y_1-y_2)**2)**(1/2)
    plus = r_1+r_2
    minus = abs(r_1-r_2)
    if (plus < dist) | (minus > dist) | ((x_1 == x_2) and (y_1 == y_2) and (r_1 != r_2)):
        print(0)
    elif ((plus == dist) | (minus == dist)) and (dist != 0):
        print(1)
    elif (minus < dist) and (plus > dist):
        print(2)
    else:
        print(-1)