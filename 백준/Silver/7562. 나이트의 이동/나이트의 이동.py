from collections import deque
T = int(input())

for t in range(T):
    n = int(input())
    chess = [[0] * n for _ in range(n)]

    kni, ght = map(int, input().split())
    desti, nation = map(int, input().split())

    # +1,+2 -1+2 +1,-2 -1,-2 +2,+1 +2,-1 -2,+1 -2,-1
    search = [(1,2), (-1,2), (1,-2), (-1,-2), (2,1), (2,-1), (-2,1), (-2,-1)]

    def bfs(kni, ght):
        queue = deque()
        queue.append((kni, ght))
        chess[kni][ght] = 1

        while True:
            x, y = queue.popleft()

            for i in search:
                x_ = i[0] + x
                y_ = i[1] + y

                if x_ < 0 or x_ >= n or y_ < 0 or y_ >= n:
                    continue

                if chess[x_][y_] == 0:
                    chess[x_][y_] = chess[x][y] + 1
                    queue.append((x_,y_))
            
            if x == desti and y == nation:
                break
    bfs(kni, ght)

    print(chess[desti][nation] - 1)