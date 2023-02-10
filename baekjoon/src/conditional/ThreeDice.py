# https://www.acmicpc.net/problem/2480

dice1, dice2, dice3 = map(int, input().split())

if dice1 == dice2 == dice3:
    print(10000 + dice1 * 1000)
elif dice1 == dice2 != dice3 or dice1 == dice3 != dice2:
    print(1000 + dice1 * 100)
elif dice2 == dice3 != dice1:
    print(1000 + dice2 * 100)
else:
    if dice1 > dice2 and dice1 > dice3:
        print(dice1 * 100)
    elif dice2 > dice1 and dice2 > dice3:
        print(dice2 * 100)
    else:
        print(dice3 * 100)
