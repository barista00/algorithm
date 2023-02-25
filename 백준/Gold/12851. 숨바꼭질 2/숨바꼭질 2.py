from collections import deque
n, k = map(int, input().split())
visited = [0] * 100001

cnt = 0 
def bfs(n, k):
    global cnt
    queue = deque()
    queue.append(n)
    visited[n] = 1
    
    while queue:
        cur = queue.popleft()
        if cur == k:
            cnt += 1 

        for i in (cur-1, cur+1, cur*2): # bfs문제는 이렇게 현재위치에서 이동하는 위치를 어떻게 잘 지정해서 구하느냐의 문제인 것 같다

            if i < 0 or i >= 100001:
                continue

            if visited[i] == 0 or visited[cur] + 1 == visited[i]: # 처음 i가 k와 같다면 k는 0이라 최단거리로 바꿔준다
                visited[i] = visited[cur] + 1                       # 같은 최단거리에서 k가 되는 i도 append하게 만들어줘야한다
                queue.append(i)                                     # 그래서 조건을 현재위치에서 +1한 값과 바뀌는 값인 i가 같다면 append하게 만들어준다
bfs(n, k)                                                           # 그럼 최단거리+1이상부터 i가 k와 같아도 append되지 않는다
print(visited[k] -1)
print(cnt)