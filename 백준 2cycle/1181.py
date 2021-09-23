import sys
from collections import Counter

input = sys.stdin.readline

n = int(input().rstrip())

ans = []

for i in range(n):
    word = input().rstrip()
    ans.append((word, len(word)))

ans = set(ans)
ans = sorted(ans, key=lambda x:(x[1], x[0]))

for i in ans:
    print(i[0])