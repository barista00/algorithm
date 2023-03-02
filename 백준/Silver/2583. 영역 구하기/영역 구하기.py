m, n, k = map(int, input().split())
graph = [[0] * n for _ in range(m)]
dx = [1,-1,0,0]
dy = [0,0,-1,1]

for _ in range(k):
    x1, y1, x2, y2 = list(map(int, input().split()))

    for i in range(y1,y2):
        for j in range(x1,x2):
            graph[m-1-i][j] = 1

def dfs(i, j):
    count = 1
    stack = []
    stack.append((i, j))
    graph[i][j] = 1

    while stack:
        x, y = stack.pop()

        for a in range(4):
            nx = x + dx[a]
            ny = y + dy[a]

            if nx < 0 or nx >= m or ny < 0 or ny >= n:
                continue
            if graph[nx][ny] == 0:
                count += 1
                graph[nx][ny] = 1
                stack.append((nx, ny))
    return count

cnt = 0
li = []
for i in range(m):
    for j in range(n):
        if graph[i][j] == 0:
            cnt += 1
            li.append(dfs(i, j))
li.sort()
print(cnt)
print(*li)