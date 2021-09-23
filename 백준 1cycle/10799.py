import sys
from collections import deque

input = sys.stdin.readline

stick = input().strip()

branch = []
cnt = 0

for i in stick:
    if i == '(':
        branch.append(i)
        last = i
        # print('111', cnt)
    else:
        if last == '(':
            branch.pop()
            cnt += len(branch)
            last = i
            # print('222',branch, cnt)
        else:
            branch.pop()
            cnt += 1
            # print('333',branch, cnt)

print(cnt)