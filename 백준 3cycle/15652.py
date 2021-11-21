import sys
input = sys.stdin.readline

n, m = map(int, input().split())

ans = []

def sol(cnt):
  if len(ans) == m:
    print(*ans)
    return 
  
  for i in range(cnt, n+1):
    # if i not in ans:
      ans.append(i)
      sol(cnt)
      cnt += 1
      ans.pop()
    

sol(1)