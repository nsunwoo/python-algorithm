# https://www.acmicpc.net/problem/3052

a = []
r = []

for i in range(10):
    n = int(input())
    a.append(n)

for n in a:
    n %= 42
    r.append(n)

print(len(set(r)))
