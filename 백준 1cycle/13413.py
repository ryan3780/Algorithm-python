import sys

input = sys.stdin.readline

T = int(input().rstrip())

result = []

for i in range(T):
    N = int(input().rstrip())
    F = input().rstrip()
    L = input().rstrip()
    white, black = 0, 0 
    for idx, spel in enumerate(F):
        if spel != L[idx]:
            if spel == 'W':
                white += 1
            else:
                black += 1
    result.append([white, black])

for i in result:
    print(max(i))

