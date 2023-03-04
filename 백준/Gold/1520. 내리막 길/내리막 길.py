import sys
n, m = map(int, sys.stdin.readline().split())

graph = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
visited = [[-1] * m for _ in range(n)]
dx = [1,-1,0,0]
dy = [0,0,1,-1]

def dfs(x, y):
    if x == n-1 and y == m-1:
        return 1

    if visited[x][y] != -1:
        return visited[x][y]
    
    visited[x][y] += 1
    for i in range(4):

        nx = dx[i] + x
        ny = dy[i] + y
        
        if nx < 0 or nx >= n or ny < 0 or ny >= m:
            continue
        
        if graph[x][y] > graph[nx][ny]:
            visited[x][y] = visited[x][y] + dfs(nx, ny)
    return visited[x][y]
print(dfs(0, 0))