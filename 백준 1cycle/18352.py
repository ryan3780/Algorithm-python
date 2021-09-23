import sys
from collections import deque

input = sys.stdin.readline

n,m,k,x = map(int, input().split())
check = [0]*(n+1)
graph = [[] for _ in range(n+1)]

for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    # graph[b].append(a)

def bfs(start):
    queue = deque()
    queue.append(start)
    check[start] = 1
    
    while queue:
        start = queue.popleft()
        for i in graph[start]:
            if not check[i] :
                queue.append(i)
                check[i] = check[start] + 1


bfs(x)

print(graph)
print(check)
