# https://www.acmicpc.net/problem/5597

a = list(range(1, 31))

for i in range(28):
    num = int(input())
    a.remove(num)

for num in a:
    print(num)
