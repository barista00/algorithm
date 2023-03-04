from collections import deque
N = int(input())

matrix = [[] for _ in range(N+1)]
for _ in range(N-1):
    a, b = map(int, input().split())
    matrix[a].append(b)
    matrix[b].append(a)

visited = [0 for _ in range(N+1)]

queue = deque()
queue.append(1)
visited[1] = 1 # 첫 시작은 1로 1이 부모로 스타트 한다

while queue:
    q_num = queue.popleft()

    for i in matrix[q_num]: # 반복문으로 확인중인 노드를 visited[i]로 확인 했을 때 이미 그 인덱스가 1이라면 찾는 노드의 부모라는 의미
        if visited[i] == 0:
            visited[i] = q_num
            queue.append(i)

for i in visited[2:]:
    print(i)