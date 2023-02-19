N = int(input())
graph = [list(map(int, input())) for _ in range(N)]


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(a, b):
    lst = [(a, b)]
    graph[a][b] = 0
    넓이 = 1
    while lst:
        c,d = lst.pop()

        for i in range(4):
            x_ = dx[i] + c
            y_ = dy[i] + d

            if x_ < 0 or x_ >= N or y_ < 0 or y_ >= N:
                continue
            if graph[x_][y_] == 1:
                graph[x_][y_] = 0
                lst.append((x_,y_))
                넓이 += 1
    return 넓이

cnt = 0
단지개수 = []
for i in range(N):
    for j in range(N):
        if graph[i][j] == 1:
            cnt += 1
            단지개수.append(dfs(i, j))

print(cnt)
if 단지개수 == []:
    print(0)
else:
    단지개수.sort()
    for i in 단지개수:
        print(i)