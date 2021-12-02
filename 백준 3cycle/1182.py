import sys
input = sys.stdin.readline
from itertools import combinations

n,s = map(int, input().split())
nums = list(map(int, input().split()))

count = 0

for i in range(1,n+1):
    combi = combinations(nums,i)
    for j in list(combi):
        if sum(j) == s:
            count += 1
            
print(count)