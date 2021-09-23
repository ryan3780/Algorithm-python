import sys

input = sys.stdin.readline

n = int(input())

for i in range(n):
    ans = ''
    case = input().split()
    cnt = int(case[0])
    code = case[1]

    for j in range(len(code)):
        ans += code[j] * cnt

    print(ans)