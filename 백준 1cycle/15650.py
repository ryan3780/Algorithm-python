import sys
from itertools import combinations

input = sys.stdin.readline

N, M = map(int, input().rstrip().split())

result = []

# for i in combinations([N+1 for N in range(N)], M):
#     result.append(str(i))

# for i in result:
#     print(''.join(i).strip('()').replace(',',''))

def sol(start):
    if len(result) == M:
        print(*result)
        return
    for i in range(start, N+1):
        if i not in result:
            result.append(i)
            sol(i+1)
            result.pop()


sol(1)