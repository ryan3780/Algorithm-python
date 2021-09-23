import sys
from collections import deque
input = sys.stdin.readline

n = int(input().rstrip())

graph = [[] for _ in range(n+1)]
check = [0] * (n+1)

def bfs(start):
    queue = deque()
    queue.append(start)
    check[start] = 1
    print('queue', queue)
    while queue:
        start = queue.popleft()
        for i in graph[start]:
            if not check[i]:
                queue.append(i)
                print('for queue', queue)
                check[i] = start
                print('for check',check)


for i in range(n-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


bfs(1)

