while True:
    n, m = map(int, input().split())
    if n == 0 and m == 0:
        break

    lst = []
    for _ in range(m):
        lst.append(list(map(int, input().split())))

    def dfs(x, y):
        if x <= -1 or x >= m or y <= -1 or y >= n:
            return False
        if lst[x][y] == 1:
            lst[x][y] = 0

            dfs(x+1,y)
            dfs(x-1,y)
            dfs(x,y+1)
            dfs(x,y-1)
            dfs(x+1,y-1)
            dfs(x-1,y+1)
            dfs(x+1,y+1)
            dfs(x-1,y-1)
            # 재귀함수 호출 하면 발생하는 상황을 머릿속에 잘 시뮬 돌리면 더 잘 이해될듯
            return True
        return False
    
    land = 0
    for i in range(m):
        for j in range(n):
            if dfs(i, j) == True:
                land += 1
    print(land)