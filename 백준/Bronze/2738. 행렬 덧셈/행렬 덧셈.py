N, M = map(int, input().split()) # 3 3
lst = [list(map(int, input().split())) for _ in range(N)]
lst2 = [list(map(int, input().split())) for _ in range(N)]
new_lst = []
result = []
for i in range(N):
    for j in range(M):
        new_lst.append(lst[i][j] + lst2[i][j])
    result.append(new_lst)
    new_lst = []
for i in result:
    print(*i)