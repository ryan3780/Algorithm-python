N = int(input())
graph = [input() for i in range(N)]
cnt = []
visited = [[0] * N for i in range(N)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
def dfs(x, y, number):
    visited[x][y] = number
    # 위쪽: (x - 1, y)
    # 아래: (x + 1, y)
    # 왼쪽: (x, y - 1)
    # 오른: (x, y + 1)
    for i in range(4):
        X = x + dx[i]
        Y = y + dy[i]
        if X < 0 or X >= N or Y < 0 or Y >= N:
            continue
        if not(visited[X][Y]) and graph[X][Y] == '1':
            dfs(X, Y, number)
for i in range(N):
    for j in range(N):
        if graph[i][j] == '1' and not(visited[i][j]):
            dfs(i, j, len(cnt) + 1)
            # len(cnt) = 0 -> 1을 채워넣고
            # 1의 갯수를 세서 cnt 배열에 넣습니다
            # 그럼 이제 len(cnt) + 1 = 2
            count = 0
            for i in range(N):
                count += visited[i].count(len(cnt) + 1)
            cnt.append(count)
print(len(cnt))
print(*sorted(cnt), sep='\n')