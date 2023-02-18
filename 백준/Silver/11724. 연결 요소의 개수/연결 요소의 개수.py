N, M = map(int, input().split())

lst = [[] for _ in range(N+1)] # 그냥 리스트 [] * N 하는거랑 다른 결과다
for _ in range(M):
    num1, num2 = map(int, input().split())
    lst[num1].append(num2)
    lst[num2].append(num1)
# print(lst)

visited = [False] * (N+1)

def dfs(a):
    start = [a]
    visited[a] = True
    while True:
        if start == []:
            break
        else:
            start_pop = start.pop()

            for i in lst[start_pop]:
                if visited[i] == False:
                    visited[i] = True
                    start.append(i)


cnt = 0
for i in range(1,N+1):
    if visited[i] == False:
        cnt += 1
        dfs(i)
print(cnt)
# 재귀함수 활용을 좀 해보면 좋을 것 같다 지금 상황은 좀 쓸데없이 동작한느 코드가 많은듯 함