# 다른 사람의 풀이
import sys
input = sys.stdin.readline
 
editor = ['L', 'D', 'B', 'P']

word = input().rstrip()
commands = []
cusor = len(word) + 1

for i in range(int(input())):
    commands.append(input().replace('\n',''))

for i in commands:
    if 'P' in i:
        if cusor >= len(word):
            word = word[:cusor] + i[2]
        else:
            word = word[:cusor] + i[2] + word[-1]
    elif i == 'L':
        if cusor < 1:
            pass
        else:
            cusor -= 1
    elif i == 'D':
        if cusor == len(word) + 1:
            pass
        else:
            cusor += 1
    else:
        if cusor < 1:
            pass
        else:
            cusor -= 1
            word = word[:cusor]

print(word)
