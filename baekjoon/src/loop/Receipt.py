# https://www.acmicpc.net/problem/25304

x = int(input())
n = int(input())

for i in range(n):
    a, b = map(int, input().split())
    x -= a * b

if x == 0:
    print('Yes')
else:
    print('No')
