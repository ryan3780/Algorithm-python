import sys
from collections import deque

input = sys.stdin.readline
N = int(input())
check = [0]*(N+1)

def dfs(start):
    check[start] = 1
    for t in graph[start]:
        if not check[t]:
            print(check)
            dfs(t)


graph = [[] for _ in range(N+1)]

for _ in range(int(input())):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


# print(graph)
dfs(1)
print(check)
print(sum(check)-1)


# N = int(input())
# graph = [[] for _ in range(N+1)]
# check = [0]*(N+1)

# def bfs(start):
#     queue = deque()
#     queue.append(start)
#     check[start] = 1
#     while queue:
#         start = queue.popleft()
#         for i in graph[start]:
#             if not check[i]:
#                 queue.append(i)
#                 check[i] = 1


# for _ in range(int(input())):
#     a, b = map(int, input().split())
#     graph[a].append(b)
#     graph[b].append(a)

# bfs(1)
# print(sum(check)-1)