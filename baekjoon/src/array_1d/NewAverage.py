# https://www.acmicpc.net/problem/1546

n = int(input())
old_scores = list(map(int, input().split()))

max_score = old_scores[0]
for i in range(n):
    if old_scores[i] > max_score:
        max_score = old_scores[i]

new_scores = list(map(lambda x: x / max_score * 100, old_scores))

print(sum(new_scores) / n)
