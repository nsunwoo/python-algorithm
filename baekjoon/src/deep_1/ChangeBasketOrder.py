# https://www.acmicpc.net/problem/10812

# 1 2 3 4 5 6 7 8 9 10
# 4 5 6 1 2 3 7 8 9 10
# 4 5 8 9 6 1 2 3 7 10
# 4 6 1 2 3 7 10 5 8 9
# 1 4 6 2 3 7 10 5 8 9
# 1 4 6 2 3 7 10 5 8 9

n, m = map(int, input().split())
a = list(range(1, n + 1))

for i in range(m):
    i, j, k = map(int, input().split())
    b = a[i - 1 : j]
    c = b[b.index(a[k - 1]) :] + b[: b.index(a[k - 1])]
    a = a[: i - 1] + c + a[j:]

convert_string = " ".join(str(i) for i in a)
print(convert_string)
