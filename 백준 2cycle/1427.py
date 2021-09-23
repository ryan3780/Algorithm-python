import sys
from collections import Counter

input = sys.stdin.readline

n = input().rstrip()
ans = sorted(n, reverse=True)
print(''.join(ans))

