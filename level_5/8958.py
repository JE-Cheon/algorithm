n = int(input())
a = []

for i in range(n):
    a.append(input())

for i in a:
    score = 0
    sum_score = 0
    for j in i:
        if j == "O":
            score += 1
        else:
            score = 0
        sum_score += score
    print(sum_score)
