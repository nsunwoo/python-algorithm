# https://www.acmicpc.net/problem/10818

n = int(input())
a = list(map(int, input().split()))
min_value = a[0]
max_value = a[0]

for i in a:
    if i > max_value:
        max_value = i
    if i < min_value:
        min_value = i

print(min_value, max_value)
