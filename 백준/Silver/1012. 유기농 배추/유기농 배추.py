T = int(input())

for _ in range(T):
    M, N, K = map(int, input().split())
    cab = [[0] * M for _ in range(N)]

    for _ in range(K):
        a, b = map(int, input().split())
        cab[b][a] = 1

    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    def dfs(x, y):
        stack = [(x, y)]
        cab[x][y] = 0

        while stack:
            c, d = stack.pop()

            for i in range(4):
                x_ = c + dx[i]
                y_ = d + dy[i]

                if x_ < 0 or x_ >= N or y_ < 0 or y_ >= M:
                    continue

                if cab[x_][y_] == 1:
                    stack.append((x_, y_))
                    cab[x_][y_] = 0

    cnt = 0
    for i in range(N):
        for j in range(M):
            if cab[i][j] == 1:
                dfs(i, j)
                cnt += 1
    print(cnt)