from collections import deque
m, n, h = map(int, input().split())

main_lst = [[] for _ in range(h)] 

dx = [1,-1,0,0]
dy = [0,0,1,-1]
dz = [1,-1]

for i in range(h):
    for _ in range(n):
        main_lst[i].append(list(map(int, input().split())))
# print(main_lst)
queue = deque()

def bfs():
    while queue:
        z, x, y = queue.popleft()

        for b in range(2):
            z_ = dz[b] + z

            if z_ < 0 or z_ >= h:
                continue
            if main_lst[z_][x][y] == 0:
                main_lst[z_][x][y] = main_lst[z][x][y] + 1
                queue.append((z_, x, y))

        for a in range(4):
            x_ = dx[a] + x
            y_ = dy[a] + y

            if x_ < 0 or x_ >= n or y_ < 0 or y_ >= m: # 본인이 밖으로 나가는 경우
                continue
            
            if main_lst[z][x_][y_] == 0:
                main_lst[z][x_][y_] = main_lst[z][x][y] + 1
                queue.append((z,x_,y_))


for i in range(h):
    for j in range(n):
        for k in range(m):
            if main_lst[i][j][k] == 1:
                queue.append((i,j,k))
bfs()


res = 0
for i in main_lst:
    for j in i:
        if 0 in j:
            print(-1)
            exit(0)
        if max(j) > res:
            res = max(j)
print(res - 1) # 처음 본인 일수는 빼야한다