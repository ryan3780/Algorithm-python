import sys
from itertools import permutations

input = sys.stdin.readline

N, M = map(int, input().rstrip().split())

result = []

# for i in permutations([N+1 for N in range(N)], M):
#     result.append(str(i))

# for i in result:
#     print(''.join(i).strip('()').replace(',',''))

def sol():
    if len(result) == M:
        print(*result)
        return
    for i in range(1, N+1):
        if i not in result:
            result.append(i)
            sol()
            result.pop()

sol()


