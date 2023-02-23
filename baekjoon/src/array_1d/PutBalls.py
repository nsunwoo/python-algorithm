# https://www.acmicpc.net/problem/10810

n, m = map(int, input().split())
a = []
for i in range(n):
    a.append(0)

for b in range(m):
    i, j, k = map(int, input().split())
    for c in range(i - 1, j):
        a[c] = k

convert_string = " ".join(str(i) for i in a)
print(convert_string)
