from collections import deque

N, M = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(a, b):
    넓이 = 1
    queue = deque()
    queue.append((a, b))
    matrix[a][b] = 0

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            x_ = dx[i] + x
            y_ = dy[i] + y

            if x_ < 0 or x_ >= N or y_ < 0 or y_ >= M:
                continue
            
            if matrix[x_][y_] == 0:
                continue

            if matrix[x_][y_] == 1:
                queue.append((x_, y_))
                matrix[x_][y_] = 0
                넓이 += 1
    return 넓이

cnt = 0
lst = []
for i in range(N):
    for j in range(M):
        if matrix[i][j] == 1:
            cnt += 1
            lst.append(bfs(i, j))
print(cnt)
if lst == []:
    print(0)
else:
    print(max(lst))