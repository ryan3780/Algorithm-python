import sys
from collections import deque

input = sys.stdin.readline
N, M, V = map(int, input().split())

graph = [[] for _ in range(N+1)]
check = [0] * (N+1)
dfs_list = []

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(start):
    check[start] = 1
    dfs_list.append(start)
    for i in sorted(graph[start]):
        if check[i] == 0:
            dfs(i)


dfs(V)

check =[0] * (N + 1)
bfs_list =[]

def bfs(start):
    queue = deque()
    queue.append(start)
    check[start] = 1

    while queue:
        start = queue.popleft()
        bfs_list.append(start)
        for i in sorted(graph[start]):
            if check[i] == 0:
                queue.append(i)
                check[i] = 1


bfs(V)
print(*dfs_list)
print(*bfs_list)