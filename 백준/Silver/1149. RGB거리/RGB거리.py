n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

# 3경우를 다 보고, 모든 경로를 다 탐색한다 최종적으로 가장 작기만 하고 조건에 부합하면 그만이다
for i in range(1, n):
    graph[i][0] = min(graph[i - 1][1], graph[i - 1][2]) + graph[i][0]

    graph[i][1] = min(graph[i - 1][0], graph[i - 1][2]) + graph[i][1]

    graph[i][2] = min(graph[i - 1][1], graph[i - 1][0]) + graph[i][2]
print(min(graph[n-1])) # 가장 마지막에서 가장 작은 수를 골라내는게 핵심인 것