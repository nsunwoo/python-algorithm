# https://www.acmicpc.net/problem/10809

s = input()
a = [-1 for i in range(26)]

for i in s:
    for j in range(97, 123):
        if chr(j) == i:
            a[j - 97] = s.index(i)

convert_string = " ".join(str(i) for i in a)
print(convert_string)
