import sys
from collections import Counter

input = sys.stdin.readline

n = int(input().rstrip())

for i in range(n):
    word = input().split()
    ans = ''
    for j in word:
        ans += j[::-1] + ' '
    print(ans)