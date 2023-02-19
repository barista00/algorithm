from collections import deque
N = int(input())
person1, person2 = map(int, input().split())
M = int(input())

lst = [[] for _ in range(N+1)]
visited = [False] * (N + 1)
check_li = [0] * (N + 1)

for _ in range(M):
    a, b = map(int, input().split())
    lst[a].append(b)
    lst[b].append(a)


def bfs(a):
    queue = deque()
    queue.append(a)
    visited[a] = True
    
    while queue:
        pop_num = queue.popleft()

        for i in lst[pop_num]:
            if visited[i] == False:
                queue.append(i)
                check_li[i] = check_li[pop_num] + 1 # 노드로 생각하면 된다 본인 노드에있는 데이터는 1촌 다음 이어진 노드 데이터들은 모두 2촌 그다음은 3촌.....이렇게 쭉 카운트한다
                visited[i] = True
bfs(person1)
if check_li[person2] == 0:
    print(-1)
else:
    print(check_li[person2])