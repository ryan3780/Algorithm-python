import sys

input = sys.stdin.readline

n = int(input())

for _ in range(n):
    case = input().rstrip()
    score = 0
    tmp = 0
    for i in case:
        if i == 'O':
            tmp += 1
            score += tmp
        else:
            tmp = 0

    print(score)