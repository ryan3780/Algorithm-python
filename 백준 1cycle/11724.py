from collections import deque
import sys

input = sys.stdin.readline

N, M = map(int, input().split())

graph = [[] for _ in range(N+1)]
check = [0] * (N+1)

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def bfs(start):
    queue = deque()
    queue.append(start)
    check[start] = 1

    while queue:
        start = queue.popleft()
        for i in graph[start]:
            if not check[i]:
                queue.append(i)
                check[i] = 1

    print(check)

cnt = 0

for i in range(1, N+1):
    print(check)
    if check[i] == 0:
        print('123123', check[i], i)
        bfs(1)
        cnt += 1

print(cnt)

# def dfs(start):
#     check[start] = 1
#     for i in graph[start]:
#         if not check[i]:
#             # print(check)
#             dfs(i)


# dfs(1)