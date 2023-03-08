# https://www.acmicpc.net/problem/2738

n, m = map(int, input().split())

a = [[0 for col in range(m)] for row in range(n)]

for i in range(n):
    a[i] = list(map(int, input().split()))

b = [[0 for col in range(m)] for row in range(n)]

for i in range(n):
    b[i] = list(map(int, input().split()))

c = [[a[i][j] + b[i][j] for j in range(m)] for i in range(n)]

for i in range(n):
    for j in range(m):
        if j == m - 1:
            print(c[i][j])
            break
        print(c[i][j], end=" ")
