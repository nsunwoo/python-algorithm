# https://www.acmicpc.net/problem/10813

n, m = map(int, input().split())
a = []

for x in range(n):
    a.append(x + 1)

for y in range(m):
    i, j = map(int, input().split())
    temp = a[i - 1]
    a[i - 1] = a[j - 1]
    a[j - 1] = temp

convert_string = " ".join(str(i) for i in a)
print(convert_string)
