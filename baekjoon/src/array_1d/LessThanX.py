# https://www.acmicpc.net/problem/10871

n, x = map(int, input().split())
a = list(map(int, input().split()))
b = list()

for i in a:
    if i < x:
        b.append(i)

print(' '.join(map(str, b)))
