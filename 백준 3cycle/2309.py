import sys
input = sys.stdin.readline

from itertools import combinations


shorts = []

for i in range(9):
    shorts.append(int(input()))

shorts = sorted(shorts)
_shorts = list(combinations(shorts, 7))

ans = []
for i in _shorts:
    if sum(i) == 100:
        ans.append(i)
        break

for i in range(7):
    print(ans[0][i])