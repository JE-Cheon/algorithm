word = list(input())

two = ["A","B","C"]
three = ["D","E","F"]
four = ["G","H","I"]
five = ["J","K","L"]
six = ["M","N","O"]
seven = ["P","Q","R","S"]
eight = ["T","U","V"]
nine = ["W","X","Y","Z"]

sec = 0

for i in word:
    if i in two:
        sec += 3
    if i in three:
        sec += 4
    if i in four:
        sec += 5
    if i in five:
        sec += 6
    if i in six:
        sec += 7
    if i in seven:
        sec += 8
    if i in eight:
        sec += 9
    if i in nine:
        sec += 10

print(sec)