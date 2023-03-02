from collections import deque 
n = int(input())
paint = [list(input()) for _ in range(n)]


dx = [1,-1,0,0]
dy = [0,0,-1,1]

def bfs(i, j, c):
    queue = deque()
    queue.append((i, j))
    paint[i][j] = c.lower()

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue
            if paint[nx][ny] == c:
                paint[nx][ny] = c.lower()
                queue.append((nx, ny))

def bfs2(i, j, c, c2):
    queue = deque()
    queue.append((i, j))
    paint[i][j] = 2

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue

            if paint[nx][ny] == c or paint[nx][ny] == c2:
                paint[nx][ny] = 2
                queue.append((nx, ny))

cnt = 0
for i in range(n):
    for j in range(n):
        if paint[i][j] == 'R':
            cnt += 1
            bfs(i, j, 'R')
        elif paint[i][j] == 'B':
            cnt += 1
            bfs(i, j, 'B')
        elif paint[i][j] == 'G':
            cnt += 1
            bfs(i, j, 'G')
cnt2 = 0
for i in range(n):
    for j in range(n):
        if paint[i][j] == 'r' or paint[i][j] == 'g':
            cnt2 += 1
            bfs2(i, j, 'r', 'g')

        elif paint[i][j] == 'b':
            cnt2 += 1
            bfs2(i, j, 'b', 'b')
print(cnt, cnt2)