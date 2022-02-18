word = input()
alpha = []

for i in range(97,123):
    alpha.append(chr(i))

for i in alpha:
    if i in word:
        print(word.find(i), end=" ")
    else:
        print(-1, end=" ")