# https://www.acmicpc.net/problem/8958

n = int(input())
score = 0
bonus = 0

for i in range(n):
    test_case = list(input())
    for j in range(len(test_case)):
        if test_case[j] == "O":
            score += bonus + 1
            bonus += 1
        else:
            bonus = 0
    print(score)
    score = 0
    bonus = 0
