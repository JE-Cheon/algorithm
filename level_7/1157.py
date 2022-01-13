word = input()
WORD = word.upper()
alpha = list(set(list(WORD)))
cnt = {}

for i in range(len(alpha)):
    cnt[alpha[i]] = WORD.count(alpha[i])

Max = max(cnt.values())
Max_key = max(cnt, key=cnt.get)
cnt.pop(Max_key)

if Max in cnt.values():
    print("?")
else:
    print(Max_key)


