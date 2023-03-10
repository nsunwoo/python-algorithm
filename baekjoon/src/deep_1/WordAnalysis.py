# https://www.acmicpc.net/problem/1157

s = input().upper()
a = sorted(list(s))

# 중복 요소 카운팅
count = {}
for i in a:
    try:
        count[i] += 1
    except:
        count[i] = 1

keys_of_max_value = [k for k, v in count.items() if max(count.values()) == v]
if len(keys_of_max_value) == 1:
    print(keys_of_max_value[0])
else:
    print("?")
