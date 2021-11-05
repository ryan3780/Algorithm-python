import sys
input = sys.stdin.readline

n = int(input())
n = str(n)

ans = 0
for i in range(len(n) - 1):
    ans += 9 * (i + 1) * 10 ** i

ans += (int(n) - (10 ** (len(n) - 1)) + 1) * len(n)

print(ans)