import sys
input = sys.stdin.readline

n, m = map(int, input().split())

ans = []

def sol():
  if len(ans) == m:
    print(*ans)
    return
  
  for i in range(1, n+1):
    # if i not in ans:
      ans.append(i)
      sol()
      ans.pop()

sol()