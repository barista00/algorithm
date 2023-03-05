n, m = map(int, input().split())

ground = [list(input()) for _ in range(n)]
visited = [[False] * m for _ in range(n)]

dx = [1,-1,0,0]
dy = [0,0,-1,1]

def dfs(i, j):
    sheep = 0
    wolf = 0

    stack = []
    stack.append((i, j))
    visited[i][j] = True

    while stack:
        x, y = stack.pop()

        if ground[x][y] == 'v':
            wolf += 1
        elif ground[x][y] == 'o':
            sheep += 1

        for a in range(4):
            nx = x + dx[a]
            ny = y + dy[a]

            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue

            if ground[nx][ny] != '#' and visited[nx][ny] == False:
                stack.append((nx, ny))
                visited[nx][ny] = True

            # if ground[nx][ny] == 'v' and visited[nx][ny] == False:
            #     visited[nx][ny] = True
            #     stack.append((nx, ny))
            # if ground[nx][ny] == 'o' and visited[nx][ny] == False:
            #     visited[nx][ny] = True
            #     stack.append((nx, ny))
            # if ground[nx][ny] == '.' and visited[nx][ny] == False:
            #     visited[nx][ny] = True
            #     stack.append((nx, ny))
    
    if wolf >= sheep:
        wolf_lst.append(wolf)
    else:
        sheep_lst.append(sheep)

wolf_lst = []
sheep_lst = []
for i in range(n):
    for j in range(m):
        if ground[i][j] != '#' and visited[i][j] == False:
            dfs(i, j)
print(sum(sheep_lst), sum(wolf_lst))
# print(visited)
# print(wolf_lst, sheep_lst)