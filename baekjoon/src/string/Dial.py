# https://www.acmicpc.net/problem/5622

s = input()
d = {2: "ABC", 3: "DEF", 4: "GHI", 5: "JKL", 6: "MNO", 7: "PQRS", 8: "TUV", 9: "WXYZ"}
sec = 0

for i in range(len(s)):
    for j in range(2, 10):
        if s[i] in d[j]:
            sec += 1 + j

print(sec)
