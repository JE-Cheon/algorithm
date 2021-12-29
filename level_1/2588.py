A = int(input())
B = int(input())
a = B//100
b = (B-100*a)//10
c = B%10
print(A*c)
print(A*b)
print(A*a)
print(A*B)