import sys
from collections import Counter

input = sys.stdin.readline

n = int(input().rstrip())

ans = []

for i in range(n):
    age, name = input().split()
    ans.append((int(age), name, int(i)))

ans = sorted(ans, key= lambda x:(x[0], x[2]))

for i in ans:
    print(i[0], i[1])