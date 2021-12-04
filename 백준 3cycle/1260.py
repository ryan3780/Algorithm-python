import sys
from collections import deque

input = sys.stdin.readline
N, M, V = map(int, input().split())

graph = [[] for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

check = [0]*(N+1)
dfs_list = []

def dfs(start):
    check[start] = 1
    dfs_list.append(start)
    for t in sorted(graph[start]):
        if not check[t]:
            dfs(t)


dfs(V)
bfs_list = []
check = [0]*(N+1)
def bfs(start):
    queue = deque()
    queue.append(start)
    
    check[start] = 1
    while queue:
        start = queue.popleft()
        bfs_list.append(start)
        for i in sorted(graph[start]):
            if not check[i]:
                queue.append(i)
                check[i] = 1

bfs(V)

print(*dfs_list)
print(*bfs_list)