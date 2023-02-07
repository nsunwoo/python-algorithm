# https://www.acmicpc.net/problem/2588

a = int(input())
b = int(input())

c1 = b // 100
c2 = b % 100
d1 = c2 // 10
d2 = c2 % 10

print(a*d2)
print(a*d1)
print(a*c1)
print(a*b)
