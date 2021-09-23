import sys

input = sys.stdin.readline

N, L = map(int,input().split())
h = list(map(int, input().split()))
h = sorted(h)

for i in range(len(h)):
    if L >= h[i]:
        L += 1

# 길이가 작거나 같은 높이에 있는 과일만 먹을 수 있다
# print(N, L)
print(L)
