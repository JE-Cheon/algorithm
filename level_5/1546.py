n = int(input())
score = list(map(int, input().split( )))
new_score = []

for i in score:
    new_score.append((i/max(score))*100)

print(sum(new_score)/n)