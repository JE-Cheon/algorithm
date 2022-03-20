from fractions import Fraction

n = int(input())

lst = list(map(int, input().split(' ')))

for i in range(1,n):
    roll =  Fraction(lst[0], lst[i])
    if roll.denominator == 1:
        print(roll, "/1", sep="")
    else:
        print(Fraction(lst[0], lst[i]))