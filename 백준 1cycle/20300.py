import sys

input = sys.stdin.readline

N = int(input())
M = list(map(int, input().split()))
M = sorted(M)

if N % 2 != 0:
    M.pop()

ans = 0
for i in range(N//2):
    ans = max(ans,  M[i] + M[-1-i])

print(ans)