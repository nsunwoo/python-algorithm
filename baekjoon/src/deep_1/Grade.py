# https://www.acmicpc.net/problem/25206

grade = {
    "A+": 4.5,
    "A0": 4.0,
    "B+": 3.5,
    "B0": 3.0,
    "C+": 2.5,
    "C0": 2.0,
    "D+": 1.5,
    "D0": 1.0,
    "F": 0.0,
}
grade_sum = 0
credit_sum = 0

for i in range(20):
    a, b, c = input().split()
    if c == "P":
        continue
    b = float(b)
    grade_sum += b * grade[c]
    credit_sum += b

grade_total = grade_sum / credit_sum
print(grade_total)
