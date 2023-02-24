from collections import deque
n, k = map(int, input().split())
visited = [0] * 100001

def bfs(n, k):
    queue = deque()
    queue.append(n)
    visited[n] = 1
    
    while queue:
        cur = queue.popleft()
        if cur == k:
            return visited[cur] - 1 # 이미 밑에서 visited[k] 값을 바꿔주고 append되었고 시작이 1부터 시작했기 때문에 -1해서 출력해준다

        for i in (cur-1, cur+1, cur*2): # bfs문제는 이렇게 현재위치에서 이동하는 위치를 어떻게 잘 지정해서 구하느냐의 문제인 것 같다

            if i < 0 or i >= 100001:
                continue

            if visited[i] == 0:
                visited[i] = visited[cur] + 1
                queue.append(i)

print(bfs(n, k))