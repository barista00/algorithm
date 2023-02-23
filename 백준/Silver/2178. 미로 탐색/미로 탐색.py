from collections import deque
n, m = map(int, input().split())
graph = [list(map(int, input())) for _ in range(n)]

dx = [-1,1,0,0]
dy = [0,0,1,-1]

def bfs(i, j):
    queue = deque()
    queue.append((i, j))
    
    while queue:
        x, y = queue.popleft()

        for a in range(4):
            nx = dx[a] + x
            ny = dy[a] + y

            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue

            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))

for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            bfs(i, j)

print(graph[n-1][m-1])