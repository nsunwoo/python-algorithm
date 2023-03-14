# https://www.acmicpc.net/problem/1316

n = int(input())
group_word_count = 0

for i in range(n):
    s = input()
    a = []
    group_word_checker = True
    for j in range(len(s)):
        if s[j] in a:
            if s[j] == a[-1]:
                continue
            else:
                group_word_checker = False
                break
        else:
            a.append(s[j])
    if group_word_checker:
        group_word_count += 1

print(group_word_count)
