dice = list(map(int, input().split( )))

if len(set(dice)) == 1:
    print(10000 + dice[0]*1000)
elif len(set(dice)) == 2:
    for i in set(dice):
        if dice.count(i) == 2:
            print(1000 + i*100)
else:
    print(max(dice)*100)