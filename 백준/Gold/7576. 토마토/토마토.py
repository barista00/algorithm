from collections import deque

M, N = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
queue = deque()

dx = [1,-1,0,0]
dy = [0,0,1,-1]

def bfs():
    while queue:
        x, y = queue.popleft()
        
        for a in range(4):
            x_ = dx[a] + x
            y_ = dy[a] + y
            
            if x_ < 0 or x_ >= N or y_ < 0 or y_ >= M:
                continue
            
            if graph[x_][y_] == 0:
                graph[x_][y_] = 1 + graph[x][y]
                queue.append((x_, y_))

for i in range(N):
    for j in range(M):
        if graph[i][j] == 1:
            queue.append((i, j))
            
bfs()
li = []
for i in graph:
    li.append(max(i))
    for j in i:
        if j == 0:
            print(-1)
            exit(0)
print(max(li) - 1)