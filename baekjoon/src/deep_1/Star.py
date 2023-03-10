# https://www.acmicpc.net/problem/2444

n = int(input())
number_of_star = 1

for i in range(n - 1, 0, -1):
    print(" " * i + "*" * number_of_star)
    number_of_star += 2

print("*" * number_of_star)
number_of_star -= 2

for i in range(1, n):
    print(" " * i + "*" * number_of_star)
    number_of_star -= 2
