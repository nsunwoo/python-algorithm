# https://www.acmicpc.net/problem/1110

n = int(input())
i = 0
new_n = n

while True:
    tens = new_n // 10
    units = new_n % 10
    plus = tens + units
    plus_units = plus % 10
    new_n = units * 10 + plus_units
    i += 1
    if n == new_n:
        break

print(i)
