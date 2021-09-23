from itertools import combinations, permutations

N = int(input())
graph = [list(map(int, input().split())) for i in range(N)]
index = [i for i in range(N)]
answer = int(1e9)

for case in combinations(index, N // 2):
    # print(case)
    team_1 = []
    team_2 = []
    for i in range(N):
        if i in case:
            team_1.append(i)
        else:
            team_2.append(i)
    # print(team_1, team_2)
    point_1, point_2 = 0, 0
    
    for i in range(len(team_1)):
        for j in range(i + 1, len(team_1)):
            point_1 += graph[team_1[i]][team_1[j]] + graph[team_1[j]][team_1[i]]

    for i in range(len(team_2)):
        for j in range(i + 1, len(team_2)):
            point_2 += graph[team_2[i]][team_2[j]] + graph[team_2[j]][team_2[i]] 

    answer = min(answer, abs(point_1 - point_2))

print(answer)    


# from itertools import permutations
# from math import inf

# N = int(input())
# graph = [list(map(int, input().split())) for i in range(N)]
# index = [0] * (N // 2) + [1] * (N // 2)
# answer = int(1e9)
# # print(graph)

# for case in permutations(index, N):
#     print(case)
#     team_1 = []
#     team_2 = []
#     for idx, val in enumerate(case):
#         # print(idx, val)
#         if val == 0:
#             team_1.append(idx)
#         else:
#             team_2.append(idx)
    
#     point_1, point_2 = 0, 0

#     for i in range(len(team_1)):
#         for j in range(i + 1, len(team_1)):
#             point_1 += graph[team_1[i]][team_1[j]] + graph[team_1[j]][team_1[i]]

#     for i in range(len(team_2)):
#         for j in range(i + 1, len(team_2)):
#             point_2 += graph[team_2[i]][team_2[j]] + graph[team_2[j]][team_2[i]]
    
#     answer = min(answer, abs(point_1 - point_2))

# print(answer)

# import sys

# input = sys.stdin.readline

# N = int(input().rstrip())
# team = [0 for _ in range(N)]
# diff = sys.maxsize
# stat = [list(map(int, input().split())) for _ in range(N)]

# def sol(cnt, idx):
#     global diff
#     if idx == N:
#         return
#     if cnt == N // 2 :
#         s , l = 0, 0
#         for i in range(N):
#             for j in range(N):
#                 if team[i] == 0 and team[j] == 0 :
#                     s += stat[i][j]
#                 if not team[i] == 0 and not team[j] == 0:
#                     l += stat[i][j]
#         diff = min(diff, abs(s -l))
#         return

#     team[idx] = 0
#     sol(cnt+1, idx+1)
#     team[idx] = 1
#     sol(cnt, idx+1)


# sol(0,0)
# print(diff)
            


