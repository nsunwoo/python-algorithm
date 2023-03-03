# https://www.acmicpc.net/problem/2675

t = int(input())

for i in range(t):
    r, s = input().split()
    r = int(r)
    p = ""
    for j in s:
        p += j * r
    print(p)
