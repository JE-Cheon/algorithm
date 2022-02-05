x_lst = []
y_lst = []
for i in range(3):
    x, y = map(int, input().split( ))
    x_lst.append(x)
    y_lst.append(y)

x_num = list(set(x_lst))
y_num = list(set(y_lst))

for i in x_num:
    for j in y_num:
        if y_lst.count(j) != 2:
            new_y = j
    if x_lst.count(i) != 2:
        new_x = i

print(new_x, new_y, sep=' ')