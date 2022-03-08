n = int(input())
member = []

for i in range(n):
    age, name = input().split(' ')
    age = int(age)
    member.append((age, i, name))
member.sort()

for i in member:
    print(i[0], i[2], sep=' ')
