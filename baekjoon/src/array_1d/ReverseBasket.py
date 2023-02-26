# https://www.acmicpc.net/problem/10811

n, m = map(int, input().split())
a = []

for x in range(n):
    a.append(x + 1)

for x in range(m):
    i, j = map(int, input().split())
    b = a[i - 1 : j]
    b.reverse()
    del a[i - 1 : j]
    a[i - 1 : i - 1] = b

convert_string = " ".join(str(i) for i in a)
print(convert_string)
