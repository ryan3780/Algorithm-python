import sys

input = sys.stdin.readline

key = list(map(int, input().split()))
N, A, D = key[0], key[1], key[2]
pitch = list(map(int, input().split()))

ans = 0

for i in range(len(pitch)):
    if pitch[i] == A + (ans * D):
        ans += 1

print(ans)