import sys
input = sys.stdin.readline

n, m = map(int, input().split())

ans = []

def sol(cnt):
  if len(ans) == m:
    print(*ans)
    return
  
  c = cnt
  for i in range(c, n+1):
    if i not in ans:
      c += 1
      ans.append(i)
      sol(c)
      ans.pop()

sol(1)