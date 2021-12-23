import sys
from collections import deque
from types import coroutine
input = sys.stdin.readline

n, m = map(int, input().split())

graph = []
check = [[0] * m for _ in range(n)]

for _ in range(m):
  graph.append(list(map(int, input().split())))

dx = [-1, 1, 0, 0] 
dy = [0, 0, -1, 1]

def bfs(x,y):
    queue = deque()
    queue.append((x,y))
    check[x][y] = 1

    while queue:                    # O(N)
        x,y = queue.popleft()

        if x == n - 1 and y == m -1:
            print(graph[n - 1][m - 1])
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] == 1:
                    graph[nx][ny] = graph[x][y] + 1
                    queue.append((nx, ny)) 


bfs(0,0)
        