# https://www.acmicpc.net/problem/2941

length_two = ["c=", "c-", "d-", "lj", "nj", "s=", "z="]
length_three = ["dz="]

count = 0

s = input()
for i in range(len(s)):
    if s[i : i + 2] in length_two:
        if s[i - 1 : i + 2] in length_three:
            continue
        count += 1
    elif s[i : i + 3] in length_three:
        count += 1
    else:
        if (
            s[i - 1 : i + 1] in length_two
            or s[i - 1 : i + 2] in length_three
            or s[i - 2 : i + 1] in length_three
        ):
            continue
        count += 1

print(count)
