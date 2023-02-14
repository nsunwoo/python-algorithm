# https://www.acmicpc.net/problem/2562

a = list()
for i in range(9):
    num = int(input())
    a.append(num)

max_value = a[0]
order = a.index(a[0]) + 1
for num in a:
    if num > max_value:
        max_value = num
        order = a.index(num) + 1
print(max_value, order, sep='\n')
