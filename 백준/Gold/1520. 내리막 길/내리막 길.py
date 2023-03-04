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
# 설명
# 결국은 처음부터 마지막 graph[n-1][m-1]까지 도달하는 경우만 계산하면 되는 것이다
# 마지막부분에 닿았다면 그 순간 하나의 루트를 모두 마지막 리턴값인 1을 더하면서 재귀를 끝낸다
# 그러면 가장 최초의 루트는 전부1의 값을 가지게 된다
# 그다음 여러갈래로 나뉜경우의 루트가 이미 최초로 도달한 루트와 겹친다면 굳이 끝까지 들어가지 않아도된다
# 그래서 이미 값이 바뀐 루트를 만났다면 그 즉시 재귀를 종료시키면서 원래 출발한 원점까지 이미 만난 루트의 visited값을 더하면서 복귀한다
# 이과정을 반복하면 결국 가장 최초의 출발한 지점의 visited가 갈 수있는 루트만 더한 값이 나오게 된다