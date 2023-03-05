# https://www.acmicpc.net/problem/2908

a, b = input().split()
new_a = int(a[::-1])
new_b = int(b[::-1])
if new_a > new_b:
    print(new_a)
elif new_a < new_b:
    print(new_b)
