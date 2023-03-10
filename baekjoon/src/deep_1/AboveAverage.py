# https://www.acmicpc.net/problem/4344

c = int(input())

for i in range(c):
    a = list(map(int, input().split()))
    average = sum(a[1:]) / a[0]
    count = 0
    for j in range(a[0]):
        if a[j + 1] > average:
            count += 1
    above_average_rate = count / a[0] * 100
    print(format(above_average_rate, ".3f") + "%")
