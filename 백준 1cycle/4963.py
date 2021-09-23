import sys

input = sys.stdin.readline

dx = (-1, -1, -1, 0, 1, 1, 1, 0)
dy = (-1, 0, 1, 1, 1, 0, -1, -1)


def dfs(x,y):
    check[x][y] = 1
    # print(check)
    for i in range(8):
        nx, ny = x + dx[i], y + dy[i]
        if nx < 0 or nx >= h or ny < 0 or ny >= w:
            continue
        if island[nx][ny] == 1 and check[nx][ny] == 0:
            dfs(nx, ny)          


while True:
    w, h = map(int, input().split())

    if w == 0 and h == 0:
        break
    
    island = []
    check = [[0] * w for _ in range(h)]

    for _ in range(h):
        island.append(list(map(int, input().split())))

    cnt = 0
    for i in range(h):
        for j in range(w):
            if island[i][j] == 1 and check[i][j] == 0:
                dfs(i, j)
                cnt += 1
    print(cnt)
   

    
