import sys
input = sys.stdin.readline

n, m = map(int, input().split())

ans = []
def sol():
  if len(ans) == m:
    print(*ans)
    return

  for i in range(1, n + 1):
    if i not in ans:          # ans의 길이 만큼 최악은 길이가 O(n * m)
        ans.append(i)
        sol()
        ans.pop()

sol()