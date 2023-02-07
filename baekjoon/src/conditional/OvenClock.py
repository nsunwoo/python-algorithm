# https://www.acmicpc.net/problem/2525

hour, minute = map(int, input().split())
cook_minute = int(input())

if (minute + cook_minute) < 60:
    minute += cook_minute
else:
    temp = minute + cook_minute
    hour += temp // 60
    minute = temp % 60
    if hour >= 24:
        hour -= 24

print(hour, minute)
