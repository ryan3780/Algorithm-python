import sys
input = sys.stdin.readline
from itertools import combinations

l, c = map(int,input().split())

spelling = input().split()
spelling = sorted(spelling)

print(list(combinations(spelling,l)))



