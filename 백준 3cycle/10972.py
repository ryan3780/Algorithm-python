import sys
input = sys.stdin.readline
import itertools

n = int(input())
m = list(map(int, input().split()))

s = []
for i in range(1,n+1):
  s.append(i)

npr = itertools.permutations(s, n)
npr_len = len(list(npr))

npr = itertools.permutations(s, n)
npr_index = list(npr).index(tuple(m)) + 1

if npr_len == npr_index:
  print(-1)

npr = itertools.permutations(s, n)
npr_index = list(npr).index(tuple(m))

npr = itertools.permutations(s, n)
print(*list(list(npr)[npr_index+1]))  

