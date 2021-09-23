import sys
from collections import Counter

input = sys.stdin.readline

n = int(input().rstrip())
ans = []

for i in range(n):
    x,y = map(int, input().split())
    ans.append((x,y))


ans = sorted(ans, key=lambda x:(x[1], x[0]))

for i in ans:
    print(i[0], i[1])