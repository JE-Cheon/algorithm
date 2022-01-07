a = []
b = []

for i in range(10):
    a.append(int(input()))
    b.append(a[i]%42)

set_b = set(b)
print(len(set_b))