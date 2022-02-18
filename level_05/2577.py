a = int(input())
b = int(input())
c = int(input())

multi = a*b*c
arr = list(map(int,str(multi)))

for i in range(10):
    print(arr.count(i))