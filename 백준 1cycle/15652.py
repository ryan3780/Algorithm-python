import sys

input = sys.stdin.readline

N, M = map(int, input().rstrip().split())

result = []

def sol(start):

    if len(result) == M:
        print(*result)
        return 
    for i in range(start, N+1):
        result.append(i)
        sol(i)
        result.pop()

            
sol(1)