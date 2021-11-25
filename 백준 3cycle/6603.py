import sys
input = sys.stdin.readline
from itertools import combinations

while True:
  lotto = list(map(int, input().split()))

  if lotto[0] == 0:
    break
  
  del lotto[0]
  lotto = list(combinations(lotto,6))

  for i in lotto:
    for j in i:
      print(j, end=' ')
    print()
  print()


