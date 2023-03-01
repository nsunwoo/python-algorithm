# https://www.acmicpc.net/problem/11720

n = int(input())
m = input()

a = list(m)
a_int = list(map(int, a))
total = 0

for i in range(n):
    total += a_int[i]
print(total)
